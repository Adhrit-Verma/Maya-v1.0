import winreg
import sys
import os

def add_to_startup():
    script_path = os.path.abspath(sys.argv[0])
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "MyScript", 0, winreg.REG_SZ, script_path)
    winreg.CloseKey(key)

if __name__ == "__main__":
    add_to_startup()