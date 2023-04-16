import requests
from bs4 import BeautifulSoup
import pandas as pd

def parser(number, username):
    target_url = "https://home.gamer.com.tw/acgbox.php?page=" + str(number) + "&owner=" + str(username) + "&tab=&m="

    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

    r = requests.get(target_url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    #pandas.read_html() 是設計來解析 HTML 中的表格標籤 (<table>) 的內容的，如果 HTML 內容不是表格標籤或是表格內容沒有被包在 <table> 標籤中，就不能直接使用 pandas.read_html()。
    # 如果你想要解析 HTML 中的其他元素，比如 <div>，你可以先使用 BeautifulSoup 或是其他 HTML 解析器，然後再提取出需要的內容，再將其轉換成 pandas.DataFrame。
    check_table = pd.read_html(str(soup), flavor='lxml', attrs={'class': 'acgboxname'})
    print(check_table)

if __name__ == "__main__":
    #please replace username to test
    parser(1, "username")
    