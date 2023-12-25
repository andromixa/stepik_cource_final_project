import pytest
from .pages.product_page import ProductPage

links = [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{x}' for x in range(10)]
# Mark expected fail
links[7] = pytest.param(links[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_added()
