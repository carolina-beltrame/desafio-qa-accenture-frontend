# importando bibliotecas
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# troca palavras para números
WORD_TO_NUMBER = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6
}
NUMBER_TO_WORD = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six"
}

# definindo a classe
class SortablePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/sortable"
        self.LIST_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")

    def open_page(self):
        # método para abrir a URL da página
        self.driver.get(self.url)

    def get_list_items(self):
        # método para pegar todos os elementos da lista
        return self.driver.find_elements(*self.LIST_ITEMS)

    def get_item_texts(self):
        # método para pegar todos os elementos da lista
        items = self.get_list_items()
        return [item.text for item in items]

    def sort_by_dragging(self, from_index, to_index):
        # método para arrastar e soltar itens
        list_items = self.get_list_items()
        source = list_items[from_index]
        target = list_items[to_index]
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        time.sleep(0.5)

    def sort_in_descending_order(self):
        # por definição do site, os itens já estão em ordem crescente, então coloquei na ordem descrescente
        list_items_text = self.get_item_texts()
        for i in range(len(list_items_text)):
            correct_item_word = NUMBER_TO_WORD[len(list_items_text) - i]
            
            current_order_text = self.get_item_texts()
            if current_order_text[i] != correct_item_word:
                correct_item_index = current_order_text.index(correct_item_word)
                self.sort_by_dragging(correct_item_index, i)

    def sort_in_ascending_order(self):
        # ordenando os elementos na ordem crescente
        for i in range(len(self.get_item_texts())):
            correct_item_word = NUMBER_TO_WORD[i + 1]
            
            current_order_text = self.get_item_texts()
            if current_order_text[i] != correct_item_word:
                correct_item_index = current_order_text.index(correct_item_word)
                self.sort_by_dragging(correct_item_index, i)