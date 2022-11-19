import unittest
from selenium.webdriver import Firefox

from pages.bing_home_page import HomePage

class TestBingHome (unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.bing_home = HomePage(self.driver)
    
    def test_search_info(self):
        self.bing_home.buscar_conteudo('Instituto Flexpeak')
        resultado_obtido = self.bing_home.get_title()
        self.assertIn('flexpeak', resultado_obtido)


    #def tearDown(self):
    #    self.driver.quit()

if __name__ == "__main__":
    unittest.main()
