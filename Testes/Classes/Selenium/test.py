import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ProcedimentoBuscaProduto(unittest.TestCase):

    def test_search_no_find_product(self):
        driver = webdriver.Firefox()
        driver.get("http://automationpractice.com/")
        campo_busca = driver.find_element(By.ID, 'search_query_top')
        # ENTRADA
        campo_busca.send_keys('Blusa')

        # SAIDA ESPERADA
        mensagem_esperada = 'No results were found for your search "Blusa"'

        pesquisar = driver.find_element(By.NAME, 'submit_search')
        pesquisar.click()

        elemento = driver.find_element(By.XPATH, '//*[@id="center_column"]/p')
        mensagem_obtida = elemento.text

        self.assertEqual(mensagem_esperada, mensagem_obtida)
        driver.quit()

    def test_search_find_product(self):
        driver = webdriver.Firefox()
        driver.get("http://automationpractice.com/")
        campo_busca = driver.find_element(By.ID, 'search_query_top')
        # ENTRADA
        campo_busca.send_keys('Blouse')

        # SAIDA ESPERADA
        mensagem_esperada = 'Blouse'

        pesquisar = driver.find_element(By.NAME, 'submit_search')
        pesquisar.click()

        elemento = driver.find_element(
            By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/h5/a')
        mensagem_obtida = elemento.text

        self.assertEqual(mensagem_esperada, mensagem_obtida)
        driver.quit()
    
    def test_search_find_product(self):
        driver = webdriver.Firefox()
        driver.get("http://automationpractice.com/")
        campo_busca = driver.find_element(By.ID, 'search_query_top')
        # ENTRADA
        campo_busca.send_keys('Dress')

        # SAIDA ESPERADA
        mensagem_esperada = 'Dress'

        pesquisar = driver.find_element(By.NAME, 'submit_search')
        pesquisar.click()

        elemento = driver.find_element(
            By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/h5/a')
        mensagem_obtida = elemento.text

        self.assertEqual(mensagem_esperada, mensagem_obtida)
        driver.quit()

#mapeia e executa só o que é caso de teste
if __name__ == "__main__":
    unittest.main()
#torna a classe executável