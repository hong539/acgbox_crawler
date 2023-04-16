import requests
from bs4 import BeautifulSoup
import pandas as pd

def parser(number, username):
    target_url = "https://home.gamer.com.tw/acgbox.php?page=" + str(number) + "&owner=" + str(username) + "&tab=&m="

    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

    r = requests.get(target_url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup)
    # print(type(soup))
    # print(type(str(soup)))    
    
    p = soup.find_all(class_="acgboxname")
    
    print(p)
    # print(type(p))
    
    # content = []
    # for name in p:
    #     content.append(p.text)

    # print(content)
    # check_table = pd.read_html(str(soup), match=False, flavor='lxml', attrs={'class': 'acgboxname'})
    # print(check_table)

if __name__ == "__main__":
    #please replace username to test
    parser(1, "username")    