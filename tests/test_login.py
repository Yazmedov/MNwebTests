import allure

from core.Base_Test import browser
from pages.Base_Page import BasePage
from pages.Login_Page import LoginPageHelper

BASE_URL = "https://ok.ru/"
EMPTY_LOGIN_ERROR = "Введите логин"

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустой форме авторизации")
def test_empty_login_end_password(browser):
    BasePage(browser).get_url(BASE_URL)
    Login_Page = LoginPageHelper(browser)
    Login_Page.click_login()
    assert Login_Page.get_error_text() == EMPTY_LOGIN_ERROR

@allure.title("Проверка ошибки ввода пароля при пустом логине")
def test_password(browser):
    BasePage(browser).get_url(BASE_URL)
    Login_Page = LoginPageHelper(browser)
    Login_Page.error_password()
    Login_Page.click_login()
    assert Login_Page.get_error_text() == EMPTY_LOGIN_ERROR




