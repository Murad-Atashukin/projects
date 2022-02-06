from .pages.product_page import ProductPage
import time
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_product()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.should_be_coincide_name_books()
    page.should_be_coincide_prices_basket_and_book()
    page.should_be_success_message()