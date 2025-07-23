from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """
    Page Object for the Products Page.
    """
    # Locators
    ALL_PRODUCTS_HEADER = (By.XPATH, "//h2[text()='All Products']")
    PRODUCTS_LIST = (By.CSS_SELECTOR, "div.features_items div.col-sm-4")
    FIRST_PRODUCT_VIEW_LINK = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_HEADER = (By.XPATH, "//h2[text()='Searched Products']")
    SEARCHED_PRODUCTS_LIST = (By.CSS_SELECTOR, "div.productinfo.text-center")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, ".modal-footer button.btn")
    VIEW_CART_MODAL_LINK = (By.CSS_SELECTOR, "p > a[href='/view_cart']")
    CATEGORIES_SIDEBAR = (By.ID, "accordian")
    WOMEN_CATEGORY = (By.CSS_SELECTOR, "a[href='#Women']")
    DRESS_SUBCATEGORY = (By.CSS_SELECTOR, "#Women a[href='/category_products/1']")
    MEN_CATEGORY = (By.CSS_SELECTOR, "a[href='#Men']")
    TSHIRTS_SUBCATEGORY = (By.CSS_SELECTOR, "#Men a[href='/category_products/3']")
    CATEGORY_HEADER = (By.CSS_SELECTOR, "h2.title.text-center")
    BRANDS_SIDEBAR = (By.CSS_SELECTOR, ".brands_products")

    def get_all_products_header(self):
        return self.get_text(self.ALL_PRODUCTS_HEADER)

    def is_products_list_visible(self):
        return len(self.find_elements(self.PRODUCTS_LIST)) > 0

    def view_first_product(self):
        self.click(self.FIRST_PRODUCT_VIEW_LINK)
    
    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_searched_products_header(self):
        return self.get_text(self.SEARCHED_PRODUCTS_HEADER)
    
    def get_searched_products(self):
        return self.find_elements(self.SEARCHED_PRODUCTS_LIST)

    def add_product_by_id(self, product_id):
        product_to_hover_xpath = f"//a[@data-product-id='{product_id}']/ancestor::div[@class='product-image-wrapper']"
        self.scroll_to_element((By.XPATH, product_to_hover_xpath))
        self.hover_over_element((By.XPATH, product_to_hover_xpath))
        add_to_cart_button = (By.XPATH, f"//div[contains(@class, 'overlay-content')]//a[@data-product-id='{product_id}']")
        self.click(add_to_cart_button)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON, time=5)

    def view_cart_in_modal(self):
        self.click(self.VIEW_CART_MODAL_LINK)
    
    def add_all_searched_products_to_cart(self):
        product_links = self.find_elements((By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']/a[@data-product-id]"))
        product_ids = [link.get_attribute("data-product-id") for link in product_links]
        for product_id in product_ids:
            self.add_product_by_id(product_id)
            self.click_continue_shopping()
        return len(product_ids)

    def is_categories_visible(self):
        return self.find_element(self.CATEGORIES_SIDEBAR).is_displayed()
    
    def click_women_category(self):
        self.click(self.WOMEN_CATEGORY)

    def click_dress_subcategory(self):
        self.click(self.DRESS_SUBCATEGORY)
    
    def get_category_header_text(self):
        return self.get_text(self.CATEGORY_HEADER)

    def click_men_category(self):
        self.click(self.MEN_CATEGORY)
    
    def click_tshirts_subcategory(self):
        self.click(self.TSHIRTS_SUBCATEGORY)
    
    def are_brands_visible(self):
        return self.find_element(self.BRANDS_SIDEBAR).is_displayed()
    
    def click_brand(self, brand_name):
        brand_locator = (By.XPATH, f"//div[@class='brands_products']//a[contains(text(), '{brand_name}')]")
        self.click(brand_locator)
