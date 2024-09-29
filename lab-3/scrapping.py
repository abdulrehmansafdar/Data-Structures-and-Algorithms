from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# initialize the driver
service = Service(
    executable_path="H:\Setups\chromedriver-win64\chromedriver.exe"
)
chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'normal'
driver = webdriver.Chrome(service=service, options=chrome_options)

product_list =[]
price_list = []
currency_list = []
discount_list = []
comments_list = []

# open the url
driver.get('https://www.daraz.pk/#hp-just-for-you')

driver.implicitly_wait(10)
for _ in range(3):
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#js_jfy > div.hp-mod-card-content > div.jfy-card-load-more > div'))  # Replace with the actual selector
        )
        load_more_button.click()
        # Wait for the new content to load
        # #js_jfy > div.hp-mod-card-content > div.jfy-card-load-more > div
        driver.implicitly_wait(10)
    except Exception as e:
        print(f"Error clicking load more button: {e}")
        break

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

# find the div with the class name 'card-info.gallery-card-layout-info'
for elements in soup.find_all('div', class_='card-jfy-item-desc'):
    print(elements)
    product = elements.find('div', class_='card-jfy-title')
    currency = elements.find('span', class_='currency')
    price = elements.find('span', class_='price')
    discount = elements.find('span', class_='hp-mod-discount')
    comments = elements.find('span', class_='card-jfy-ratings-comment')
    # if no discount is available, set it to 0 and if no comments are available, set it to 0 as well otherwise get the text and append it to the list
    discount = 0 if discount is None else discount.text
    comments = 0 if comments is None else comments.text
    product_list.append(product.text)
    currency_list.append(currency.text)
    price_list.append(price.text)
    discount_list.append(discount)
    comments_list.append(comments)

# write the data to a csv file with pandas and aslo columns name
df = pd.DataFrame({'Product': product_list, 'Currency': currency_list, 'Price': price_list, 'Discount': discount_list, 'Comments': comments_list})
df.to_csv('daraz_products.csv', index=False)

       
    



    

