from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
from bs4 import BeautifulSoup

# Set up Selenium
service = Service('chromedriver.exe')  # Path to your ChromeDriver executable
# options = Options()
# options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service)

# Navigate to a specific page
page_url = "https://leetcode.com/problemset/all/?page=";

def get_a_tags(url):
    driver.get(url)
    time.sleep(7);
    links = driver.find_elements(By.TAG_NAME,"a")
    print(links)
    ans = []
    pattern = "/problems"
    for i in links:
        try:    #Exception handling
            if pattern in i.get_attribute("href"):
                ans.append(i.get_attribute("href"))
        except:
            pass
    ans = list(set(ans)); #removing duplicates
    return ans ;

my_ans = []

for i in range(1,55):
    my_ans+=(get_a_tags(page_url+str(i)))

my_ans = list(set(my_ans))

with open('lc.txt','a') as f:
    for j in my_ans:
        f.write(j+'\n')

print(len(my_ans))

driver.quit()