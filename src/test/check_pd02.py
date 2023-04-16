import pandas as pd

url = 'https://www.w3schools.com/html/html_tables.asp'
# dfs = pd.read_html(url, match="customers" ,flavor='lxml')
dfs = pd.read_html(url, flavor='lxml')
print(dfs)