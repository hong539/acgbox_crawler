#使用pyyaml可以讀取yaml格式的檔案，然後使用sqlalchemy的text()方法嵌入SQL語句。
#我們使用yaml.load()方法讀取example.yaml檔案，然後建立一個sqlalchemy的engine物件連接到資料庫。
# 接下來，我們可以使用text()方法嵌入從yaml檔案中讀取的SQL語句，並使用engine.connect()方法執行SQL查詢。
import yaml
from sqlalchemy import create_engine, text

with open("example.yaml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

# connect to the database
engine = create_engine(data["db_uri"])

# execute the SQL statement
with engine.connect() as connection:
    connection.execute(text(data["sql"]))
    connection.commit()