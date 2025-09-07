# importando bibliotecas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# definindo a classe 
class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

        # locators
        self.FIRST_NAME_FIELD = (By.ID, "firstName")
        self.LAST_NAME_FIELD = (By.ID, "lastName")
        self.EMAIL_FIELD = (By.ID, "userEmail")
        self.GENDER_RADIO = (By.CSS_SELECTOR, "div.custom-control.custom-radio")
        self.MOBILE_FIELD = (By.ID, "userNumber")
        self.DATE_OF_BIRTH_FIELD = (By.ID, "dateOfBirthInput")
        self.SUBJECTS_FIELD = (By.ID, "subjectsInput")
        self.HOBBIES_CHECKBOX = (By.CSS_SELECTOR, "div.custom-control.custom-checkbox")
        self.UPLOAD_PICTURE_BUTTON = (By.ID, "uploadPicture")
        self.CURRENT_ADDRESS_FIELD = (By.ID, "currentAddress")
        self.STATE_FIELD = (By.ID, "react-select-3-input")
        self.CITY_FIELD = (By.ID, "react-select-4-input")
        self.SUBMIT_BUTTON = (By.ID, "submit")
        self.SUBMISSION_MODAL = (By.CSS_SELECTOR, ".modal-content")
        self.MODAL_CLOSE_BUTTON = (By.ID, "closeLargeModal")
    
    def fill_form(self, first_name, last_name, email, mobile, current_address):
        # preecher os campos dos formulários
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.MOBILE_FIELD).send_keys(mobile)
        self.driver.find_element(*self.CURRENT_ADDRESS_FIELD).send_keys(current_address)
    
    def select_gender(self, gender):
        # selecionar o gênero
        gender_locator = (By.XPATH, f"//label[text()='{gender}']")
        self.driver.find_element(*gender_locator).click()

    def select_hobbies(self, hobbies):
        # selecionar hobby
        for hobby in hobbies:
            hobby_locator = (By.XPATH, f"//label[text()='{hobby}']")
            self.driver.find_element(*hobby_locator).click()

    def upload_picture(self, file_path):
        # upload do arquivo txt
        self.driver.find_element(*self.UPLOAD_PICTURE_BUTTON).send_keys(file_path)

    def submit_form(self):
        # salvar o fomulário
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.SUBMIT_BUTTON))

    def is_modal_visible(self):
        # verificar se o pop-up foi aberto
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUBMISSION_MODAL)
            )
            return True
        except:
            return False

    def close_modal(self):
        # fechar o pop-up
        self.driver.find_element(*self.MODAL_CLOSE_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.SUBMISSION_MODAL)
        )