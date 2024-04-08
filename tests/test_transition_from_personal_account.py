import settings
from locators import StellarBurgerLocators
from data import StellarBurgersTestData


class TestStellarBurgerPersonalAccount:
    def test_transition_in_constructor_by_constructor_button(self, driver):
        driver.get(settings.URL + '/login')
        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_EMAIL_INPUT)
        login_input.send_keys(StellarBurgersTestData.AUTH_EMAIL)
        password_input = driver.find_element(*StellarBurgerLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(StellarBurgersTestData.AUTH_PASSWORD)
        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()
        personal_account_button = driver.find_element(*StellarBurgerLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()
        constructor_button = driver.find_element(*StellarBurgerLocators.HEADER_CONSTRUCTOR_BUTTON)
        constructor_button.click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and driver.find_element(
            *StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON).is_displayed()

    def test_transition_in_constructor_by_logo_button(self, driver):
        driver.get(settings.URL + '/login')
        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_EMAIL_INPUT)
        login_input.send_keys(StellarBurgersTestData.AUTH_EMAIL)
        password_input = driver.find_element(*StellarBurgerLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(StellarBurgersTestData.AUTH_PASSWORD)
        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()
        personal_account_button = driver.find_element(*StellarBurgerLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()
        logo_button = driver.find_element(*StellarBurgerLocators.HEADER_LOGO_BUTTON)
        logo_button.click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and driver.find_element(
            *StellarBurgerLocators.MAIN_PAGE_CHECKOUT_BUTTON).is_displayed()
