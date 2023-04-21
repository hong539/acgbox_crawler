import yaml
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

engine = create_engine(f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8mb4")
metadata = MetaData()
users_table = Table('users', metadata, autoload=True, autoload_with=engine)

result = engine.execute(users_table.select())
for row in result:
    print(row)