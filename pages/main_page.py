# importando bibliotecas
from selenium.webdriver.common.by import By
import time

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/"
        
        # locators 
        self.FORMS_BUTTON = (By.XPATH, "//div[h5='Forms']")
        self.PRACTICE_FORM_LINK = (By.XPATH, "//span[text()='Practice Form']")
        self.ELEMENTS_BUTTON = (By.XPATH, "//div[h5='Elements']")
        self.WEB_TABLES_LINK = (By.XPATH, "//span[text()='Web Tables']")
        self.ALERTS_WINDOWS_BUTTON = (By.XPATH, "//div[h5='Alerts, Frame & Windows']")
        self.BROWSER_WINDOWS_LINK = (By.XPATH, "//span[text()='Browser Windows']")
        self.WIDGETS_BUTTON = (By.XPATH, "//div[h5='Widgets']")
        self.PROGRESS_BAR_LINK = (By.XPATH, "//span[text()='Progress Bar']")
        self.INTERACTIONS_BUTTON = (By.XPATH, "//div[h5='Interactions']")
        self.SORTABLE_LINK = (By.XPATH, "//span[text()='Sortable']")

    def open_page(self):
        # método para abrir a URL da página
        self.driver.get(self.url)

    def navigate_to_practice_form(self):
        # navega até Practice Form
        self.driver.find_element(*self.FORMS_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(*self.PRACTICE_FORM_LINK).click()

    def navigate_to_webtables(self):
        # navega até Web Tables
        self.driver.find_element(*self.ELEMENTS_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(*self.WEB_TABLES_LINK).click()
        
    def navigate_to_browser_windows(self):
        # navega até Browser Windows
        self.driver.find_element(*self.ALERTS_WINDOWS_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(*self.BROWSER_WINDOWS_LINK).click()
        
    def navigate_to_progress_bar(self):
        # navega até Progress Bar
        self.driver.find_element(*self.WIDGETS_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(*self.PROGRESS_BAR_LINK).click()
        
    def navigate_to_sortable(self):
        # navega até Sortable
        self.driver.find_element(*self.INTERACTIONS_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(*self.SORTABLE_LINK).click()