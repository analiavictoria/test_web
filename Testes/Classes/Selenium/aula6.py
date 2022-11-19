from functools import partial
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from time import sleep


driver = webdriver.Firefox()
driver.get("http://automationpractice.com/")

# BUSCAR POR ID
# element = driver.find_element(By.ID, 'home-page-tabs')
# print(element.text)

# BUSCAR POR NAME
# element = driver.find_element(By.NAME, 'search_query')
# print(element.text)


# BUSCAR POR XPATH
# element = driver.find_element(
#     By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/a')
# print(element.text)

# BUSCAR POR XPATH
# element = driver.find_element(
#     By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')
# print(element.text)

continue_link = driver.find_element(By.LINK_TEXT, 'My orders')

# BUSCAR POR LINKS
# continue_link = driver.find_element(By.LINK_TEXT, 'My orders')
# print(continue_link.text)

# partial = driver.find_element(By.PARTIAL_LINK_TEXT, 'Selen')
# print(partial.text)

# BUSCAR POR CLASS
# content = driver.find_element(By.CLASS_NAME, 'sf-with-ul')
# print(content.text)

# BUSCAR POR TAGS
# elements = driver.find_elements(By.TAG_NAME, 'a')
# for element in elements:
#     print(element.text)

# driver.quit()