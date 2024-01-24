# -*- mode: python ; coding: utf-8 -*-

import os
import tempfile
import subprocess

TEMPLATE_PARAMETER: str = "%code%"

template = None
with open('banana.py', 'r', encoding='utf8') as file:
    template = file.read()

completed_process = subprocess.run(["python", "encryption_zip.py"], capture_output=True, text=True)
data = template.replace(TEMPLATE_PARAMETER, completed_process.stdout)

fp = tempfile.NamedTemporaryFile(delete=False)
fp.write(bytes(data, 'utf-8'))
filename = fp.name
print(filename)
fp.close()

a = Analysis(
    [filename],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='test2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="program.ico",
)