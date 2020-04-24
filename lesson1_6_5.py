from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector(".first_block .first")
    input1.send_keys('text')
    input2 = browser.find_element_by_css_selector(".first_block .second")
    input2.send_keys('text')
    input3 = browser.find_element_by_css_selector(".first_block .third")
    input3.send_keys('text')
    input4 = browser.find_element_by_css_selector(".second_block .first")
    input4.send_keys('text')
    input5 = browser.find_element_by_css_selector(".second_block .second")
    input5.send_keys('text')
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    
    time.sleep(5)
    
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
    