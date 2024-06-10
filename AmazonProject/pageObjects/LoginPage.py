from selenium.webdriver.common.by import By

class SigninPage:
#__init__ method serves as the constructor for a class -> Called when an object is created
    def __init__(self,driver):
        self.driver = driver

    email = (By.ID,"ap_email")
    continue_elmnt = (By.ID, "continue")
    password_elmnt = (By.ID, "ap_password")
    signin = (By.ID, "signInSubmit")

    username_text = (By.XPATH,"//span[contains(@id,'nav-link-accountList-nav-line-1')]")





    def signin_Items(self):
        return self.driver.find_element(*SigninPage.email)
    def continue_button(self):
        return self.driver.find_element(*SigninPage.continue_elmnt)

    def password_field(self):
        return self.driver.find_element(*SigninPage.password_elmnt)

    def signin_button(self):
        return self.driver.find_element(*SigninPage.signin)

    def username(self):
        return self.driver.find_element(*SigninPage.username_text)








