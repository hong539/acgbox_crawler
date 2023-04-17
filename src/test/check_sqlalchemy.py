import yaml
from sqlalchemy import create_engine

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

engine = create_engine(f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8mb4")
