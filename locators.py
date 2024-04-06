from selenium.webdriver.common.by import By

class StellarBurgerLocators:
    REGISTRATION_NAME_INPUT = (By.XPATH, "//div/input[@name = 'name']") #Поле имя на странице регистрации
    REGISTRATION_EMAIL_INPUT = [By.XPATH, "//fieldset[2]/div/div/input"] #Поле email на странице регистрации
    REGISTRATION_PASSWORD_INPUT = (By.NAME, "Пароль") #Поле пароль на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    REGISTRATION_TITLE = (By.XPATH, "//main/div/h2[text() = 'Регистрация']") #Заголовок "Регистрация"
    LOGIN_TITLE = (By.XPATH, "//main/div/h2[text() = 'Вход']") #Заголовок "Вход"
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//fieldset/div/p") #Ошибка "Некорректный пароль" на странице входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "//div/input[@name = 'name']") #Поле email на странице login
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//div/input[@name = 'Пароль']") #Поле пароль на странице login
    LOGIN_BUTTON = (By.XPATH,"//form/button") #Кнопка "Войти" на странице login
    MAIN_PAGE_HEADER = (By.XPATH, "//section/h1") #Заголовок "Соберите бургер" на главной странице
    MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") #Кнопка "Войти в аккаунт" на главной странице
    MAIN_PAGE_CHECKOUT_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']") #Кнопка "Оформить заказ" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//nav/a/p") #Кнопка "Личный кабинет" в шапке
    REGISTRATION_LOGIN_BUTTON = (By.XPATH, "//a[text() = 'Войти']") #Кнопка "Войти" на странице регистрации
    RESTORE_PASSWORD_LOGIN_BUTTON = (By.LINK_TEXT, "Войти") #Кнопка "Войти" на странице восстановления пароля
    PERSONAL_ACCOUNT_PAGE_PROFILE_BUTTON = (By.XPATH, "//a[@href = '/account/profile']") #Кнопка "Профиль" на странице profile
    HEADER_CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор") #Кнопка Конструктор в шапке
    HEADER_LOGO_BUTTON = (By.XPATH, ".//div/a[@href= '/']") #Кнопка "Лого" в шапке
    PERSONAL_ACCOUNT_EXIT_BUTTON = (By.XPATH, ".//li/button[@type = 'button']") #Кнопка "Выход" на странице profile
    CONSTRUCTOR_PAGE_SAUCE_BUTTON = (By.XPATH, ".//div/span[text() = 'Соусы']") #Кнопка "Соусы" на главной странице
    CONSTRUCTOR_PAGE_SAUCE_INGRIDIENTS = (By.XPATH, ".//div/ul[2]") #Список соусов на главной странице
    CONSTRUCTOR_PAGE_SAUCE_TITLE = (By.XPATH, ".//div/h2[2]") #Заголовок "Соусы" на главной странице
    CONSTRUCTOR_PAGE_BULKA_TITLE = (By.XPATH, ".//div/h2[1]") #Заголовок "Булки" на главной странице
    CONSTRUCTOR_PAGE_FILLER_BUTTON = (By.XPATH, "//div[3]/span") #Кнопка "Начинки" на главной странице
    CONSTRUCTOR_PAGE_BULKA_BUTTON = (By.XPATH, ".//div/span[text() = 'Булки']") #Кнопка "Булка" на главной странице
    CONSTRUCTOR_PAGE_BULKA_INGRIDIENTS = (By.XPATH, ".//div[2]/ul[1]") #Список булок на главной странице
    CONSTRUCTOR_PAGE_FILLER_INGRIDIENTS = (By.XPATH, "//div[2]/ul[3]") #Список начинок на главной странице
    CONSTRUCTOR_PAGE_FILLER_TITLE = (By.XPATH, "//h2[3]")







