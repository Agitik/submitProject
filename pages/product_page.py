from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_purchase_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def add_purchase_to_basket_par(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def is_purchase_name_right(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_after_add = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE).text
        assert book_name == book_name_after_add, "Названия книг не совпадают."

    def is_purchase_prise_right(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_after_add = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_AFTER_ADD).text
        assert book_price == book_price_after_add, "Цены не совпадают."

    def there_is_no_messgae_after_add_to_purschase(self, par=0):
        check = self.is_not_element_present(*ProductPageLocators.ACCEPT_MESSAGE)
        assert check, "Элемент есть на странице"

    def messgae_dissappeared_after_basket_add(self):
        check = self.is_disappeared(*ProductPageLocators.ACCEPT_MESSAGE)
        assert check, "Сообщение не исчезает"
