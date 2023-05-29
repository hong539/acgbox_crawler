import pandas as pd

def load_html_table(url:str):    
    print("Please input your url to parse html table:")
    # dfs = pd.read_html(url, match="customers" ,flavor='lxml')
    dfs = pd.read_html(url, flavor='lxml')
    return dfs

if __name__ == "__main__":    
    load_html_table()