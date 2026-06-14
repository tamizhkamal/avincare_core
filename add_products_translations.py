#!/usr/bin/env python
"""Add Tamil translations for products page strings."""
from pathlib import Path
import polib

TRANSLATIONS = {
    "Our Product Portfolio": "எங்கள் தயாரிப்பு தொகுப்பு",
    "15+ Pharmaceutical Brands Across Multiple Therapeutic Segments": "பல சிகிச்சை பிரிவுகளில் 15+ மருந்து பிராண்டுகள்",
    "Featured Products": "முக்கிய தயாரிப்புகள்",
    "Our flagship pharmaceutical products serving diverse therapeutic segments with WHO-GMP certification": "WHO-GMP சான்றிதழுடன் பல்வேறு சிகிச்சை பிரிவுகளுக்கு சேவை செய்யும் எங்கள் முன்னணி மருந்துத் தயாரிப்புகள்",
    "Category:": "வகை:",
    "Antibiotics": "ஆண்டிபயாட்டிக்ஸ்",
    "Type:": "வகை:",
    "Tablet": "மாத்திரை",
    "Strength:": "அளவு:",
    "MRP:": "எம்ஆர்பி:",
    "Product Features:": "தயாரிப்பு அம்சங்கள்:",
    "High Quality": "உயர் தரம்",
    "WHO-GMP Certified": "WHO-GMP சான்றளிக்கப்பட்டது",
    "Effective": "பயனுள்ளது",
    "Broad spectrum antibiotic": "பரந்த செயல்பாட்டுக் கொண்ட ஆண்டிபயாட்டிக்",
    "Available": "கிடைக்கும்",
    "Ready for dispatch": "அனுப்ப தயாராக உள்ளது",
    "Pain Management": "வலி மேலாண்மை",
    "Injection": "ஊசி",
    "Fast pain relief": "வேகமான வலி நிவாரணம்",
    "Dry Syrup": "உலர் சிரப்",
    "Pediatric friendly": "குழந்தைகள் நட்பு",
    "Innovation Products": "புதுமை தயாரிப்புகள்",
    "10+ Upcoming Products in Our Pipeline - Advanced Formulations for Better Healthcare": "எங்கள் পাইப்லைனில் 10+ வரவிருக்கும் தயாரிப்புகள் - சிறந்த சுகாதாரத்திற்கான மேம்பட்ட கலவைகள்",
    "Gastrointestinal": "செரிமான அமைப்பு",
    "Capsule": "காப்ஸ்யூல்",
    "Status:": "நிலை:",
    "Coming Soon": "விரைவில் வருகிறது",
    "Advanced PPI with dual action": "இரட்டை செயல்பாட்டுடன் மேம்பட்ட PPI",
    "Cardiovascular": "இதயநாள் அமைப்பு",
    "Next-gen antihypertensive": "அடுத்த தலைமுறை இரத்த அழுத்த கட்டுப்பாட்டு மருந்து",
    "Respiratory": "சுவாச அமைப்பு",
    "Inhaler": "இன்ஹேலர்",
    "Advanced bronchodilator": "மேம்பட்ட சுவாசவழி விரிவாக்கி",
    "Neurology": "நரம்பியல்",
    "Neuroprotective agent": "நரம்பு பாதுகாப்பு மருந்து",
    "Product Categories": "தயாரிப்பு பிரிவுகள்",
    "Comprehensive Pharmaceutical Solutions Across Multiple Therapeutic Segments": "பல சிகிச்சை பிரிவுகளில் முழுமையான மருந்து தீர்வுகள்",
    "Tablets & Capsules": "மாத்திரைகள் மற்றும் காப்ஸ்யூல்கள்",
    "Wide range of oral formulations including antibiotics, anti-inflammatory, cardiovascular, and gastrointestinal medications": "ஆண்டிபயாட்டிக்ஸ், அழற்சி எதிர்ப்பு, இதயநாள் மற்றும் செரிமான மருந்துகள் உள்ளிட்ட விரிவான வாய்வழி கலவைகள்",
    "Popular Products:": "பிரபலமான தயாரிப்புகள்:",
    "Injectables": "ஊசி மருந்துகள்",
    "Sterile injectable formulations for critical care, antibiotics, and specialized treatments": "அவசர சிகிச்சை, ஆண்டிபயாட்டிக்ஸ் மற்றும் சிறப்பு சிகிச்சைகளுக்கான நுண்ணுயிர் இல்லா ஊசி கலவைகள்",
    "Pediatric Formulations": "குழந்தைகளுக்கான கலவைகள்",
    "Child-friendly formulations including dry syrups, oral suspensions, and drops": "உலர் சிரப்புகள், வாய்வழி சஸ்பென்ஷன்கள் மற்றும் டிராப்ஸ் உள்ளிட்ட குழந்தை நட்பு கலவைகள்",
    "Topical Products": "மேற்பரப்பு பயன்பாட்டு தயாரிப்புகள்",
    "Ointments, creams, and gels for dermatological and pain management applications": "தோல் மற்றும் வலி மேலாண்மை பயன்பாடுகளுக்கான களிம்புகள், கிரீம்கள் மற்றும் ஜெல்கள்",
    "Quality Assurance & Compliance": "தர உறுதி மற்றும் இணக்கம்",
    "Every product meets international standards and regulatory requirements": "ஒவ்வொரு தயாரிப்பும் சர்வதேச தரநிலைகள் மற்றும் ஒழுங்குமுறை தேவைகளை பூர்த்தி செய்கிறது",
    "WHO-GMP Compliance": "WHO-GMP இணக்கம்",
    "World Health Organization Good Manufacturing Practices compliance ensuring product safety and efficacy.": "உலக சுகாதார அமைப்பின் நல்ல உற்பத்தி நடைமுறைகளுடன் இணக்கம் தயாரிப்பு பாதுகாப்பையும் செயல்திறனையும் உறுதிசெய்கிறது.",
    "International Standards": "சர்வதேச தரநிலைகள்",
    "Compliance with global regulatory requirements across all operational markets including Chad, Djibouti, and expanding markets.": "சாட், ஜிபூட்டி மற்றும் விரிவடைந்து வரும் சந்தைகள் உட்பட அனைத்து செயல்பாட்டு சந்தைகளிலும் உலகளாவிய ஒழுங்குமுறை தேவைகளுக்கு இணக்கம்.",
    "Certifications": "சான்றிதழ்கள்",
    "Recognized certifications from national and international regulatory bodies ensuring product quality and safety.": "தயாரிப்பு தரம் மற்றும் பாதுகாப்பை உறுதிப்படுத்தும் தேசிய மற்றும் சர்வதேச ஒழுங்குமுறை அமைப்புகளின் அங்கீகரிக்கப்பட்ட சான்றிதழ்கள்."
}

po_path = Path("locale/ta/LC_MESSAGES/django.po")
po = polib.pofile(str(po_path))

added = 0
updated = 0
for msgid, msgstr in TRANSLATIONS.items():
    entry = po.find(msgid)
    if entry is None:
        po.append(polib.POEntry(msgid=msgid, msgstr=msgstr))
        added += 1
    elif not entry.msgstr.strip():
        entry.msgstr = msgstr
        updated += 1

po.save(str(po_path))
print(f"Added: {added}")
print(f"Updated: {updated}")
print(f"Total entries: {len(po)}")
