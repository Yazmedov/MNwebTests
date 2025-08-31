from pages.Base_Page import BasePageHelper
from selenium.webdriver.common.by import By
import allure

class AdvertisementCabinetHelpLocators:
    TITLE = (By.XPATH,'//span[text()="Рекламный кабинет"]')


class AdvertisementCabinetHelpHelper(BasePageHelper):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(AdvertisementCabinetHelpLocators.TITLE)
