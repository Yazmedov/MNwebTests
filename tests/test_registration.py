import allure

from core.Base_Test import browser
from pages.Base_Page import BasePageHelper
from pages.Login_Page import LoginPageHelper
from pages.Registration_Page import RegistrationPageHelperHelper

BASE_URL = "https://ok.ru/"


@allure.suite("Проверка страницы регистрации")
@allure.title("Проверка регистрации со случайной страной")
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    Login_Page = LoginPageHelper(browser)
    Login_Page.click_registration()
    RegistrationPage = RegistrationPageHelperHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_country_code = RegistrationPage.get_phone_field_value()
    assert Selected_country_code == Actual_country_code




