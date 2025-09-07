# importando bibliotecas# 
import pytest
from pages.sortable_page import SortablePage
import time

def test_sortable_flow(driver):
    sortable_page = SortablePage(driver)
    sortable_page.open_page()

    initial_order = sortable_page.get_item_texts()
    assert initial_order == ["One", "Two", "Three", "Four", "Five", "Six"]
    
    # ordena a lista em ordem decrescente
    sortable_page.sort_in_descending_order()
    
    # validando se a lista está em ordem decrescente
    final_order_desc = sortable_page.get_item_texts()
    assert final_order_desc == ["Six", "Five", "Four", "Three", "Two", "One"]
    
    # ordena a lista de volta para ordem crescente
    sortable_page.sort_in_ascending_order()

    # validando se a lista está em ordem crescente
    final_order_asc = sortable_page.get_item_texts()
    assert final_order_asc == ["One", "Two", "Three", "Four", "Five", "Six"]
    
    print("\nDesafio 'Sortable' concluído com sucesso!")