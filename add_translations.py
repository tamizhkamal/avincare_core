#!/usr/bin/env python
"""
Add Tamil translations for new about.html strings
"""
import polib
from pathlib import Path

# Tamil translations for about.html
tamil_translations = {
    "Years Experience": "ஆண்டுகளின் அனுபவம்",
    "About Avin Shukri Pharmaceuticals": "அவின் சுக்ரி பார்மாசியூட்டிக்கல்ஸ் பற்றி",
    "Our Comprehensive Product Portfolio:": "எங்கள் விரிவான தயாரிப்பு போர்ட்ஃபோலியோ:",
    "Injections": "ஊசிகள்",
    "Tablets": "மாத்திரைகள்",
    "Capsules": "காப்ஸுல்கள்",
    "Ointments": "களிம்புகள்",
    "Creams": "கிரீம்கள்",
    "Dry Syrups": "உலர் சிரப்புகள்",
    "Oral Suspensions": "வாய்வழி சஸ்பென்ஷன்கள்",
    "Countries Served": "சேவை செய்யப்பட்ட நாடுகள்",
    "Product Range": "தயாரிப்பு வரம்பு",
    "Quality Standards": "தரத்தின் தரநிலைகள்",
    "Our Vision, Mission & Values": "எங்கள் பார்வை, மிஷன் & மதிப்புகள்",
    "Vision": "பார்வை",
    "Mission": "மிஷன்",
    "Core Values": "முக்கிய மதிப்புகள்",
    "Market Challenges & Our Solutions": "சந்தை சவால்கள் & எங்கள் தீர்வுகள்",
    "Market Problems": "சந்தை சிக்கல்கள்",
    "Regulatory and Market Entry Barriers": "ஒழுங்குமுறை மற்றும் சந்தை நுழைவு தடைகள்",
    "Supply Chain Inefficiencies": "விநியோக சங்கிலி திறமையின்மை",
    "Inconsistent Quality Standards": "சீரற்ற தரத்தின் தரநிலைகள்",
    "Lack of Access to Affordable Medicines": "மலிவான மருந்துகளுக்கான அணுகலின் பற்றாக்குறை",
    "Our Solutions": "எங்கள் தீர்வுகள்",
    "Offering Cost-Effective, High-Quality Products": "செலவு-பயனுள்ள, உচ்চ-தர தயாரிப்புகளை வழங்குதல்",
    "Maintaining Stringent Quality Control": "கடுமையான தரக் கட்டுப்பாட்டை பராமரித்தல்",
    "Streamlining Distribution Networks": "விநியோग வலையமைப்பை இலினியமாக்குதல்",
    "Navigating Global Compliance": "உலகளாவிய இணக்கத்தைத் தொடர்தல்",
    "Quality": "தரம்",
    "Integrity": "நேர்மை",
    "Innovation": "புதுமை",
    "Global Responsibility": "உலகளாவிய பொறுப்பு",
    "Partnership": "கூட்டு வேலை",
}

# Read the Tamil .po file
ta_po_path = Path('locale/ta/LC_MESSAGES/django.po')
po = polib.pofile(str(ta_po_path))

# Add new translations
added = 0
for english, tamil in tamil_translations.items():
    existing = po.find(english)
    if not existing:
        entry = polib.POEntry(msgid=english, msgstr=tamil)
        po.append(entry)
        added += 1
        print(f"✓ Added: {english} → {tamil}")
    else:
        if not existing.msgstr:
            existing.msgstr = tamil
            print(f"✓ Updated: {english} → {tamil}")

# Save the updated .po file
po.save(str(ta_po_path))
print(f"\n✅ Added {added} new translations to Tamil .po file")
print(f"📝 Total entries in file: {len(po)}")
