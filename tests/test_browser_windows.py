# importando bibliotecas
import pytest
from pages.main_page import MainPage
from pages.browser_windows_page import BrowserWindowsPage
import time

def test_browser_windows(driver):
    # navegação a partir da página inicial
    main_page = MainPage(driver)
    browser_windows_page = BrowserWindowsPage(driver)

    # navegação para a página Browser Windows
    main_page.open_page()
    # clicar em Alerts, Frame & Windows e depois em Browser Windows
    main_page.navigate_to_browser_windows()
    
    assert driver.title == "DEMOQA"
    
    # fluxo da nova janela
    browser_windows_page.open_new_window()
    new_window_text = browser_windows_page.get_new_content()
    assert "This is a sample page" in new_window_text
    # fechar a nova janela aberta
    browser_windows_page.close_current_window()
    
    print("\nDesafio 'Browser Windows' concluído com sucesso!")