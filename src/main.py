import yaml
from time import sleep
import os
import fake_useragent
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

#For simple test                
# HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',}

class acgbox_crawler(object):
        """docstring for ClassName."""
        def __init__(self, path):
            self.path = path

        def load_config(self):
                with open(self.path, "r") as config:
                        self.data = yaml.safe_load(config)

        def db_init(self):
                pass
        
        def parser(self):
                pass

        def modfy_data(self):
                pass
      
      
def load_config(path):
        """Load configuration data from a YAML file.

        Args:
        path (str): The path to the YAML configuration file.

        Returns:
        dict: The configuration data.
        """         
        with open(path, "r") as config:
                data = yaml.safe_load(config)
        #Check which type is data?
        print(type(data))
        #Check seed/url
        print(data["seed"]["url"])
        #Check target username & number
        print(data["target"]["username"])
        print(data["target"]["number"])
        #Check db_settingup detials
        # print(data["db_settingup"]["db_admin"])
        return data

def db_init(data):
        engine = create_engine(data["db_settingup"]["db_admin"])
        
        with engine.connect() as connection:
                connection.execute(text(data["db_settingup"]["sql_init_user"]))
                connection.execute(text(data["db_settingup"]["sql_init_database"]))
                connection.execute(text(data["db_settingup"]["sql_init_user_privileges"]))
                connection.execute(text(data["db_settingup"]["sql_flush_privileges"]))
                connection.commit()
                connection.close()

def show_pid():
        pid = os.getpid()
        return pid

def modfy_data():
        # ACG_tag_list = ['Android', 'iOS', 'PC線上', 'PC單機', 'WEB', 'PS5', 'PS4', 'XboxSX', 'Switch', '動畫', '漫畫', '輕小說']
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
        df_acg.to_sql('anime_favorites', engine, if_exists='replace', index=False)

def check_headers():
        # ua = UserAgent(browsers=['edge', 'chrome'])
        # ua = UserAgent(use_external_data=True)
        ua = fake_useragent.UserAgent(fallback='chrome')
        ua.random == 'chrome'
        print(ua.random)

def parser(data):
        sleep(3)
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',}
        print(HEADERS)
        target_url = data["seed"]["url"] + str(data["target"]["number"]) + "&owner=" + str(data["target"]["username"]) + "&tab=&m="
        print(target_url)
        
        # r = requests.get(target_url, headers={'user-agent': ua.random})
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

        #src:https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine
        # engine_url = "mysql+pymysql://user:passwd@host:3306/gamer_crawler"
        # engine = create_engine(engine_url, echo=True)
        # old one
        # sqlalchemy engine_url password duplicate@ cause str passe_error
        engine_url = data["db_settingup"]["sql_check_database"]
        #check engine_url
        print(engine_url)
        engine = create_engine(engine_url, echo=True)
        # test this way
        # engine = create_engine(f"mysql+pymysql://{data['db_settingup']['user']}:{data['db_settingup']['password']}@{data['db_settingup']['host']}:{data['db_settingup']['port']}/{data['db_settingup']['db_name']}?charset=utf8mb4")
        # metadata = MetaData()
        # users_table = Table('acg_collections', metadata, autoload=True, autoload_with=engine)        
        #src:https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html?highlight=to_sql#pandas.DataFrame.to_sql
        df_acg.to_sql(name='acg_collections', con=engine, if_exists='append', index=False)

if __name__ == "__main__":
        # check_headers()
        data = load_config("../my_self.yaml")
        #When 1st time db_settingup
        # db_init(data)
        #You should be careful when using range() in for loop!
        #Where to stat and where to stop?
        for data["target"]["number"] in range(1, data["target"]["number"]+1):
                parser(data)
        # modfy_data()