from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def go_to_add_product(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()

    def should_be_coincide_name_books(self):
        name_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        check_name_book = self.browser.find_element(*ProductPageLocators.CHECK_BOOK_NAME).text
        assert name_book == check_name_book, 'Error added'

    def should_be_coincide_prices_basket_and_book(self):
        price_book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert price_book == basket_price, 'Error price'

    def should_be_success_message(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert "был добавлен в вашу корзину." in success_message, 'Error message'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


