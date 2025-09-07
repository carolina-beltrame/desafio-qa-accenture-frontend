# importando bibliotecas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# definindo a classe
class BrowserWindowsPage:
    def __init__(self, driver):
        # construtor
        self.driver = driver
        self.url = "https://demoqa.com/browser-windows"

        # locators
        self.NEW_TAB_BUTTON = (By.ID, "tabButton")
        self.NEW_WINDOW_BUTTON = (By.ID, "windowButton")
        self.SAMPLE_HEADING = (By.ID, "sampleHeading")

    def open_page(self):
        # método para abrir a URL da página
        self.driver.get(self.url)

    def open_new_tab(self):
        # método para clicar no botão para abrir uma nova aba
        self.driver.find_element(*self.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def open_new_window(self):
        # método para abrir uma nova janela 
        # requisito: Clicar no botão new Windows
        self.driver.find_element(*self.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_new_content(self):
        # espera para carregar o conteúdo da aba/janela
        # Certifica-se que uma nova janela foi aberta, e validar “This is a sample page” 
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SAMPLE_HEADING)
        )
        return self.driver.find_element(*self.SAMPLE_HEADING).text

    def close_current_window(self):
        # requisito: Fechar a nova janela aberta
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])