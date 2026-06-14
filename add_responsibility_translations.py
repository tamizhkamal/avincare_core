#!/usr/bin/env python
"""
Add Tamil translations for responsibility.html strings
"""
import polib
from pathlib import Path

# Tamil translations for responsibility.html
tamil_translations = {
    "Corporate Social Responsibility": "கூட்டு சமூக பொறுப்பு",
    "Our Commitment to Sustainable Healthcare Development": "நகரும் சுகாதாரப் பாதுகாப்பு வளர்ச்சிக்கான எங்கள் வாக்குறுதி",
    "Our CSR Philosophy": "எங்கள் கூட்டு சமூக பொறுப்பு தத்துவம்",
    "Healthcare Access": "சுகாதாரப் பாதுகாப்பு அணுகல்",
    "Environmental Stewardship": "சுற்றுச்சூழல் நிர்வாகம்",
    "Key Initiatives": "முக்கிய முயற்சிகள்",
    "Community Health Programs": "சமூக சுகாதார நிரல்கள்",
    "Education & Training": "கல்வி & பயிற்சி",
    "Global Health Partnerships": "உலகளாவிய சுகாதார கூட்டு வேலைகள்",
    "Our Impact": "எங்கள் விளைவு",
    "Lives Impacted": "பாதிக்கப்பட்ட வாழ்க்கைகள்",
    "Economic Value": "பொருளாதார மதிப்பு",
    "Future Commitments": "எதிர்கால வாக்குறுதிகள்",
    "Sustainability Goals": "நிலைத்தன்மை இலக்குகள்",
}

# Read the Tamil .po file
ta_po_path = Path('locale/ta/LC_MESSAGES/django.po')
po = polib.pofile(str(ta_po_path))

# Add new translations
added = 0
updated = 0
for english, tamil in tamil_translations.items():
    existing = po.find(english)
    if not existing:
        entry = polib.POEntry(msgid=english, msgstr=tamil)
        po.append(entry)
        added += 1
        print(f"✓ Added: {english}")
    else:
        if not existing.msgstr:
            existing.msgstr = tamil
            updated += 1
            print(f"✓ Updated: {english}")

# Save the updated .po file
po.save(str(ta_po_path))
print(f"\n✅ Added {added} new translations")
print(f"✅ Updated {updated} translations")
print(f"📝 Total entries in file: {len(po)}")
