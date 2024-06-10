from selenium.webdriver.common.by import By


class CreateAccountPage:
    #__init__ method serves as the constructor for a class
    def __init__(self, driver):
        self.driver = driver

    create_account = (By.ID, "createAccountSubmit")
    landing_page_title = (By.XPATH, "//h1[contains(.,'Create Account')]")

    alert_name = (By.XPATH, "//div[@class='a-alert-content'][contains(.,'Enter your name')]")
    alert_mobile = (By.XPATH,"//input[contains(@id,'ap_phone_number')]")
    alert_password = (By.XPATH,"//input[@id='ap_password']")

    name_text = (By.ID, "ap_customer_name")
    mobile_numeric = (By.ID, "ap_phone_number")
    password_numeric = (By.ID, "ap_password")
    reenter_password_numeric = (By.ID, "ap_password_check")
    verify_mobile = (By.ID, "auth-continue")

    def create_account_button(self):
        return self.driver.find_element(*CreateAccountPage.create_account)

    def get_title(self):
        return self.driver.find_element(*CreateAccountPage.landing_page_title)

    def get_alert_message_name(self):
        return self.driver.find_element(*CreateAccountPage.alert_name)
    def get_alert_message_mobile(self):
        return self.driver.find_element(*CreateAccountPage.alert_mobile)
    def get_alert_message_password(self):
        return self.driver.find_element(*CreateAccountPage.alert_password)

    def get_name(self):
        return self.driver.find_element(*CreateAccountPage.name_text)

    def get_mobile_number(self):
        return self.driver.find_element(*CreateAccountPage.mobile_numeric)

    def get_password(self):
        return self.driver.find_element(*CreateAccountPage.password_numeric)

    def get_check_password(self):
        return self.driver.find_element(*CreateAccountPage.reenter_password_numeric)

    def get_verify_mobile(self):
        return self.driver.find_element(*CreateAccountPage.verify_mobile)

