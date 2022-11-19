from pages.base_page import BasePage
from resources.locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get ('https://www.bing.com/')
    
    def buscar_conteudo(self, informacao):
        self.enter_text(HomePageLocators.botao_pesquisar, informacao)
        self.click(HomePageLocators.campo_busca)