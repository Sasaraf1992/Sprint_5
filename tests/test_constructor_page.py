import settings
from locators import StellarBurgerLocators



class TestStellarBurgerConstructorPage:

    def test_change_section_on_sauce(self, driver):
        driver.get(settings.URL)

        sauce_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_SAUCE_BUTTON)
        sauce_button.click()

        sauce_list = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_SAUCE_INGRIDIENTS)
        sauce_title = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_SAUCE_TITLE)

        assert sauce_list.is_displayed() and sauce_title.is_displayed()

    def test_change_section_on_bulki(self,driver):
        driver.get(settings.URL)

        sauce_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_SAUCE_BUTTON)
        sauce_button.click()

        bulki_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_BULKA_BUTTON)
        bulki_button.click()

        bulki_list = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_BULKA_INGRIDIENTS)
        bulki_title = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_BULKA_TITLE)

        assert bulki_list.is_displayed() and bulki_title.is_displayed()

    def test_change_section_on_filler(self,driver):
        driver.get(settings.URL)

        filler_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_FILLER_BUTTON)
        filler_button.click()


        filler_list = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_FILLER_INGRIDIENTS)
        filler_title = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_PAGE_FILLER_TITLE)

        assert filler_list.is_displayed() and filler_title.is_displayed()


