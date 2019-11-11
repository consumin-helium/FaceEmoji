# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
block_cipher = None

added_files = [
         ( 'assets/opend.png', '.'),
         ( 'assets/haarcascade_frontalface_default.xml', '.'),
         ( 'Logo.ico', '.'),
         ]

a = Analysis(['main.py'],
             pathex=['D:\\Alexander\\NewDesktopApp\\desktop_programs'],
             binaries=[],
             datas = added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='EmojiFace',
          icon='Logo.ico',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
