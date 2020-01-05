from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)

    journey_button = browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert.accept()

    x_element = browser.find_element_by_id("input_value").text
    result = calc(x_element)

    input_field = browser.find_element_by_tag_name("input").send_keys(result)

    submit_button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()