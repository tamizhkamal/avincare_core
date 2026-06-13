# Django i18n (Internationalization) Setup Guide

## Current Setup Status ✅

Your project has multilingual support configured for:
- **English** (en) - Default
- **Tamil** (ta)
- **Arabic** (ar)
- **French** (fr)

## How Language Switching Works

1. **Language Switcher** - Located in the navbar (globe icon)
2. **URL Structure** - Language prefix in URLs:
   - English: `/en/` or `/` (default)
   - Tamil: `/ta/`
   - Arabic: `/ar/`
   - French: `/fr/`
3. **Language Session** - User's choice is stored in the session

## How to Add Translations

### Step 1: Mark Text for Translation in Templates

Use the `{% load i18n %}` tag and wrap text with `{% trans "..." %}`

```django
{% load i18n %}

<h1>{% trans "Welcome to our site" %}</h1>
<p>{% trans "This is a translatable paragraph." %}</p>

<!-- For longer blocks, use blocktrans -->
{% blocktrans %}
    This is a longer translatable text block
    that can span multiple lines.
{% endblocktrans %}
```

### Step 2: Mark Strings in Python Code

For strings in views.py or models.py, use:

```python
from django.utils.translation import gettext_lazy as _

class MyModel(models.Model):
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', _('Active')),
            ('inactive', _('Inactive')),
        ]
    )

def my_view(request):
    message = _('This is a translatable message')
```

### Step 3: Extract Translatable Strings

**Run this command to find all strings marked for translation:**

```bash
python manage.py makemessages -a
```

This creates/updates `.po` files in the `locale/` directory

### Step 4: Translate the Strings

Edit the `.po` files in:
- `locale/ta/LC_MESSAGES/django.po` (Tamil)
- `locale/ar/LC_MESSAGES/django.po` (Arabic)
- `locale/fr/LC_MESSAGES/django.po` (French)

Example `.po` file format:
```
#: templates/index.html:15
msgid "Welcome to our site"
msgstr "நமது தளத்திற்கு வரவேற்கிறோம்"

#: templates/index.html:20
msgid "This is a translatable paragraph."
msgstr "இது ஒரு மொழிபெயர்ப்பு பத்தி."
```

### Step 5: Compile Translations

**Option A - Using the provided script:**
```bash
python compile_translations.py
```

**Option B - Using Django (requires gettext tools):**
```bash
python manage.py compilemessages
```

## Files Modified

✅ **base.html** - Fixed `get_current_language` tag
✅ **index.html** - Added `{% load i18n %}` and marked main content for translation
✅ **views.py** - Updated to use Django's built-in set_language view
✅ **Created compile_translations.py** - For compiling .po files without gettext

## Current Translation Files

```
locale/
├── ar/LC_MESSAGES/
│   ├── django.po     (translations to translate)
│   └── django.mo     (compiled - ready to use) ✅
├── fr/LC_MESSAGES/
│   ├── django.po
│   └── django.mo     ✅
└── ta/LC_MESSAGES/
    ├── django.po
    └── django.mo     ✅
```

## Quick Commands

```bash
# Extract new translatable strings
python manage.py makemessages -a

# Compile .po files to .mo (with polib)
python compile_translations.py

# Update translations for specific language
python manage.py makemessages -l ta
python manage.py makemessages -l ar
python manage.py makemessages -l fr

# Start the server
python manage.py runserver

# Clear old translations cache
python manage.py compilemessages --ignore=node_modules
```

## Testing Translations

1. Open http://127.0.0.1:8000/
2. Click the language switcher (globe icon in navbar)
3. Select a language (Tamil, Arabic, French)
4. The page should reload in that language

## Translation String Reference

For template files use:
- `{% trans "..." %}` - For single line strings
- `{% blocktrans %}...{% endblocktrans %}` - For multi-line strings
- `{{ variable|translate }}` - For filters (less common)

For Python code use:
- `_("...")` or `gettext("...")` - Import as: `from django.utils.translation import gettext_lazy as _`
- Use `gettext_lazy` for models/forms to delay evaluation

## Next Steps

1. ✅ Extract strings: `python manage.py makemessages -a`
2. 📝 Add translations in the `.po` files
3. 🔧 Compile translations: `python compile_translations.py`
4. 🧪 Test language switcher
5. 🚀 Deploy and verify

## Useful Resources

- Django i18n docs: https://docs.djangoproject.com/en/5.2/topics/i18n/
- Poedit (GUI editor for .po files): https://poedit.net/
- gettext tools: https://www.gnu.org/software/gettext/
