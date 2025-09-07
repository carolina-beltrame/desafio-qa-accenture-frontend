# importando bibliotecas
import pytest
from pages.main_page import MainPage
from pages.webtables_page import WebTablesPage
from faker import Faker

def test_webtables_basic_flow(driver):
    faker = Faker()
    # navegação a partir da página inicial
    main_page = MainPage(driver)
    webtables_page = WebTablesPage(driver)

    # navegando até a página Web Tables
    main_page.open_page()
    main_page.navigate_to_webtables()
    assert driver.title == "DEMOQA", "Página inicial não carregou corretamente"

    # criação do registro
    email = faker.email()
    webtables_page.add_new_record(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=email,
        age="19",
        salary="5000",
        department="QA Automation Engineering"
    )
    assert webtables_page.is_record_in_table(email), f"Registro {email} não encontrado"

    # editar o registro
    webtables_page.edit_record(email, "6500")
    assert webtables_page.is_record_in_table(email), "Registro não encontrado após edição"

    # deletar o registro
    webtables_page.delete_record(email)
    assert not webtables_page.is_record_in_table(email), f"Registro {email} não foi deletado"

    print("\nTeste Web Tables concluído com sucesso!")
