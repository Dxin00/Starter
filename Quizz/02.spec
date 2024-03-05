# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['02.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Sunrise_LAPTOP\\Desktop\\PROJECT CODE\\Repository\\Starter\\Starter\\module 2\\man1.wav', '.'), ('C:\\Users\\Sunrise_LAPTOP\\Desktop\\PROJECT CODE\\Repository\\Starter\\Starter\\module 2\\pirate3.jpg', '.'), ('C:\\Users\\Sunrise_LAPTOP\\Desktop\\PROJECT CODE\\Repository\\Starter\\Starter\\module 2\\wom1.wav', '.'), ('C:\\Users\\Sunrise_LAPTOP\\Desktop\\PROJECT CODE\\Repository\\Starter\\Starter\\module 2\\yes1.jpg', '.')],
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
    name='02',
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
)
