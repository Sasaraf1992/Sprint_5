import settings
from locators import StellarBurgerLocators


class TestStellarBurgerConstructorPage:

    def test_change_section_on_sauce(self, driver):
        driver.get(settings.URL)
        sauce_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_SAUCE_BUTTON)
        sauce_button.click()
        sauce_button_active = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_SAUCE_BUTTON_ACTIVE)
        assert sauce_button_active.is_displayed()

    def test_change_section_on_bulki(self, driver):
        driver.get(settings.URL)
        sauce_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_SAUCE_BUTTON)
        sauce_button.click()
        bulki_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_BULKA_BUTTON)
        bulki_button.click()
        bulki_button_active = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_BULKA_BUTTON_ACTIVE)
        assert bulki_button_active.is_displayed()

    def test_change_section_on_filler(self, driver):
        driver.get(settings.URL)
        filler_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_FILLER_BUTTON)
        filler_button.click()
        filler_button_active = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_FILLER_BUTTON_ACTIVE)
        assert filler_button_active.is_displayed()
