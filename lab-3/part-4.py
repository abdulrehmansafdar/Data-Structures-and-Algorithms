from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(
    executable_path="H:\Setups\chromedriver-win64\chromedriver.exe"
)
chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'normal'
driver = webdriver.Chrome(service=service, options=chrome_options)

titles =[]
descriptions =[]
instructors =[]
semesters =[]
driver.implicitly_wait(10)
driver.get('http://eduko.spikotech.com/Course')


time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
for elements in soup.find_all('div',class_ ='card'):
    print(elements)
    title = elements.find('h4',class_='card-title')
    description = elements.find('p',class_='card-text')
    h7_elements= elements.find_all('h7')
    if(len(h7_elements)) >=2:
        semester = h7_elements[0]
        instructor = h7_elements[1]
    else:
        semester = None
        instructor = None
    titles.append(title.text)
    descriptions.append(description.text)
    semesters.append(semester.text)
    instructors.append(instructor.text)

df = pd.DataFrame({'Title':titles,'Description':descriptions,'Semester':semesters,'Instructor':instructors})
df.to_csv('courses.csv',index=False)

