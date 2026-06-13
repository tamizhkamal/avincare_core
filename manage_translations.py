#!/usr/bin/env python
"""
Django i18n Translation Management Script
Helps manage translations without needing gettext tools installed
"""
import os
import sys
import subprocess
import argparse
from pathlib import Path

def setup_path():
    """Add the project to Python path"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avincare_core.settings')
    BASE_DIR = Path(__file__).resolve().parent
    sys.path.insert(0, str(BASE_DIR))

def extract_messages():
    """Extract translatable strings from the project"""
    print("\n📝 Extracting translatable strings...")
    os.system('python manage.py makemessages -a')
    print("✅ Extraction complete!")

def compile_messages():
    """Compile .po files to .mo files"""
    print("\n🔧 Compiling translations...")
    
    try:
        import polib
    except ImportError:
        print("⚠️  Installing polib...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "polib"])
        import polib
    
    BASE_DIR = Path(__file__).resolve().parent
    LOCALE_DIR = BASE_DIR / 'locale'
    
    if not LOCALE_DIR.exists():
        print(f"❌ Locale directory not found: {LOCALE_DIR}")
        return False
    
    po_files_found = False
    for po_file in LOCALE_DIR.rglob('django.po'):
        po_files_found = True
        try:
            po = polib.pofile(str(po_file))
            mo_file = po_file.with_suffix('.mo')
            po.save_as_mofile(str(mo_file))
            print(f"  ✓ {po_file.relative_to(BASE_DIR)}")
        except Exception as e:
            print(f"  ✗ Error with {po_file}: {e}")
            return False
    
    if po_files_found:
        print("✅ Compilation complete!")
        return True
    else:
        print("⚠️  No .po files found. Run extract first.")
        return False

def update_language(language):
    """Update translations for a specific language"""
    print(f"\n📝 Updating {language} translations...")
    os.system(f'python manage.py makemessages -l {language}')
    print(f"✅ {language} updated! Now edit locale/{language}/LC_MESSAGES/django.po")

def list_languages():
    """List available languages and their status"""
    print("\n📚 Available Languages:\n")
    
    BASE_DIR = Path(__file__).resolve().parent
    LOCALE_DIR = BASE_DIR / 'locale'
    
    languages = {
        'ta': 'Tamil (தமிழ்)',
        'ar': 'Arabic (العربية)',
        'fr': 'French (Français)',
        'en': 'English (Default)'
    }
    
    for code, name in languages.items():
        if code == 'en':
            print(f"  • {code}: {name}")
            continue
            
        po_file = LOCALE_DIR / code / 'LC_MESSAGES' / 'django.po'
        mo_file = po_file.with_suffix('.mo')
        
        status = ""
        if po_file.exists() and mo_file.exists():
            status = "✅ Ready"
        elif po_file.exists():
            status = "🔄 Needs compilation"
        else:
            status = "❌ Not created"
        
        print(f"  • {code}: {name} {status}")

def open_po_file(language):
    """Open .po file in default editor"""
    BASE_DIR = Path(__file__).resolve().parent
    po_file = BASE_DIR / 'locale' / language / 'LC_MESSAGES' / 'django.po'
    
    if not po_file.exists():
        print(f"❌ File not found: {po_file}")
        return
    
    print(f"\n📝 Opening {language} translations...")
    print(f"File: {po_file}")
    
    # Try to open with default editor
    if sys.platform == 'win32':
        os.startfile(str(po_file))
    elif sys.platform == 'darwin':
        os.system(f'open "{po_file}"')
    else:
        os.system(f'xdg-open "{po_file}"')

def show_help():
    """Show help information"""
    help_text = """
╔════════════════════════════════════════════════════════════════════════════╗
║                  Django i18n Translation Manager                          ║
║                                                                            ║
║  A tool to manage translations without needing gettext installed          ║
╚════════════════════════════════════════════════════════════════════════════╝

USAGE:
  python manage_translations.py [COMMAND]

COMMANDS:
  extract              Extract new translatable strings from templates/code
  compile              Compile .po files to .mo (binary format)
  update LANGUAGE      Update translations for specific language (ta/ar/fr)
  list                 Show available languages and their status
  edit LANGUAGE        Open .po file in default editor (ta/ar/fr)
  full                 Run complete workflow: extract → compile

EXAMPLES:
  # Extract all translatable strings
  python manage_translations.py extract

  # Compile translations
  python manage_translations.py compile

  # Update Tamil translations
  python manage_translations.py update ta

  # Open French .po file for editing
  python manage_translations.py edit fr

  # Complete workflow
  python manage_translations.py full

WORKFLOW:
  1. Extract:  python manage_translations.py extract
  2. Edit:     python manage_translations.py edit ta  (or ar/fr)
  3. Compile:  python manage_translations.py compile
  4. Test:     python manage.py runserver
     Then visit http://localhost:8000/ and test language switcher

SUPPORTED LANGUAGES:
  • ta - Tamil (தமிழ்)
  • ar - Arabic (العربية)
  • fr - French (Français)

TIPS:
  • Use Poedit (https://poedit.net/) for a GUI editor
  • Always compile after editing .po files
  • Test language switching before deploying

DOCUMENTATION:
  See TRANSLATION_GUIDE.md for detailed instructions
    """
    print(help_text)

def main():
    setup_path()
    
    parser = argparse.ArgumentParser(
        description='Django i18n Translation Manager',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Run "python manage_translations.py -h" for more help'
    )
    
    parser.add_argument(
        'command',
        nargs='?',
        default='help',
        choices=['extract', 'compile', 'update', 'list', 'edit', 'full', 'help'],
        help='Command to execute'
    )
    
    parser.add_argument(
        'language',
        nargs='?',
        default=None,
        choices=['ta', 'ar', 'fr'],
        help='Language code (for update/edit commands)'
    )
    
    args = parser.parse_args()
    
    try:
        if args.command == 'extract':
            extract_messages()
        
        elif args.command == 'compile':
            compile_messages()
        
        elif args.command == 'update':
            if not args.language:
                print("❌ Please specify a language: ta, ar, or fr")
                sys.exit(1)
            update_language(args.language)
        
        elif args.command == 'list':
            list_languages()
        
        elif args.command == 'edit':
            if not args.language:
                print("❌ Please specify a language: ta, ar, or fr")
                sys.exit(1)
            open_po_file(args.language)
        
        elif args.command == 'full':
            extract_messages()
            input("\n⏸️  Press Enter after updating translations...")
            compile_messages()
        
        else:
            show_help()
    
    except KeyboardInterrupt:
        print("\n\n⏹️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
