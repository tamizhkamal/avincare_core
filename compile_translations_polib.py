#!/usr/bin/env python
"""
Compile .po files to .mo files using polib
"""
from pathlib import Path
import polib

locale_path = Path('locale')

print("🔧 Compiling translations...")

for lang_dir in locale_path.iterdir():
    if lang_dir.is_dir() and lang_dir.name != '__pycache__':
        po_file = lang_dir / 'LC_MESSAGES' / 'django.po'
        mo_file = lang_dir / 'LC_MESSAGES' / 'django.mo'
        
        if po_file.exists():
            try:
                po = polib.pofile(str(po_file))
                po.save_as_mofile(str(mo_file))
                print(f"  ✓ {lang_dir.name}: Compiled to {mo_file}")
            except Exception as e:
                print(f"  ✗ {lang_dir.name}: Error - {e}")
        else:
            print(f"  ✗ {lang_dir.name}: .po file not found")

print("\n✅ Compilation complete!")
print("🌐 Now test your translations at http://localhost:8000/")
