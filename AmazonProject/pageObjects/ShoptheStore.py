from selenium.webdriver.common.by import By

class ShopTheStorePage:
    def __init__(self,driver):
        self.driver = driver


    budget_store = (By.XPATH, "(//img[@class='product-image'])[1]")
    budget_store_item = (By.XPATH, "//a[@aria-label='# Furniture']")
    budget_store_item_choose = (By.XPATH, "(//span[contains(@class,'a-size-medium a-color-base a-text-normal')])[3]")
    budget_store_item_title = (By.XPATH, "//span[@id='productTitle']")
    budget_store_stock = (By.XPATH, "//span[@class='a-dropdown-label'][contains(.,'Quantity:')]")
    budget_store_choose = (By.CSS_SELECTOR,"#quantity_1")
    budget_store_add_to_cart = (By.NAME, "submit.add-to-cart")
    protection = (By.XPATH, "//input[@aria-labelledby='attachSiAddCoverage-announce']")
    cart_option = (By.XPATH,"//span[@id='nav-cart-count']")
    cart_first_item_name = (By.XPATH, "(//span[contains(@class,'a-truncate-cut')])[1]")


    def get_budget_store(self):
        return self.driver.find_element(*ShopTheStorePage.budget_store)

    def get_budget_store_item(self):
        return self.driver.find_element(*ShopTheStorePage.budget_store_item)

    def get_budget_store_item_choose(self):
        return self.driver.find_element(*ShopTheStorePage.budget_store_item_choose)

    def get_budget_store_item_title(self):
        return self.driver.find_element(*ShopTheStorePage.budget_store_item_title)

    def get_budget_store_stock(self):
        return self.driver.find_element(*ShopTheStorePage.budget_store_stock)

    def get_budget_store_choose(self):
        return self.driver.find_element(*ShopTheStorePage.budget_store_choose)

    def get_budget_store_add_to_cart(self):
        return self.driver.find_element(*ShopTheStorePage.budget_store_add_to_cart)

    def get_protection(self):
        return self.driver.find_element(*ShopTheStorePage.protection)

    def get_cart_option(self):
        return self.driver.find_element(*ShopTheStorePage.cart_option)

    def get_cart_first_item_name(self):
        return self.driver.find_element(*ShopTheStorePage.cart_first_item_name)









