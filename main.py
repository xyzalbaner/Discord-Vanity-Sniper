# Project made for Free2use
# dev: bhop3
# join discord.gg/xyzshop for more :)

import tls_client, requests
from threading import Thread
import threading
from itertools import cycle
import random
import easygui
import os
from colorama import Fore
from datetime import datetime
import ctypes
import time
from pystyle import *

class xyzVanity:
    def __init__(self):
        self.time = datetime.today().strftime('%H:%M:%S')
        os.system("mode 80, 18")
        self.clear()
        self.setTitle("xyzVanitySniper Tool → discord.gg/xyzshop → dev: bhop3")
        self.banner()

        useproxy =  Write.Input(f'          {self.time} Use Proxies? (y/n): ', Colors.cyan_to_green, interval=0.03).lower()

        if useproxy == "y":
            Write.Print("                    ~ Using Proxy", Colors.cyan_to_green, interval=0.03)
            proxy = self.get_proxy_list()
            self.clear()
            self.banner()

            self.session = tls_client.Session(client_identifier = "chrome_120", random_tls_extension_order=True)

            self.session.proxies = {
                "http": proxy,
                "https": proxy
            }
        else:
            Write.Print("                    ~ Using Proxyless", Colors.cyan_to_green, interval=0.03)
            self.clear()
            self.banner()
            self.session = tls_client.Session(client_identifier = "chrome_120", random_tls_extension_order=True)


        vanity = Write.Input(f'                  {self.time} (Vanity) → ', Colors.cyan_to_green, interval=0.03)
        guild = Write.Input(f'                  {self.time} (Guild) → ', Colors.cyan_to_green, interval=0.03)
        delay = float(Write.Input(f'                  {self.time} (Delay) → ', Colors.cyan_to_green, interval=0.03))
        token = Write.Input(f'{self.time} (Token) → ', Colors.cyan_to_green, interval=0.03)

        ts = [threading.Thread(target=self.xyzeasy,args=[token,guild,vanity,delay])]
        for t in ts:
            t.start()
        for t in ts:
            t.join()
    

    def banner(self):
        banner = f'''
               ┓┏    •   ┏┓  •      
          ┓┏┓┏┓┃┃┏┓┏┓┓╋┓┏┗┓┏┓┓┏┓┏┓┏┓
          ┛┗┗┫┗┗┛┗┻┛┗┗┗┗┫┗┛┛┗┗┣┛┗ ┛ 
             ┛          ┛     ┛           
       discord.gg/xyzshop - dev: bhop3                         
        '''
        print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter(banner, 15)))
    
    def clear(self):
        os.system("cls")
    
    def setTitle(self, _str):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")

    def get_proxy_list(self):
        useproxy = Write.Input(f'\n          {self.time} (y) Own Proxies or (n) Generate some ', Colors.cyan_to_green, interval=0.03).lower()

        if useproxy == "y":
            proxylist = easygui.fileopenbox(msg="Choose your Proxy List", title="Proxy List Opener", filetypes=".txt")
            proxies = open(proxylist, "r", encoding="utf-8").read().splitlines()
            return "http://" + random.choice(proxies) or "https://" + random.choice(proxies)

        else:
            try:
                api = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=ipport&format=text"
                proxies = requests.get(api).text.splitlines()
                return "http://" + cycle(proxies) or "https://" + cycle(proxies)
            except:
                pass
    
    def get_headers(self, token):
        headers = {
            "authorization": token,
            "content-type": "application/json"
        }
        return headers
    
    @staticmethod
    def check_status(status_code: int):
        status_messages = {
            200: "Success",
            201: "Success",
            204: "Success",
            400: "Detected Captcha",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method not allowed",
            429: "Too many Requests"
        }
        return status_messages.get(status_code, "Unknown Status")

    def xyzeasy(self, token, guildid, vanity, delay):
        self.clear()
        self.banner()
        headerz = self.get_headers(token)
        tk = token[:32] + "*" * 3

        while True:
            try:
                r = self.session.get(f"https://discord.com/api/v9/invites/{vanity}?with_counts=true&with_expiration=true", headers=headerz)
                if r.status_code == 200:
                    print(Colorate.Horizontal(Colors.cyan_to_green, f'                    [Vanity Taken] ({self.check_status(r.status_code)}) → {tk} [{vanity}]'))
                    time.sleep(delay)
                else:
                    print(Colorate.Vertical(Colors.cyan_to_green, f'                    [Vanity Free] ({self.check_status(r.status_code)}) → {tk}'))
                    r = self.session.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", json={"code": vanity}, headers=headerz)
                    if r.status_code == 200:
                        print(Colorate.Horizontal(Colors.cyan_to_green, f'                    [Claimed] ({self.check_status(r.status_code)}) → {tk} [{vanity}]'))
                        break
                    else:
                        print(Colorate.Vertical(Colors.red_to_purple, f'                    [Vanity] ({self.check_status(r.status_code)}) → {tk}'))
                        time.sleep(delay)
            except Exception as e:
                print(Colorate.Vertical(Colors.red_to_purple, f'                    [Error] {e}'))
                return False

xyzVanity()
input("")