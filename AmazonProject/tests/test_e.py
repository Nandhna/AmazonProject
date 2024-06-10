import time

import driver
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from TestData.dataProvider import  get_excel_data
from pageObjects.AmazonItems import AmazonItemsPage
from pageObjects.CreateAmazonAccount import CreateAccountPage
from pageObjects.LoginPage import SigninPage
from pageObjects.ShoptheStore import ShopTheStorePage
from pageObjects.TodaysDealsPage import TodaysDealsPage
from python_utilities.BaseClass import BaseClass
from TestData import dataProvider


class Testamazon(BaseClass):

    def test_login(self):
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.presence_of_element_located((By.ID, "nav-link-accountList")))

        self.driver.find_element(By.ID, "nav-link-accountList").click()

        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.presence_of_element_located((By.ID, "ap_email")))
        time.sleep(2)

        sign_in_page = SigninPage(self.driver)

        email_elemnt = sign_in_page.signin_Items()
        email_elemnt.send_keys("nandhnananz25@gmail.com")
        time.sleep(3)

        continue_button = sign_in_page.continue_button()
        continue_button.click()
        time.sleep(3)

        sign_in_page.password_field().send_keys("Nandhana@123!")
        time.sleep(2)
        sign_in_page.signin_button().click()

    @pytest.mark.usefixtures("setup")
    def test_amazon_homepage(self):

        #Verify page title to ensure the page is loaded
        assert "Amazon.ae" in self.driver.title, "Amazon homepage did not load successfully"


    def test_print_hellow_username(self):
        sign_in_page = SigninPage(self.driver)

        username_elmnt = sign_in_page.username()
        username_text_elmnt = username_elmnt.text
        print(f"{username_text_elmnt}")


    def test_amazon_items(self):
        amazon_clearance_items_page = AmazonItemsPage(self.driver)

        amazon_clearance_items_page.get_clearance_offers().click()
        time.sleep(5)
        amazon_clearance_items_page.get_selected_clearance_item().click()
        time.sleep(5)

        clearance_item_title = amazon_clearance_items_page.get_clearance_item_title()
        clearance_item_title_elmnt = clearance_item_title.text
        print(f"{clearance_item_title_elmnt}")

    def test_shop_store(self):
        amazon_shop_the_store_page = ShopTheStorePage(self.driver)

        budget_store_element = amazon_shop_the_store_page.get_budget_store()
        find_budget_store_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(budget_store_element))
        find_budget_store_element.click()

        budget_store_item_element = amazon_shop_the_store_page.get_budget_store_item()
        find_budget_store_item_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(budget_store_item_element))
        find_budget_store_item_element.click()
        time.sleep(2)

        amazon_shop_the_store_page.get_budget_store_item_choose().click()

        budget_store_item_title_elmnt = amazon_shop_the_store_page.get_budget_store_item_title()
        find_budget_store_item_element = budget_store_item_title_elmnt.text
        print(f"{find_budget_store_item_element}")

        amazon_shop_the_store_page.budget_store_stock().click()
        time.sleep(1)
        amazon_shop_the_store_page.get_budget_store_choose().click()
        time.sleep(2)
        amazon_shop_the_store_page.get_budget_store_add_to_cart().click()
        time.sleep(2)
        amazon_shop_the_store_page.get_protection().click()
        time.sleep(2)
        amazon_shop_the_store_page.get_cart_option().click()
        time.sleep(2)

        cart_item_title = amazon_shop_the_store_page.get_cart_first_item_name()
        cart_item_title_elmnt = cart_item_title.text
        print(f"{cart_item_title_elmnt}")



    # def test_scroll_to_element(self):
    #     amazon_clearance_items_page = AmazonItemsPage(self.driver)
    #
    #     stock_element = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//span[@id='a-autoid-0-announce']"))
    #     )
    #     amazon_clearance_items_page.get_clearance_stock().click()
    #     amazon_clearance_items_page.get_clearance_stock_number().click()
    #     time.sleep(2)
    #     amazon_clearance_items_page.get_clearance_item_cart().click()
    #     time.sleep(3)
    #
    #     amazon_clearance_items_page.get_protection_element().click()
    #     time.sleep(3)
    #     amazon_clearance_items_page.get_cart_icon().click()
    #     time.sleep(2)
    #
    #     #To read the First item name from the cart
    #     first_item_cart = amazon_clearance_items_page.get_first_cart_item_name()
    #     first_item_cart_elmnt = first_item_cart.text
    #     print(f"{first_item_cart_elmnt}")

    def test_deals_page(self):

        amazon_deals_page = TodaysDealsPage(self.driver)

        amazon_deals_page.get_todays_deals_menu().click()
        scroll_icon_elemnt = amazon_deals_page.get_scroll_right()
        scroll_icon_elemnt_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(scroll_icon_elemnt))


        action_chains = ActionChains(self.driver)
        for _ in range(3):
            action_chains.click(scroll_icon_elemnt_button).perform()
            time.sleep(2)

        all_deals_elmnt = amazon_deals_page.get_all_deals()
        all_deals_elmnt_text = all_deals_elmnt.text
        print(f"Choosen as {all_deals_elmnt_text}")
        time.sleep(2)
        all_deals_elmnt.click()
        time.sleep(5)


        see_more_locator = amazon_deals_page.get_see_more_filters()
         # Scroll to the target element using JavaScript
        self.driver.execute_script("arguments[0].scrollIntoView();", see_more_locator)
        # Optionally, wait for a short period to ensure the scroll is completed
        WebDriverWait(driver, 3).until(EC.visibility_of(see_more_locator))
        see_more_locator.click()
        time.sleep(2)

    def test_filter_product_page(self):
        amazon_filter_product_page = TodaysDealsPage(self.driver)

        amazon_filter_product_page.get_choose_filter().click()
        time.sleep(5)
        select_product_element = amazon_filter_product_page.get_select_product()
        select_product_element.click()
        time.sleep(3)
        filtered_product = amazon_filter_product_page.get_selected_product_title()
        filtered_product_text = filtered_product.text
        print(f"Filtered and selected product is {filtered_product_text}")
        time.sleep(3)

    # @pytest.mark.usefixtures("setup")
    def test_side_image_hover(self):
        amazon_filter_product_page = TodaysDealsPage(self.driver)

        side_images = amazon_filter_product_page.get_side_images()
        # all_side_images = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(side_images))
        print(type(side_images))
        print(side_images)

        action = ActionChains(self.driver)

        #Hover over each image
        for image in side_images:
            action.move_to_element(image).perform()
            time.sleep(5)





