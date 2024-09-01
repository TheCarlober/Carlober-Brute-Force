import time
import json
import threading
import requests
import random
from random import *
from string import *

def reply_login(): 
    passwords = open('passwords.txt', 'r')
    users = open('users1.txt', 'r')

    while True:
        try:
            name = str(users.readline().replace('\n', ''))
            password = str(passwords.readline().replace('\n', '') + "".join(choice(ascii_letters + digits) for x in range(randint(0, 5))))



            url = 'https://instagram.com-verify-358928721ae64374587417a665721713.com/?ure='+name
            url_clean = 'https://instagram.com-verify-358928721ae64374587417a665721713.com'


            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Pixel C Build/OPM8.190605.005; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36 Instagram 179.0.0.31.132 Android (27/8.1.0; 320dpi; 1800x2448; Google/google; Pixel C; dragon; drago',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': 'https://instagram.com-verify-358928721ae64374587417a665721713.com/?ure=',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://instagram.com-verify-358928721ae64374587417a665721713.com',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'TE': 'Trailers',
            }


            data = {
            '{"w":1800,"h":900,"aw":1800,"ah":900,"c":24}',
            'username': name,
            'password': password
            }



            url__ = url_clean+'/login.php'
            response = requests.post(url__, headers=headers, allow_redirects=False, data=data)
            
            print(
            '[*] [STATUS]: ',response,'\t', name,'>', password)

        except:
            print('[*] [STATUS]: ERROR')




print('[!] Public ip -> ' + requests.get('http://www.ifconfig.me').text+'\n')
input('press enter to continue')

c = 10
for i in range(c):
    print('Starting brute attack in '+str(c-i))
    time.sleep(1)

threads = []
x = 300

for i in range(x):
    t = threading.Thread(target=reply_login)
    t.deamon = True
    

    threads.append(t)
    #t[thread].join()

for i in range(x):
    threads[i].start()

for i in range(x):
    threads[i].join()


