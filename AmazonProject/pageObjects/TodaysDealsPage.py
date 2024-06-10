from selenium.webdriver.common.by import By

class TodaysDealsPage:
    def __init__(self,driver):
        self.driver = driver

    todays_deals_menu = (By.XPATH,"//a[@href='/deals?ref_=nav_cs_gb']")
    scroll_right = (By.XPATH, "//span[@class='a-button-inner'][contains(.,'Next')]")
    all_deals = (By.XPATH, "//button[contains(.,'All Deals')]")
    see_more_filters = (By.XPATH, "//a[contains(.,'See more')]")
    choose_filter = (By.XPATH, "(//i[@class='a-icon a-icon-radio'])[6]")
    select_product = (By.XPATH,"(//div[@class='a-section ProductCardImage-module__wrapper_YgLz4kq6ekChj01qeqOf'])[3]")
    selected_product_title = (By.XPATH, "//span[@id='productTitle']")
    side_images = (By.XPATH, "//ul[contains(@class,'a-unordered-list a-nostyle a-button-list a-vertical a-spacing-top-micro regularAltImageViewLayout')]")





    def get_todays_deals_menu(self):
        return self.driver.find_element(*TodaysDealsPage.todays_deals_menu)

    def get_scroll_right(self):
        return self.driver.find_element(*TodaysDealsPage.scroll_right)

    def get_all_deals(self):
        return self.driver.find_element(*TodaysDealsPage.all_deals)

    def get_see_more_filters(self):
        return self.driver.find_element(*TodaysDealsPage.see_more_filters)

    def get_choose_filter(self):
        return self.driver.find_element(*TodaysDealsPage.choose_filter)

    def get_select_product(self):
        return self.driver.find_element(*TodaysDealsPage.select_product)

    def get_selected_product_title(self):
        return self.driver.find_element(*TodaysDealsPage.selected_product_title)

    def get_side_images(self):
        return self.driver.find_elements(*TodaysDealsPage.side_images)


