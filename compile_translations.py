#!/usr/bin/env python
"""
Compile .po translation files to .mo binary files
This script doesn't require gettext tools to be installed
"""
import os
import sys
import subprocess

# Try using Django's builtin or polib
try:
    import polib
    
    def compile_po_to_mo(po_file):
        """Convert .po file to .mo using polib"""
        po = polib.pofile(po_file)
        mo_file = po_file.replace('.po', '.mo')
        po.save_as_mofile(mo_file)
        print(f"✓ Compiled: {po_file} → {mo_file}")
        return True
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOCALE_DIR = os.path.join(BASE_DIR, 'locale')
    
    if not os.path.exists(LOCALE_DIR):
        print(f"Locale directory not found: {LOCALE_DIR}")
        sys.exit(1)
    
    # Find all .po files and compile them
    po_files_found = False
    for root, dirs, files in os.walk(LOCALE_DIR):
        for file in files:
            if file.endswith('.po'):
                po_files_found = True
                po_file = os.path.join(root, file)
                try:
                    compile_po_to_mo(po_file)
                except Exception as e:
                    print(f"✗ Error compiling {po_file}: {e}")
    
    if po_files_found:
        print("\n✓ Translation compilation completed!")
    else:
        print("No .po files found in locale directory")
        
except ImportError:
    print("polib not installed. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "polib"])
    print("Retrying...")
    os.execv(sys.executable, [sys.executable] + sys.argv)
