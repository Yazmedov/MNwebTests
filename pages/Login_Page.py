import allure

from pages.Base_Page import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocaters:
    LOGIN_FIELD = (By.ID, "field_email")
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    PASSWORD_FIELD = (By.ID, "field_password")
    SIGN_IN = (By.XPATH, '//*[@data-l="t,sign_in"]')
    SIGN_QR = (By.XPATH, '//*[@data-l="t,get_qr"]')
    CANNOT_LOG_IN = (By.XPATH, '//*[@data-l="t,get_qr"]')
    REGISTRATION_BUTTON = (By.XPATH,'//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    LOG_IN_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOG_IN_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOG_IN_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//div[@class="input-e login_error"]')
    PROFILE_RECOVERY_BUTTON = (By.XPATH,'//*[@name="st.go_to_recovery"]')
    GO_BACK_BUTTON = (By.XPATH,'//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH,'//*[@class="external-oauth-login-help portlet_f"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(LoginPageLocaters.LOGIN_FIELD)
        self.find_element(LoginPageLocaters.LOGIN_BUTTON)
        self.find_element(LoginPageLocaters.LOGIN_TAB)
        self.find_element(LoginPageLocaters.QR_TAB)
        self.find_element(LoginPageLocaters.PASSWORD_FIELD)
        self.find_element(LoginPageLocaters.SIGN_IN)
        self.find_element(LoginPageLocaters.SIGN_QR)
        self.find_element(LoginPageLocaters.CANNOT_LOG_IN)
        self.find_element(LoginPageLocaters.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocaters.LOG_IN_VK)
        self.find_element(LoginPageLocaters.LOG_IN_MAIL)
        self.find_element(LoginPageLocaters.LOG_IN_YANDEX)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocaters.LOGIN_BUTTON).click()

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocaters.ERROR_TEXT).text

    @allure.step("Вводим 'test' в поле пароля")
    def error_password(self):
        self.find_element(LoginPageLocaters.PASSWORD_FIELD).send_keys("test")
        self.attach_screenshot()

    @allure.step("Заполняем поле логин")
    def type_login(self, login):
        self.find_element(LoginPageLocaters.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step("Переходим к восстановлению")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocaters.PROFILE_RECOVERY_BUTTON).click()






