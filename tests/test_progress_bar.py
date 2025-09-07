# importando bibliotecas
import pytest
from pages.progress_bar_page import ProgressBarPage
import time

def test_progress_bar_new_flow(driver):
    # navegação a partir da página inicial
    progress_bar_page = ProgressBarPage(driver)
    progress_bar_page.open_page()
    
    # clicar no botão start
    progress_bar_page.click_start_stop()
    
    # parar antes dos 25%
    progress_bar_page.stop_at_value(20)
    
    # validação de que é menor ou igual a 25%
    current_value = int(progress_bar_page.get_progress_value())
    assert current_value <= 25
    time.sleep(5) 
    
    # start novamente até chegar aos 100% e depois resetar
    progress_bar_page.click_start_stop()
    progress_bar_page.wait_for_value(100)
    progress_bar_page.click_reset()
    # validando que a barra resetou
    time.sleep(1)
    current_value_after_reset = progress_bar_page.get_progress_value()
    assert current_value_after_reset == "0"
    
    print("\nDesafio 'Progress Bar' concluído com sucesso!")