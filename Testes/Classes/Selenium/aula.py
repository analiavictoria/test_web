from time import sleep
from selenium.webdriver import Firefox

browser = Firefox()

browser.get('https://curso-python-selenium.netlify.app/aula_03.html')
sleep(2)

elemento = browser.find_element('tag name', 'a')
print(elemento.text)

''' for click in range(1,11):
    elemento.click()
    paragrafo = browser.find_element('tag name', 'p')
    print(paragrafo.text)
'''
for click in range(1,11):
    elemento.click()
    paragrafo = browser.find_elements('tag name', 'p')
    print('Valor do paragrafo', paragrafo[-1].text)

browser.quit()

