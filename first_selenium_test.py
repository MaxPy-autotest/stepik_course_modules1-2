from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    time.sleep(2)

    fillText = "Мой текст"
    required_fields = browser.find_elements_by_css_selector('input[required]')

    for counter in range(1, len(required_fields)+1):
        input_field = browser.find_element_by_xpath(
            f"//div[@class='first_block']/div[{counter}]/input")
        input_field.send_keys(fillText)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(3)

    welcome_text_element = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_element.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

