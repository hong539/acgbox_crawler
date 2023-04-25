import yaml
from time import sleep
import os
from fake_useragent import UserAgent
import fake_useragent
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy import Table, MetaData


class Crawler:
    def __init__(self):
        self.data = None
        self.engine_url = None

    def load_config(self, path):
        with open(path, "r") as config:
            self.data = yaml.safe_load(config)

        print(type(self.data))
        print(self.data["seed"]["url"])
        print(self.data["target"]["username"])
        print(self.data["target"]["number"])

        return self.data

    def db_init(self):
        engine = create_engine(self.data["db_settingup"]["db_admin"])

        with engine.connect() as connection:
            connection.execute(text(self.data["db_settingup"]["sql_init_user"]))
            connection.execute(text(self.data["db_settingup"]["sql_init_database"]))
            connection.execute(text(self.data["db_settingup"]["sql_init_user_privileges"]))
            connection.execute(text(self.data["db_settingup"]["sql_flush_privileges"]))
            connection.commit()

        connection.close()

    @staticmethod
    def show_pid():
        pid = os.getpid()
        return pid

    def modfy_data(self):
        self.engine_url = f"mysql+pymysql://{self.data['db_settingup']['user']}:{self.data['db_settingup']['password']}@{self.data['db_settingup']['host']}:{self.data['db_settingup']['port']}/{self.data['db_settingup']['db_name']}?charset=utf8mb4"

        engine = create_engine(self.engine_url, echo=True)
        loads = pd.read_sql('acg_collections', engine)
        ss = loads.query('ACG_name.str.contains("動畫")')
        gg = ss['ACG_name'].str.replace("動畫", "")
        df_acg = pd.DataFrame(columns=['Anime_name'])
        df_acg['Anime_name'] = gg
        print(df_acg)
        df_acg.to_sql('anime_favorites', engine, if_exists='replace', index=False)

    @staticmethod
    def check_headers():
        ua = fake_useragent.UserAgent(fallback='chrome')
        ua.random == 'chrome'
        print(ua.random)

    def parser(self):
        sleep(3)
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',}
        print(HEADERS)
        target_url = self.data["seed"]["url"] + str(self.data["target"]["number"]) + "&owner=" + str(self.data["target"]["username"]) + "&tab=&m="
        print(target_url)

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
        
        engine_url = self.data["db_settingup"]["sql_check_database"]
        print(engine_url)
        engine = create_engine(engine_url, echo=True)
        df_acg.to_sql(name='acg_collections', con=engine, if_exists='append', index=False)

if __name__ == "__main__":
    test = Crawler()
    test.load_config(path)       