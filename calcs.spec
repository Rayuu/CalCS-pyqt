# -*- mode: python -*-

block_cipher = None


a = Analysis(['calcs.py'],
             pathex=['C:\\Users\\jx007\\Desktop\\PyQt_Calcs'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='calcs',
          debug=False,
          strip=False,
          upx=True,
          console=False,icon='833.ico')
