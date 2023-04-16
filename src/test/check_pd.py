import requests
from bs4 import BeautifulSoup
import pandas as pd

def parser(number, username):
    target_url = "https://home.gamer.com.tw/acgbox.php?page=" + str(number) + "&owner=" + str(username) + "&tab=&m="

    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

    r = requests.get(target_url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')

    print(type(soup))

    print(type(str(soup)))

    # check_table = pd.read_html(str(soup), flavor='lxml', attrs={'class': 'acgbox'})

    # print(check_table)

if __name__ == "__main__":
    parser(1, "username")    