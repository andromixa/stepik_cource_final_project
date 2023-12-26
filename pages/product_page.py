from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()

    def should_be_added(self):
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_product_name(self):
        actual_product_name = self.get_text(*ProductPageLocators.GOOD_ACTUAL_NAME)
        product_name_in_cart = self.get_text(*ProductPageLocators.ADDED_GOOD_NAME)
        assert actual_product_name == product_name_in_cart, \
            'Actual product name is not the same as product in the cart has'

    def should_be_product_price(self):
        actual_product_price = self.get_text(*ProductPageLocators.GOOD_ACTUAL_PRICE)
        product_price_in_cart = self.get_text(*ProductPageLocators.ADDED_GOOD_PRICE)
        assert actual_product_price == product_price_in_cart, \
            'Actual product price is no equal to cart sum'

    def should_not_be_success_message(self, timeout=1):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout=timeout), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self, timeout=1):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout=timeout), \
            "Success message should disappear, but it's still there"
