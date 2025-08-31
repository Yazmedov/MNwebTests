import allure

from core.Base_Test import browser
from pages.Base_Page import BasePageHelper
from pages.Help_Page import HelpPageLocators,HelpPageHelperHelper
from pages.Advertisement_cabinet_help import AdvertisementCabinetHelpHelper

BASE_URL = "https://ok.ru/help"

@allure.suite("Проверка раздела помощь")
@allure.title("Проверка перехода в рекламный кабинет")
def test_help_text(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    Help_Page = HelpPageHelperHelper(browser)
    Help_Page.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)
