from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 200);")

    x = browser.find_element_by_id("input_value").text
    result = calc(int(x))

    input_field = browser.find_element_by_id("answer").send_keys(str(result))

    check_box = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radio_btn = browser.find_element_by_css_selector("[for='robotsRule']").click()

    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()
