# importando bibliotecas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# definindo a classe
class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/webtables"

        # locators
        self.ADD_BUTTON = (By.ID, "addNewRecordButton")
        self.SUBMIT_BUTTON = (By.ID, "submit")
        self.FIRST_NAME_FIELD = (By.ID, "firstName")
        self.LAST_NAME_FIELD = (By.ID, "lastName")
        self.EMAIL_FIELD = (By.ID, "userEmail")
        self.AGE_FIELD = (By.ID, "age")
        self.SALARY_FIELD = (By.ID, "salary")
        self.DEPARTMENT_FIELD = (By.ID, "department")
        self.TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tr-group")

    def open_page(self):
        # método para abrir a URL da página
        self.driver.get(self.url)

    def add_new_record(self, first_name, last_name, email, age, salary, department):
        # clicando no botão para adicionar um novo registro
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        ).click()

        # esperando o formulário ficar visível e preenchendo os campos
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.FIRST_NAME_FIELD)
        )
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.AGE_FIELD).send_keys(age)
        self.driver.find_element(*self.SALARY_FIELD).send_keys(salary)
        self.driver.find_element(*self.DEPARTMENT_FIELD).send_keys(department)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def find_record_row(self, email):
        # encontrando a linha da tabela que tem o e-mail cadastrado
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        for row in rows:
            if email in row.text:
                return row
        return None

    def edit_record(self, email_to_find, new_salary):
        # encontra a linha e clica no botão da edição
        row = self.find_record_row(email_to_find)
        if not row:
            raise Exception(f"Registro com email {email_to_find} não encontrado para edição.")
        edit_btn = row.find_element(By.CSS_SELECTOR, "span[title='Edit']")
        edit_btn.click()

        # esperando o formulário ficar vísivel e atualizando o salário
        salario_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.SALARY_FIELD)
        )
        salario_field.clear()
        salario_field.send_keys(new_salary)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def delete_record(self, email_to_find):
        # encontra a linha e clica no botão de deletar
        row = self.find_record_row(email_to_find)
        if not row:
            raise Exception(f"Registro com email {email_to_find} não encontrado para deletar.")
        delete_btn = row.find_element(By.CSS_SELECTOR, "span[title='Delete']")
        delete_btn.click()

    def is_record_in_table(self, email):
        # verifica se o registro foi apagado
        return bool(self.find_record_row(email))
