from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    time.sleep(2)

    x_element = browser.find_element_by_tag_name("img")
    x = int(x_element.get_attribute("valuex"))

    y = calc(x)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)

    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()

    radio_btn = browser.find_element_by_id("robotsRule")
    radio_btn.click()

    submit_btn = browser.find_element_by_class_name("btn.btn-default")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
