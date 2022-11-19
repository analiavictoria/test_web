from time import sleep
from selenium.webdriver import Firefox

browser = Firefox()

url = 'http://google.com'

browser.get(url)
sleep(2)
campo_busca = browser.find_element('tag name', 'input')
campo_busca.click()
campo_busca.send_keys('Muse')
campo_busca.submit()


