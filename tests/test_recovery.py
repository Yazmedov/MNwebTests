import allure

from core.Base_Test import browser
from pages.Base_Page import BasePageHelper
from pages.Login_Page import LoginPageHelper
from pages.Recovery_Page import RecoveryPageHelperHelper

BASE_URL = "https://ok.ru/"
LOGIN_TEXT = "email"


@allure.suite("Проверка восстановления пользователя")
@allure.title("Проверка перехода к восстановлению после неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    Login_Page = LoginPageHelper(browser)
    Login_Page.type_login(LOGIN_TEXT)

    for i in range(3):
        Login_Page.error_password()
        Login_Page.click_login()

    Login_Page.click_recovery()
    RecoveryPageHelperHelper(browser)
