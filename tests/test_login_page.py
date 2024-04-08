import settings
from locators import StellarBurgerLocators
from data import StellarBurgersTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarBurgerLogin:

    def test_login_by_chekout_button_on_main_page(self, driver):
        driver.get(settings.URL)

        main_page_login_button = driver.find_element(*StellarBurgerLocators.MAIN_PAGE_LOGIN_BUTTON)
        main_page_login_button.click()

        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_EMAIL_INPUT)
        login_input.send_keys(StellarBurgersTestData.AUTH_EMAIL)

        password_input = driver.find_element(*StellarBurgerLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(StellarBurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON))

        assert driver.find_element(*StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON).is_displayed()

    def test_login_by_personal_account_button(self, driver):  # вход через кнопку регистрации
        driver.get(settings.URL)

        personal_account_button = driver.find_element(*StellarBurgerLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_EMAIL_INPUT)
        login_input.send_keys(StellarBurgersTestData.AUTH_EMAIL)

        password_input = driver.find_element(*StellarBurgerLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(StellarBurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON))

        assert driver.find_element(*StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON).is_displayed()


    def test_login_by_registration_page_login_button(self, driver):
        driver.get(settings.URL + "/register")

        login_page_button = driver.find_element(*StellarBurgerLocators.REGISTRATION_LOGIN_BUTTON)
        login_page_button.click()

        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_EMAIL_INPUT)
        login_input.send_keys(StellarBurgersTestData.AUTH_EMAIL)

        password_input = driver.find_element(*StellarBurgerLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(StellarBurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON))

        assert driver.find_element(*StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON).is_displayed()


    def test_login_by_login_button_in_restore_password_page(self, driver):
        driver.get(settings.URL + "/forgot-password")

        restore_password_login_button = driver.find_element(*StellarBurgerLocators.RESTORE_PASSWORD_LOGIN_BUTTON)
        restore_password_login_button.click()

        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_EMAIL_INPUT)
        login_input.send_keys(StellarBurgersTestData.AUTH_EMAIL)

        password_input = driver.find_element(*StellarBurgerLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(StellarBurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON))

        assert driver.find_element(*StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON).is_displayed()
