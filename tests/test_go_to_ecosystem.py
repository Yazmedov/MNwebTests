import allure

from core.Base_Test import browser
from pages.Base_Page import BasePageHelper
from pages.Login_Page import LoginPageHelper
from pages.Vk_ecosystem_page import VkEcosystemPageHelper

BASE_URL = "https://ok.ru/"

@allure.suite("Проверка тулбара")
@allure.title("Переход к проектам экосистемы VK")
def test_open_vk_ecosystem(browser):
    Base_Page = BasePageHelper(browser)
    Base_Page.get_url(BASE_URL)
    Base_Page.check_page()
    Login_Page = LoginPageHelper(browser)
    current_window_id = Login_Page.get_window_id(0)
    Login_Page.click_vk_ecosystem()
    Login_Page.click_more_button()
    new_window_id = Login_Page.get_window_id(1)
    Login_Page.switch_window(new_window_id)
    VkEcosystemPage = VkEcosystemPageHelper(browser)
    VkEcosystemPage.switch_window(current_window_id)
    LoginPageHelper(browser)

