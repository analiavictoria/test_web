from selenium.webdriver.common.by import By

class HomePageLocators():
    campo_busca = (By.ID, 'sb_form_q')
    botao_pesquisar = (By.ID, 'search_icon')

#mapear os locators do buscador