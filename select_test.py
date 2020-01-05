from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"

try:
    browser.get(link)
    time.sleep(2)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    result = int(num1) + int(num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text('%s' % result)

    submit_btn = browser.find_element_by_tag_name("button").click()


finally:
    time.sleep(10)
    browser.quit()