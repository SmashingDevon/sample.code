import requests
import json
import csv
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from data import constants

def create_stock_json_record():

    #Setting up browser in headless mode.
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    print("Headless Firefox Running...")

    #Navigating to the page via URL from constants, maximize the window to ensure all elements visible.
    #Gives the implicit wait of five seconds in case of any lag on the page.
    driver.get(constants.stock_idx['item']['url'])
    driver.maximize_window()
    driver.implicitly_wait(5)

    #Submitting the stock symbol from the constants.
    stock_input = driver.find_element_by_xpath("""//*[@id="stock-search-text"]""")
    stock_symbol = constants.stock_idx['item']['symbol']
    stock_input.send_keys(stock_symbol)
    submit = driver.find_element_by_xpath("""//*[@id="stock-search-submit"]""").click()

    #Checking for something that should be present, then scraping the values I want.
    elems = driver.find_element_by_xpath("""/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]""").text
    if len(elems) > 0 :
        pc = driver.find_element_by_xpath("""//*[@id="quotes_content_left__PreviousClose"]""").text
        vol = driver.find_element_by_xpath("""//*[@id="quotes_content_left__Volume"]""").text

        driver.close()

    #Putting data into dict and printing for developer to see in terminal.
        data = {'previous_close': pc, 'volume': vol}
        print(data)

    return json.dumps(data)
