from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASS_INPUT = (By.ID, "id_registration-password1")
    REGISTER_PASS_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GOOD_ACTUAL_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    GOOD_ACTUAL_PRICE = (By.CSS_SELECTOR, ".product_main>p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:first-child")
    ADDED_GOOD_NAME = (By.CSS_SELECTOR, "#messages>div:first-child strong")
    ADDED_GOOD_PRICE = (By.CSS_SELECTOR, "#messages>div:last-child strong")


class BasketPageLocators:
    BASKET_ITEMS_LIST = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
