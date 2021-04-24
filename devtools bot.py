from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager# Initiate the browser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser  = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

# Open the Website
input("open into a game, then press enter to start")


# Bad code that does things
while (True):
    question = browser.find_element_by_xpath("//*[@id=\"livemathletics\"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div").text

    question = question.replace(" =", "")
    question = question.split(" + ")
    answer = int(question[0]) + int(question[1])

    browser.find_element_by_xpath("//*[@id=\"livemathletics\"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div/input").send_keys(answer)
    time.sleep(.001)
    browser.find_element_by_xpath("//*[@id=\"livemathletics\"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div/input").send_keys(Keys.ENTER)
    time.sleep(.001)