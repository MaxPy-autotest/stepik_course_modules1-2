from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price_value = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element(By.ID, "book").click()

    x_element = browser.find_element_by_id("input_value").text
    result = calc(x_element)

    input_field = browser.find_element_by_tag_name("input").send_keys(result)

    submit_button = browser.find_element_by_id("solve").click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    browser.quit()