# importando bibliotecas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# definindo a classe
class ProgressBarPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/progress-bar"

        # locators
        self.START_STOP_BUTTON = (By.ID, "startStopButton")
        self.RESET_BUTTON = (By.ID, "resetButton")
        self.PROGRESS_BAR = (By.CSS_SELECTOR, ".progress-bar")

    def open_page(self):
        # método para abrir a URL da página
        self.driver.get(self.url)

    def click_start_stop(self):
        # clicar no botão start/stop
        self.driver.find_element(*self.START_STOP_BUTTON).click()

    def click_reset(self):
        # resetar a barra
        self.driver.find_element(*self.RESET_BUTTON).click()

    def get_progress_value(self):
        # método para pegar o valor da barra em progresso
        progress_bar_element = self.driver.find_element(*self.PROGRESS_BAR)
        return progress_bar_element.get_attribute("aria-valuenow")

    def stop_at_value(self, target_value):
        # stop antes dos 25%
        value = 0
        while value < target_value:
            value = int(self.get_progress_value())
            time.sleep(0.1)  
        self.click_start_stop()
        
    def wait_for_value(self, target_value):
        # esperar até que alcance o 100%
        WebDriverWait(self.driver, 60).until(
            lambda driver: int(self.get_progress_value()) >= target_value
        )