from selenium import webdriver
from selenium.webdriver.common.by import By
from mysql.connector import MySQLConnection, Error
import time
import getpass
driver = webdriver.Firefox()
all_movies = []
site = driver.get("https://www.kinopoisk.ru/lists/movies/top250/")

driver.implicitly_wait(0.5)
def find_text():
    text_box = driver.find_elements(By.CLASS_NAME, 'desktop-list-main-info_mainTitle__8IBrD')
    for data in text_box:
        all_movies.append(data.text)

def click_button(num):
    button = driver.find_element(By.LINK_TEXT, f'{num}')
    button.click()
time.sleep(10)
find_text()
click_button(2)
find_text()
click_button(3)
find_text()
click_button(4)
find_text()
click_button(5)
find_text()
for film in all_movies:
    print(film)

try:
    with MySQLConnection(
        host='localhost',
        user='root',
        password=getpass.getpass(),
        database='movies'
    ) as connection:
        for film in all_movies:
            query = "INSERT INTO films(name) VALUE ('{}')".format(film)
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                connection.commit()
except Error as e:
    print(e)
