import pytest
from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
promo_links = [f'{link}?promo=offer{x}' for x in range(10)]
# Mark expected fail
promo_links[7] = pytest.param(promo_links[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize('promo_link', promo_links)
def test_guest_can_add_product_to_basket(browser, promo_link):
    product_page = ProductPage(browser, promo_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_added()


@pytest.mark.xfail(reason="under development")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message(4)


@pytest.mark.xfail(reason="under development")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_disappeared_success_message(4)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

