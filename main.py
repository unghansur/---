from selenium import webdriver
import time

from selenium.common import ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()
browser.get('https://sbis.ru/')


def clck_bttn():
    click_button = (browser.find_element(By.XPATH,
                                         value='//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div['
                                               '2]/ul/li[3]/a'))
    click_button.click()
    print(f'Currently URL is: {browser.current_url}')
    time.sleep(2)


def clck_bttn2():
    click_button2 = (browser.find_element(By.XPATH, value='//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img'))
    click_button2.click()
    print(f'Currently URL is: {browser.current_url}')
    time.sleep(2)


browser.switch_to.window(browser.window_handles[-1])


def title():
    WebDriverWait(browser, 10).until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')))
    time.sleep(5)


def about():
    browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a').send_keys(Keys.ENTER)
    print(f'Currently URL is: {browser.current_url}')
    time.sleep(5)


browser.switch_to.window(browser.window_handles[-1])


def image1():
    image_1 = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/div')
    try:
        size = image_1.size
        print(size)
        width = size['width']
        height = size['height']
        print(f'Width : {width}')
        print(f'Height : {height}')
    except ElementNotInteractableException:
        print('image could be hidden')


def image2():
    image_2 = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/div')
    try:
        size = image_2.size
        print(size)
        width = size['width']
        height = size['height']
        print(f'Width : {width}')
        print(f'Height : {height}')
    except ElementNotInteractableException:
        print('image could be hidden')


def image3():
    image_3 = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/div')
    try:
        size = image_3.size
        print(size)
        width = size['width']
        height = size['height']
        print(f'Width : {width}')
        print(f'Height : {height}')
    except ElementNotInteractableException:
        print('image could be hidden')


def image4():
    image_4 = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/div')
    try:
        size = image_4.size
        print(size)
        width = size['width']
        height = size['height']
        print(f'Width : {width}')
        print(f'Height : {height}')
    except ElementNotInteractableException:
        print('image could be hidden')
