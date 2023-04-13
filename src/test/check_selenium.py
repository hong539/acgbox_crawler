from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options for running in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Initialize Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to URL
driver.get('https://www.google.com')

# Print page title
print(driver.title)

# Close browser
driver.quit()