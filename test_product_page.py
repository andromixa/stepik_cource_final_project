import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import time


main_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
alt_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
promo_links = [f"{main_link}?promo=offer{x}" for x in range(10)]
# Mark expected fail
promo_links[7] = pytest.param(promo_links[7], marks=pytest.mark.xfail)


def credentials():
    return f"{str(time.time())}@fakemail.org", "qwerty+93874=X"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        product_page = ProductPage(browser, main_link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(*credentials())
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, main_link)
        product_page.open()
        product_page.add_to_cart()
        product_page.should_be_added()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, main_link)
        product_page.open()
        product_page.should_not_be_success_message(4)


@pytest.mark.need_review
@pytest.mark.parametrize("promo_link", promo_links)
def test_guest_can_add_product_to_basket(browser, promo_link):
    product_page = ProductPage(browser, promo_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_added()


@pytest.mark.xfail(reason="under development")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, main_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, main_link)
    product_page.open()
    product_page.should_not_be_success_message(4)


@pytest.mark.xfail(reason="under development")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, main_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_disappeared_success_message(4)


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, alt_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, alt_link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()
