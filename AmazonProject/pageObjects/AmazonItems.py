from selenium.webdriver.common.by import By

class AmazonItemsPage:
#__init__ method serves as the constructor for a class - Called when an object is created
    def __init__(self,driver):
        self.driver = driver


    clearance_offers = (By.XPATH,"//img[@alt='Up to 50% off | Clearance offers']")
    select_clearance_item = (By.XPATH, "(//div[@class='a-section ProductCardImage-module__wrapper_YgLz4kq6ekChj01qeqOf'])[2]")
    clearance_product_title = (By.XPATH,"//span[@id='productTitle']")
    clearance_stock = (By.XPATH, "//span[@id='a-autoid-0-announce']")
    stock_choose = (By.CSS_SELECTOR,"#quantity_1")
    clearance_add_to_cart = (By.NAME, "submit.add-to-cart")
    protection = (By.XPATH, "//input[@aria-labelledby='attachSiAddCoverage-announce']")
    cart_option = (By.XPATH,"//span[@id='nav-cart-count']")
    cart_first_item_name = (By.XPATH, "(//span[contains(@class,'a-truncate-cut')])[1]")




    def get_clearance_offers(self):
        return self.driver.find_element(*AmazonItemsPage.clearance_offers)

    def get_selected_clearance_item(self):
        return self.driver.find_element(*AmazonItemsPage.select_clearance_item)

    def get_clearance_item_title(self):
        return self.driver.find_element(*AmazonItemsPage.clearance_product_title)

    def get_clearance_stock(self):
        return self.driver.find_element(*AmazonItemsPage.clearance_stock)

    def get_clearance_stock_number(self):
        return self.driver.find_element(*AmazonItemsPage.stock_choose)

    def get_clearance_item_cart(self):
        return self.driver.find_element(*AmazonItemsPage.clearance_add_to_cart)

    def get_protection_element(self):
        return self.driver.find_element(*AmazonItemsPage.protection)

    def get_cart_icon(self):
        return self.driver.find_element(*AmazonItemsPage.cart_option)

    def get_first_cart_item_name(self):
        return self.driver.find_element(*AmazonItemsPage.cart_first_item_name)






