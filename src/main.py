# import concurrent.futures
# from concurrent.futures import as_completed
from time import sleep
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
# from datetime import datetime
from sqlalchemy import create_engine
# import psutil

# target_url = "https://home.gamer.com.tw/acgbox.php?page=1&owner=username&tab=&m="
                
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',}

ACG_tag_list = ['Android', 'iOS', 'PC線上', 'PC單機', 'WEB', 'PS5', 'PS4', 'XboxSX', 'Switch', '動畫', '漫畫', '輕小說']

def show_pid():
        pid = os.getpid()
        return pid

def modfy_data():
        engine_url = "mysql+pymysql://user:passwd@host:3306/gamer_crawler"
        engine = create_engine(engine_url, echo=True)
        loads = pd.read_sql('acg_collections', engine)
        ss = loads.query('ACG_name.str.contains("動畫")')
        # print(ss)
        gg = ss['ACG_name'].str.replace("動畫", "")
        # print(gg)

        df_acg = pd.DataFrame(columns=['Anime_name'])
        df_acg['Anime_name'] = gg
        print(df_acg)
        df_acg.to_sql('anime_favorites', engine, if_exists='append', index=False)

def parser_ACG_tag_list(src_url):
        
        r = requests.get(src_url, headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        p = soup.find_all(class_="BA-menu")
        # ps = soup.select("body > div.BA-topbg > div > ul > li > a")
        # print(ps)        

        # print(p)        
        catch_text = []
        for item in p:
                target = item.find_all('a')
                # print(target)
                if target != []:
                        for x in range(len(target) - 1):
                                target_text = target[x].text
                                catch_text.append(target_text)
                
        print(catch_text)


def parser(number, username):
        sleep(3)
        target_url = "https://home.gamer.com.tw/acgbox.php?page=" + str(number) + "&owner=" + str(username) + "&tab=&m="
        # print(target_url)
        
        r = requests.get(target_url, headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        p = soup.find_all(class_="acgboxname")
        
        catch_text = []

        for item in p:
                s = item.select_one('a').text
                catch_text.append(s)
                
        
        # print(catch_text)
        df_acg = pd.DataFrame(columns=['ACG_name'])

        df_acg['ACG_name'] = catch_text

        print(df_acg)

        # engine_url = "mysql+pymysql://user:passwd@host:3306/gamer_crawler"
        # engine = create_engine(engine_url, echo=True)
        # df_acg.to_sql('acg_collections', engine, if_exists='append', index=False)

if __name__ == "__main__":               
        for x in range(1, 2):
                parser(x, "username")
        # parser_ACG_tag_list("https://www.gamer.com.tw/")
        # modfy_data()