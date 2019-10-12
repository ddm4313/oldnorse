import requests, pyfiglet, random
from bs4 import BeautifulSoup
from colorama import Fore

def get_norse_name():
    norse_site = requests.get(f"https://babynames.net/all/old-norse?page={random.randint(1, 9)}")
    soup = BeautifulSoup(norse_site.text, features="lxml")
    norse_names = soup.findAll("span", attrs={"class": "result-name"})

    norse_list = []
    for name in norse_names:
        norse_list.append(name.text)
    return random.choice(norse_list)
