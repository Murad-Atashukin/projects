from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, '#register_form')
    EMAIL_REGISTER = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTER = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_PASSWORD_REGISTER = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button')

class ProductPageLocators:
    BUTTON_ADD = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    CHECK_BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, '.basket-items') # селектор, для корзины с товаром
    EMPTY_MESSAGE_BASKET = (By.CSS_SELECTOR, '#content_inner > p') # селектор с сообщением о пустой корзине