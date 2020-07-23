from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
from matplotlib import pyplot as plt
import time

"""
code by Christoph Mittermaier

github.com/chrisimi
"""

# set the path to the driver of your browser
PATH = "C:\Program Files (x86)\chromedriver.exe"

# set the driver and the browser with the PATH to it
driver = webdriver.Chrome(PATH)

driver.get("https://cookiesclicker.net/guest/")

# wait some time before starting
time.sleep(5)

# get mostly used web elements
cookie = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]")
cookie_display = driver.find_element_by_xpath("//*[@id='CookiesBaked']")
cookies_needed = driver.find_elements_by_xpath("//*[@id='cps']")

# check if bot has enough cookies to buy an upgrade
def check_for_buttons():
    cursor_needed = int(driver.find_element_by_xpath("//*[@id='cursorBuyCount']").text)
    baker_needed = int(driver.find_element_by_xpath("//*[@id='BakerBuyCount']").text)
    cookie_shop_needed = int(driver.find_element_by_xpath("//*[@id='CookieShopBuyCount']").text)
    trucks_needed = int(driver.find_element_by_xpath("//*[@id='TrucksBuyCount']").text)
    cookie_yard_needed = int(driver.find_element_by_xpath("//*[@id='CookieYardBuyCount']").text)

    if cookies > cursor_needed:
        driver.find_element_by_xpath("//*[@id='tileonecontent']").click()
    elif cookies > baker_needed:
        driver.find_element_by_xpath("//*[@id='tiletwo']").click()
    elif cookies > cookie_shop_needed:
        driver.find_element_by_xpath("//*[@id='tilethree']").click()
    elif cookies > trucks_needed:
        driver.find_element_by_xpath("//*[@id='tilefour']").click()
    elif cookies > cookie_yard_needed:
        driver.find_element_by_xpath("//*[@id='tilefive']").click()

# define variables for graph

index = 0
second = 0
x = [0]
y = [0]

try:
    while True:
        index = index + 1
        cookie.click()
        cookies = int(cookie_display.text.split(' ')[0])
        print(cookies)
        time.sleep(0.1)
        check_for_buttons()
        if index >= 10:
            second = second + 1
            x = np.append(x, second)
            y = np.append(y, cookies)
            index = 0
except:
    driver.quit()

# create graph and save it under 'graph.png'
    plt.plot(x, y)
    plt.xlabel("time in seconds")
    plt.ylabel("cookies")
    plt.title("cookies on time")
    plt.show()
    plt.savefig('graph.png')
