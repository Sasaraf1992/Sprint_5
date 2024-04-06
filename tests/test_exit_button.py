import settings
from locators import StellarBurgerLocators
from data import StellarBurgersTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarBurgerExitButton:
    def test_logout_by_exit_button(self, driver):
        driver.get(settings.URL + '/login')

        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_EMAIL_INPUT)
        login_input.send_keys(StellarBurgersTestData.AUTH_EMAIL)

        password_input = driver.find_element(*StellarBurgerLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(StellarBurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        personal_account_button = driver.find_element(*StellarBurgerLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.PERSONAL_ACCOUNT_PAGE_PROFILE_BUTTON))

        exit_button = driver.find_element(*StellarBurgerLocators.PERSONAL_ACCOUNT_EXIT_BUTTON)
        exit_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.LOGIN_TITLE))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login" and driver.find_element(
            *StellarBurgerLocators.LOGIN_TITLE).is_displayed()
