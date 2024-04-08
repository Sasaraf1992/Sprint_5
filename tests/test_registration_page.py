import settings
from locators import StellarBurgerLocators
from faker import Faker
fake = Faker()
from data import StellarBurgersTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class TestStellarBurgerRegistration:

    def test_registration(self, driver):
        driver.get(settings.URL + "/register")

        name_input = driver.find_element(*StellarBurgerLocators.REGISTRATION_NAME_INPUT)
        name_input.send_keys(fake.first_name())

        email_input = driver.find_element(*StellarBurgerLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(fake.ascii_free_email())

        password_input = driver.find_element(*StellarBurgerLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(StellarBurgersTestData.AUTH_PASSWORD)

        submit_button = driver.find_element(*StellarBurgerLocators.REGISTRATION_BUTTON)
        submit_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.LOGIN_TITLE))

        login_title = driver.find_element(*StellarBurgerLocators.LOGIN_TITLE)

        assert login_title.is_displayed()

    def test_incorrect_password(self, driver):
        driver.get(settings.URL + "/register")

        name_input = driver.find_element(*StellarBurgerLocators.REGISTRATION_NAME_INPUT)
        name_input.send_keys(fake.first_name())

        email_input = driver.find_element(*StellarBurgerLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(fake.ascii_free_email())

        password_input = driver.find_element(*StellarBurgerLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(StellarBurgersTestData.WRONG_PASSWORD)

        submit_button = driver.find_element(*StellarBurgerLocators.REGISTRATION_BUTTON)
        submit_button.click()

        incorrect_password = driver.find_element(*StellarBurgerLocators.INCORRECT_PASSWORD_ERROR)

        assert incorrect_password.is_displayed()


