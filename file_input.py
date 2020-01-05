from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    for counter in range(1, 4):
        input_field = browser.find_element_by_xpath(
            f"//div[@class='form-group']/input[{counter}]").send_keys("My text")

    input_file = browser.find_element_by_css_selector("[type='file']")
    current_dir = os.path.dirname("/Users/allenmayer/PycharmProjects/webdriver/file_input.py")
    file_path = os.path.join(current_dir, "/Users/allenmayer/Desktop/text.txt")
    input_file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()