from fake_useragent import UserAgent
ua = UserAgent()
chrome_ua = ua.chrome
firefox_ua = ua.firefox
edge_ua = ua.edge

print(chrome_ua)
print(firefox_ua)
print(edge_ua)