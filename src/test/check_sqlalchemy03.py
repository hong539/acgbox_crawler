from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

# 建立數據庫連接
engine = create_engine('mysql://username:password@host:port/')

# 創建一個新的使用者
with engine.connect() as con:
    con.execute(text("CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password'"))

# 創建一個新的數據庫
with engine.connect() as con:
    con.execute(text("CREATE DATABASE newdatabase"))

# 為使用者分配數據庫權限
with engine.connect() as con:
    con.execute(text("GRANT ALL PRIVILEGES ON newdatabase.* TO 'newuser'@'localhost'"))

# 測試新用戶的數據庫連接
new_engine = create_engine('mysql://newuser:password@host:port/newdatabase')
Session = sessionmaker(bind=new_engine)
session = Session()

# 確認新用戶的數據庫連接正常
result = session.execute("SELECT 1")
print(result.fetchone())