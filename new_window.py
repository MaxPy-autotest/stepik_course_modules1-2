from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    first_page_button = browser.find_element_by_tag_name("button").click()

    opened_window = browser.window_handles[1]
    browser.switch_to.window(opened_window)

    x_element = browser.find_element_by_id("input_value").text
    result = calc(x_element)

    input_field = browser.find_element_by_tag_name("input").send_keys(result)

    submit_button = browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert

    print(alert.text)

    alert.accept()

finally:
    time.sleep(10)
    browser.quit()