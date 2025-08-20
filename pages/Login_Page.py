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
    REGISTRATION = (By.XPATH,'//*[@id="tabpanel-login-9911528512"]/form/div[4]/div[2]/a')
    LOG_IN_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOG_IN_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOG_IN_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')

class LoginPageHelper(BasePage):
    pass
