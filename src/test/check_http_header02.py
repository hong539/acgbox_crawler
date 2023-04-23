from user_agent import generate_user_agent
chrome_ua = generate_user_agent(navigator='chrome')
firefox_ua = generate_user_agent(navigator='firefox')
# edge_ua = generate_user_agent(navigator='edge')

print(chrome_ua)
print(firefox_ua)