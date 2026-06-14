#!/usr/bin/env python
"""Add Tamil translations for contact page strings."""
from pathlib import Path
import polib

translations = {
    "Contact Us": "எங்களை தொடர்பு கொள்ளுங்கள்",
    "Get in touch with Avin Shukri Pharmaceuticals Private Limited for business inquiries and partnerships": "வணிக விசாரணைகள் மற்றும் கூட்டாண்மைகளுக்காக அவின் சுக்ரி பார்மாசியூட்டிக்கல்ஸ் பிரைவேட் லிமிடெட்டை தொடர்பு கொள்ளுங்கள்",
    "Get In Touch With Us": "எங்களுடன் தொடர்பில் இருங்கள்",
    "We're here to help you with all your pharmaceutical needs. Whether you're looking for product information, business partnerships, or have questions about our global operations, our team is ready to assist you.": "உங்கள் அனைத்து மருந்து தேவைகளுக்கும் உதவ நாங்கள் இருக்கிறோம். தயாரிப்பு தகவல், வணிக கூட்டாண்மை அல்லது எங்கள் உலகளாவிய செயல்பாடுகள் குறித்து கேள்விகள் இருந்தாலும், உங்களுக்கு உதவ எங்கள் குழு தயார்.",
    "Corporate Headquarters": "நிறுவன தலைமையகம்",
    "Phone Number": "தொலைபேசி எண்",
    "Email Address": "மின்னஞ்சல் முகவரி",
    "Business Hours": "வேலை நேரம்",
    "Monday - Friday: 9:00 AM - 6:00 PM": "திங்கள் - வெள்ளி: காலை 9:00 - மாலை 6:00",
    "Saturday: 9:00 AM - 2:00 PM": "சனி: காலை 9:00 - மதியம் 2:00",
    "Sunday: Closed": "ஞாயிறு: மூடப்பட்டது",
    "Send Us a Message": "எங்களுக்கு ஒரு செய்தி அனுப்புங்கள்",
    "Your Name": "உங்கள் பெயர்",
    "Your Email": "உங்கள் மின்னஞ்சல்",
    "Your Phone": "உங்கள் தொலைபேசி",
    "General Inquiry": "பொது விசாரணை",
    "Product Information": "தயாரிப்பு தகவல்",
    "Business Partnership": "வணிக கூட்டாண்மை",
    "Global Distribution": "உலகளாவிய விநியோகம்",
    "Career Opportunities": "வேலை வாய்ப்புகள்",
    "Subject": "பொருள்",
    "Leave a message here": "இங்கே ஒரு செய்தியை எழுதுங்கள்",
    "Your Message": "உங்கள் செய்தி",
    "Send Message": "செய்தி அனுப்பு",
    "Message sent successfully! We'll contact you soon via email and WhatsApp.": "செய்தி வெற்றிகரமாக அனுப்பப்பட்டது! மின்னஞ்சல் மற்றும் வாட்ஸ்அப் மூலம் விரைவில் உங்களை தொடர்பு கொள்வோம்.",
    "Error sending message. Please try again.": "செய்தி அனுப்புவதில் பிழை. தயவுசெய்து மீண்டும் முயற்சிக்கவும்.",
    "Find Our Location": "எங்கள் இருப்பிடத்தை கண்டறியுங்கள்",
    "Visit our corporate headquarters in Chennai, India": "இந்தியாவின் சென்னை நகரில் உள்ள எங்கள் நிறுவன தலைமையகத்தை பார்வையிடுங்கள்",
    "Global Operations": "உலகளாவிய செயல்பாடுகள்",
    "Republic of Chad": "சாட் குடியரசு",
    "Registered & Operational": "பதிவு செய்யப்பட்டு செயல்பாட்டில் உள்ளது",
    "Central Africa Operations": "மத்திய ஆப்பிரிக்க செயல்பாடுகள்",
    "Djibouti": "ஜிபூட்டி",
    "Established Presence": "நிறுவப்பட்ட இருப்பு",
    "Horn of Africa Operations": "ஹார்ன் ஆப் ஆப்பிரிக்கா செயல்பாடுகள்",
    "Expanding Markets": "விரிவாகும் சந்தைகள்",
    "Coming Soon:": "விரைவில் வருகிறது:",
    "Sudan": "சூடான்",
    "Bangladesh": "பங்களாதேஷ்",
    "Seychelles": "செய்ஷெல்ஸ்",
    "Egypt": "எகிப்து",
    "Yemen": "யேமன்",
    "View Global Operations": "உலகளாவிய செயல்பாடுகளை பார்க்க",
    "New Contact Form Submission - Avin Shukri Pharmaceuticals": "புதிய தொடர்பு படிவ சமர்ப்பிப்பு - அவின் சுக்ரி பார்மாசியூட்டிக்கல்ஸ்",
    "Name:": "பெயர்:",
    "Email:": "மின்னஞ்சல்:",
    "Phone:": "தொலைபேசி:",
    "Subject:": "பொருள்:",
    "Message:": "செய்தி:",
    "Network error. Please try again.": "நெட்வொர்க் பிழை. தயவுசெய்து மீண்டும் முயற்சிக்கவும்.",
}

po_path = Path("locale/ta/LC_MESSAGES/django.po")
po = polib.pofile(str(po_path))

added = 0
updated = 0
for msgid, msgstr in translations.items():
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
