# importando bibliotecas
import pytest
from pages.main_page import MainPage
from pages.practice_form_page import PracticeFormPage
from faker import Faker
import time
import os

# cria um arquivo txt e depois o apaga
@pytest.fixture(scope="function")
def sample_file():
    file_path = os.path.join(os.getcwd(), "sample.txt")
    with open(file_path, "w") as f:
        f.write("Arquivo de teste")
    yield file_path
    os.remove(file_path)

# definindo a função
def test_practice_form_submission(driver, sample_file):
    faker = Faker()
    # navegação a partir da página inicial
    main_page = MainPage(driver)
    practice_form_page = PracticeFormPage(driver)
    
    # acessando o site
    main_page.open_page()
    # escolher a opção Forms na página inicial e clicar no submenu Practice Form
    main_page.navigate_to_practice_form()
    
    # preencher o formulário com valores aleatórios
    practice_form_page.fill_form(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        mobile="9999999999", 
        current_address=faker.address()
    )
    
    # selecionar gênero e hobbies
    practice_form_page.select_gender("Female")
    practice_form_page.select_hobbies(["Reading", "Sports"])
    
    # upload do arquivo
    practice_form_page.upload_picture(sample_file)
    
    # salvar o formulário
    practice_form_page.submit_form()
    
    # validar que o pop-up foi aberto
    assert practice_form_page.is_modal_visible()
    
    # fechar o pop-up
    practice_form_page.close_modal()

    print("\nDesafio 'Practice Form' concluído com sucesso!")