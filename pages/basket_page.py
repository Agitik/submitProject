from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def there_is_no_purchases(self):
        self.is_not_element_present(*BasketPageLocators.BUYINGS)
        self.is_element_present(*BasketPageLocators.NO_BUYINGS)
