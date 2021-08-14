import sys
from cx_Freeze import setup,Executable
import os
PYTHON_INSTALL_DIR=os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')

include_files=[(os.path.join(PYTHON_INSTALL_DIR,'DLLs','tk86t.dll'),os.path.join('lib','tk86.dll')),
(os.path.join(PYTHON_INSTALL_DIR,'DLLs','tcl86t.dll'),os.path.join('lib','tcl86.dll'))]
base=None

if sys.platform=='win32':
    base='Win32GUI'

executables=[Executable('signin_database.py',base=base,icon=r"E:\Python Project\Student management System\icon.ico",shortcutName='Student Management System',shortcutDir='DesktopFolder')]

setup(name='Student Management System Installer',
version='1.0.1',
author='Santanu Saha',
description="This is a Student Management System Software",
options={'build_exe':{'include_files':include_files}},
executables=executables)