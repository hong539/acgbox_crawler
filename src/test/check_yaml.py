import yaml

# 讀取YAML檔案
with open("example.yaml", "r") as file:
    data = yaml.safe_load(file)

# 使用讀取到的資料
print(data["name"])
print(data["age"])