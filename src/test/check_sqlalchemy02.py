from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()

engine = create_engine('mysql://root:password@localhost')
conn = engine.connect()

#需要注意的是，範例程式碼中的'password'需要替換為實際使用的密碼，而且這種方法存在資安風險，
#建議只在開發和測試環境中使用。在生產環境中應該使用更安全的方式設置資料庫連接。
# 創建新的使用者
conn.execute("CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password'")

# 創建新的DB
conn.execute("CREATE DATABASE new_db")

# 賦予新使用者對新DB的權限
conn.execute("GRANT ALL PRIVILEGES ON new_db.* TO 'new_user'@'localhost'")

# 刷新權限設定
conn.execute("FLUSH PRIVILEGES")

# 關閉連線
conn.close()