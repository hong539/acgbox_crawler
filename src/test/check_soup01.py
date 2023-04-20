import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',}

def parser_ACG_tag_list(src_url):
        
        r = requests.get(src_url, headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        p = soup.find_all(class_="BA-menu")
        # ps = soup.select("body > div.BA-topbg > div > ul > li > a")
        # print(ps)        

        # print(p)        
        catch_text = []
        for item in p:
                target = item.find_all('a')
                # print(target)
                if target != []:
                        for x in range(len(target) - 1):
                                target_text = target[x].text
                                catch_text.append(target_text)
                
        print(catch_text)

if __name__ == "__main__":
        parser_ACG_tag_list("https://www.gamer.com.tw/")