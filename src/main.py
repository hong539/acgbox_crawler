import yaml
from time import sleep
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
                
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',}
# ACG_tag_list = ['Android', 'iOS', 'PC線上', 'PC單機', 'WEB', 'PS5', 'PS4', 'XboxSX', 'Switch', '動畫', '漫畫', '輕小說']

def load_config():
        with open("../my_self.yaml", "r") as config:
                data = yaml.safe_load(config)
        print(data["seed"]["url"])
        print(data["target"]["username"])
        print(data["target"]["number"])

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

def parser(number, username):
        sleep(3)
        target_url = seed_url + str(number) + "&owner=" + str(username) + "&tab=&m="
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
        load_config()
        # for x in range(1, 2):
        #         parser(x, "username")
        # modfy_data()