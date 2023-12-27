from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        self.should_not_be_basket_items_list()
        self.should_be_empty_basket_message()

    def should_not_be_basket_items_list(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS_LIST, timeout=1
        ), "Basket items list is not empty, but it should be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE
        ), "There is no message that basket is empty, but it should be"
