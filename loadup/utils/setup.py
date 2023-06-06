import winreg
import sys
import os
import subprocess

class ClientSetup:
    def init(self):
        current_path = os.path.abspath(sys.argv[0])
        drive = os.path.splitdrive(current_path)[0]
        bat_content = '''
        @echo off
        :check
        if exist F:\ (goto true) else (goto check)

        :true
        F:
        cd loadup
        cd wake
        start set.bat
        goto end

        :end
        exit
        '''
        bat_file_path = rf'{drive}\A.D.A\A.D.A\loadup\utils\invoker.bat'
        self.write_bat_file(bat_file_path, bat_content)
        self.ask_to_run(bat_file_path)
        self.add_to_startup(bat_file_path)

    def write_bat_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    def ask_to_run(self, file_path):
        response = input("Do you want to start the bat file now? (Y/N): ")
        if response.upper() == 'Y':
            self.run_file(file_path)
        else:
            self.exit()

    def run_file(self, file_path):
        try:
            subprocess.run(file_path, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the file: {e}")
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")

    def add_to_startup(self, file_path):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "ADA Invoker", 0, winreg.REG_SZ, file_path)
        winreg.CloseKey(key)

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    cs = ClientSetup()