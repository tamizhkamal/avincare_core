#!/usr/bin/env python
"""
Extract missing translatable strings from templates and add to .po files
"""
import re
from pathlib import Path
import polib

def extract_trans_strings(template_path):
    """Extract {% trans "..." %} strings from Django templates"""
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all {% trans "..." %} patterns
    pattern = r'{%\s*trans\s+"([^"]+)"\s*%}'
    matches = re.findall(pattern, content)
    return list(set(matches))  # Remove duplicates

def add_to_po_file(po_path, strings_dict):
    """Add strings to a .po file"""
    po = polib.pofile(po_path)
    
    added_count = 0
    for english, translation in strings_dict.items():
        # Check if entry already exists
        existing = po.find(english)
        if not existing:
            entry = polib.POEntry(msgid=english, msgstr=translation)
            po.append(entry)
            added_count += 1
    
    po.save(po_path)
    return added_count

# Extract strings from index.html
template_path = Path('members/templates/index.html')
extracted = extract_trans_strings(str(template_path))

print(f"📝 Found {len(extracted)} translatable strings")
print("\nMissing strings from Products, Vision, Mission, Core Values sections:")
for s in extracted:
    if any(keyword in s for keyword in ['Products', 'Vision', 'Mission', 'Core', 'Quality', 'Integrity', 'Innovation', 'Global Responsibility', 'Antibiotics', 'Anti-inflammatory', 'Gastrointestinal', 'Vitamins', 'WHO-GMP', 'Ready to Partner', 'Contact Us Today']):
        print(f"  - {s}")

# Tamil translations for missing strings
tamil_translations = {
    "Our Products": "எங்கள் தயாரிப்புகள்",
    "Avin Shukri Pharmaceuticals currently markets 15 pharmaceutical brands across different therapeutic segments, with 10 additional products scheduled for launch.": "அவின் சுக்ரி பார்மாசியூட்டிக்கல்ஸ் தற்போது 15 மருந்து பிராண்ட்களை வெவ்வேறு சிகிச்சை பிரிவுகளில் சந்தைப்படுத்துகிறது, 10 கூடுதல் தயாரிப்புகள் வெளியீடுக்கு திட்டமிட்டு உள்ளன.",
    "Antibiotics": "நுண்ணுயிர்",
    "Quality antibiotic medications for various infections": "பல்வேறு தொற்றுகளுக்கான உச்சமான நுண்ணுயிர்க்கொல்லி மருந்துகள்",
    "Anti-inflammatory": "அழற்சி எதிர்ப்பு",
    "Effective pain and inflammation management solutions": "பயனுள்ள வலி மற்றும் அழற்சி நிர்வாக தீர்வுகள்",
    "Gastrointestinal": "செரிமான மண்டல",
    "Comprehensive GI tract treatment medications": "விரிவான செரிமான பாதை சிகிச்சை மருந்துகள்",
    "Vitamins & Supplements": "வைட்டமின்கள் மற்றும் சப்ளிமெண்ட்கள்",
    "Essential nutrients for overall health and wellness": "ஒட்டுமொத்த ஆரோக்கியம் மற்றும் நல்வாழ்க்கைக்கான அத்தியாவசிய ஊட்டச்சத்துக்கள்",
    "All products are sourced from WHO-GMP certified manufacturing partners.": "அனைத்து பொருட்களும் WHO-GMP சான்றளிக்கப்பட்ட உற்பாதன கூட்டாளிகளிடமிருந்து பெறப்படுகின்றன.",
    "Our Vision": "எங்கள் பார்வை",
    "To become a globally recognized pharmaceutical company delivering high-quality, affordable medicines while contributing to improved healthcare outcomes across emerging and developing markets.": "வளர்ந்து வரும் மற்றும் வளரும் சந்தைகளில் சுகாதார விளைவுகளை மேம்படுத்துவதில் பங்களிக்கும் போது உயர்தர, மலிவான மருந்துகளை வழங்கும் உலகளாவிய அங்கீகாரம் பெற்ற மருந்து நிறுவனமாக வேண்டியுள்ளது.",
    "Our Mission": "எங்கள் மிஷன்",
    "Provide high-quality and affordable pharmaceutical products": "உயர்தர மற்றும் மலிவான மருந்து தயாரிப்புகளை வழங்குங்கள்",
    "Expand presence across global healthcare markets": "உலகளாவிய சுகாதார சந்தைகளில் முன்னிலையை விரிவாக்குங்கள்",
    "Build strong partnerships with reliable manufacturers and distributors": "நம்பகமான உற்பாதகர்கள் மற்றும் விநியோகஸ்தர்களுடன் வலுவான கூட்டு வேலைகளை கட்டுங்கள்",
    "Ensure ethical marketing and responsible business practices": "நைதிக சந்தைப்படுத்தல் மற்றும் பொறுப்புள்ள வணிக நடைமுறைகளை உறுதிப்படுத்துங்கள்",
    "Establish our own pharmaceutical manufacturing facilities in the future": "எதிர்காலத்தில் எங்கள் சொந்த மருந்து உற்பத்தி வசதிகளை நிறுவுங்கள்",
    "Core Values": "முக்கிய மதிப்புகள்",
    "Quality": "தரம்",
    "Ensuring high pharmaceutical standards": "உயர் மருந்து தரநிலைகளை உறுதிப்படுத்துதல்",
    "Integrity": "நேர்மை",
    "Transparent and ethical business practices": "பாரதிர்மான மற்றும் நைதிக வணிக நடைமுறைகள்",
    "Innovation": "புதுமை",
    "Continuous improvement and expansion": "தொடர்ச்சியான முன்னேற்றம் மற்றும் விரிவாக்கம்",
    "Global Responsibility": "உலகளாவிய பொறுப்பு",
    "Improving access to medicines worldwide": "உலகெங்கிலும் மருந்துகளுக்கான அணுகல் மேம்படுத்துதல்",
    "Ready to Partner With Us?": "எங்களுடன் கூட்டு வேலை செய்ய தயாரா?",
    "Join us in our mission to deliver quality healthcare solutions worldwide.": "உலகெங்கிலும் தரமான சுகாதார தீர்வுகளை வழங்கும் எங்கள் கூட்டு மிஷனில் சேரவும்.",
    "Contact Us Today": "இன்று எங்களைத் தொடர்பு கொள்ளுங்கள்",
}

# Arabic translations (partial)
arabic_translations = {
    "Our Products": "منتجاتنا",
    "Antibiotics": "المضادات الحيوية",
    "Anti-inflammatory": "مضادات الالتهاب",
    "Gastrointestinal": "الجهاز الهضمي",
    "Vitamins & Supplements": "الفيتامينات والمكملات",
    "Our Vision": "رؤيتنا",
    "Our Mission": "رسالتنا",
    "Core Values": "القيم الأساسية",
    "Quality": "الجودة",
    "Integrity": "النزاهة",
    "Innovation": "الابتكار",
    "Global Responsibility": "المسؤولية العالمية",
    "Ready to Partner With Us?": "هل تريد الشراكة معنا؟",
    "Contact Us Today": "اتصل بنا اليوم",
}

# French translations (partial)
french_translations = {
    "Our Products": "Nos produits",
    "Antibiotics": "Antibiotiques",
    "Anti-inflammatory": "Anti-inflammatoire",
    "Gastrointestinal": "Gastro-intestinal",
    "Vitamins & Supplements": "Vitamines et suppléments",
    "Our Vision": "Notre vision",
    "Our Mission": "Notre mission",
    "Core Values": "Valeurs fondamentales",
    "Quality": "Qualité",
    "Integrity": "Intégrité",
    "Innovation": "Innovation",
    "Global Responsibility": "Responsabilité mondiale",
    "Ready to Partner With Us?": "Prêt à nous faire équipe?",
    "Contact Us Today": "Contactez-nous aujourd'hui",
}

# Add to .po files
print("\n📝 Adding translations to .po files...")

locale_path = Path('locale')
langs = {
    'ta': tamil_translations,
    'ar': arabic_translations,
    'fr': french_translations,
}

for lang, translations in langs.items():
    po_file = locale_path / lang / 'LC_MESSAGES' / 'django.po'
    if po_file.exists():
        count = add_to_po_file(str(po_file), translations)
        print(f"  ✓ {lang}: Added {count} new strings to {po_file}")
    else:
        print(f"  ✗ {lang}: File not found at {po_file}")

print("\n✅ Done! Now run: python manage.py compilemessages")
