from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    GOOD_ACTUAL_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    GOOD_ACTUAL_PRICE = (By.CSS_SELECTOR, '.product_main>p')
    ADDED_GOOD_NAME = (By.CSS_SELECTOR, '#messages>div:first-child strong')
    ADDED_GOOD_PRICE = (By.CSS_SELECTOR, '#messages>div:last-child strong')
