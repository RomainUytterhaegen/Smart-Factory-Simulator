from cx_Freeze import setup, Executable

setup(name="SmartUsine", version="0.1", description="La première version pour tester la compilation",
      executables=[Executable("main.py", base="Win32GUI")])
