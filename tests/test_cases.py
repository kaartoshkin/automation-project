import pytest
import os
import time
from pathlib import Path
from faker import Faker
from pages.home_page import HomePage
from pages.login_signup_page import LoginSignupPage
from pages.account_info_page import AccountInfoPage
from pages.account_created_page import AccountCreatedPage
from pages.contact_us_page import ContactUsPage
from pages.test_cases_page import TestCasesPage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

fake = Faker()

@pytest.fixture(scope="function")
def user_data():
    """Fixture to generate fake user data for tests."""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(length=10),
        "dob_day": str(fake.random_int(min=1, max=28)),
        "dob_month": fake.date_object().strftime('%B'),
        "dob_year": str(fake.random_int(min=1980, max=2005)),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "United States",
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile_number": fake.phone_number(),
    }

def test_case_1_register_user(driver, user_data):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible(), "Home page is not visible"
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    assert "New User Signup!" in login_signup_page.get_new_user_signup_header()
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    assert "ENTER ACCOUNT INFORMATION" in account_info_page.get_account_info_header()
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    assert "ACCOUNT CREATED!" in account_created_page.get_account_created_header()
    account_created_page.click_continue()
    assert user_data['name'] in home_page.get_logged_in_user()
    home_page.delete_account()
    assert "ACCOUNT DELETED!" in account_created_page.get_account_deleted_header()
    account_created_page.click_continue()

def test_case_2_login_user_with_correct_credentials(driver, user_data):
    home_page = HomePage(driver)
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    account_created_page.click_continue()
    home_page.logout()
    assert "login" in home_page.get_current_url()
    home_page.go_to_login_signup_page()
    assert "Login to your account" in login_signup_page.get_login_header()
    login_signup_page.login(user_data['email'], user_data['password'])
    assert user_data['name'] in home_page.get_logged_in_user()
    home_page.delete_account()
    assert "ACCOUNT DELETED!" in account_created_page.get_account_deleted_header()

def test_case_3_login_user_with_incorrect_credentials(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    assert "Login to your account" in login_signup_page.get_login_header()
    login_signup_page.login(fake.email(), fake.password())
    assert "Your email or password is incorrect!" in login_signup_page.get_login_error_message()

def test_case_4_logout_user(driver, user_data):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    account_created_page.click_continue()
    assert user_data['name'] in home_page.get_logged_in_user()
    home_page.logout()
    assert "login" in home_page.get_current_url()

def test_case_5_register_user_with_existing_email(driver, user_data):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    account_created_page.click_continue()
    home_page.logout()
    home_page.go_to_login_signup_page()
    assert "New User Signup!" in login_signup_page.get_new_user_signup_header()
    login_signup_page.signup(fake.name(), user_data['email'])
    assert "Email Address already exist!" in login_signup_page.get_signup_error_message()

def test_case_6_contact_us_form(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_contact_us()
    contact_us_page = ContactUsPage(driver)
    assert "GET IN TOUCH" in contact_us_page.get_get_in_touch_header()
    contact_us_page.fill_contact_form(fake.name(), fake.email(), "Test Subject", "This is a test message.")
    file_path = "test_upload.txt"
    with open(file_path, "w") as f:
        f.write("This is a test file.")
    absolute_file_path = os.path.abspath(file_path)
    contact_us_page.upload_file(absolute_file_path)
    contact_us_page.submit_form()
    contact_us_page.accept_alert()
    assert "Success! Your details have been submitted successfully." in contact_us_page.get_success_message()
    contact_us_page.go_to_home()
    assert home_page.is_home_page_visible()
    os.remove(file_path)

def test_case_7_verify_test_cases_page(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_test_cases()
    test_cases_page = TestCasesPage(driver)
    assert "test_cases" in test_cases_page.get_current_url()
    assert test_cases_page.is_test_cases_page_visible()

def test_case_8_verify_all_products_and_product_detail_page(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    assert "products" in products_page.get_current_url()
    assert "ALL PRODUCTS" in products_page.get_all_products_header()
    assert products_page.is_products_list_visible()
    products_page.view_first_product()
    product_detail_page = ProductDetailPage(driver)
    assert "product_details" in product_detail_page.get_current_url()
    assert product_detail_page.are_product_details_visible()

def test_case_9_search_product(driver):
    product_to_search = "Tshirt"
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    assert "ALL PRODUCTS" in products_page.get_all_products_header()
    products_page.search_product(product_to_search)
    assert "SEARCHED PRODUCTS" in products_page.get_searched_products_header()
    searched_items = products_page.get_searched_products()
    assert len(searched_items) > 0
    for item in searched_items:
        assert product_to_search.lower() in item.text.lower()

def test_case_10_verify_subscription_in_home_page(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.scroll_to_subscription()
    assert "SUBSCRIPTION" in home_page.get_subscription_text()
    home_page.subscribe_with_email(fake.email())
    success_message = home_page.get_subscription_success_message()
    assert "You have been successfully subscribed!" in success_message

def test_case_11_verify_subscription_in_cart_page(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.scroll_to_subscription()
    assert "SUBSCRIPTION" in cart_page.get_subscription_text()
    cart_page.subscribe_with_email(fake.email())
    success_message = cart_page.get_subscription_success_message()
    assert "You have been successfully subscribed!" in success_message

def test_case_12_add_products_in_cart(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    products_page.add_product_by_id(1)
    products_page.click_continue_shopping()
    products_page.add_product_by_id(2)
    products_page.view_cart_in_modal()
    cart_page = CartPage(driver)
    assert len(cart_page.get_cart_products()) == 2
    assert cart_page.get_product_details_by_id(1) is not None
    assert cart_page.get_product_details_by_id(2) is not None

def test_case_13_verify_product_quantity_in_cart(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.view_first_product()
    product_detail_page = ProductDetailPage(driver)
    assert "product_details" in product_detail_page.get_current_url()
    product_detail_page.set_quantity("4")
    product_detail_page.add_to_cart()
    product_detail_page.view_cart_in_modal()
    cart_page = CartPage(driver)
    product_details = cart_page.get_product_details_by_id(1)
    assert product_details['quantity'] == "4"

def test_case_14_place_order_register_while_checkout(driver, user_data):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    products_page = ProductsPage(driver)
    home_page.go_to_products()
    products_page.add_product_by_id(1)
    products_page.click_continue_shopping()
    home_page.go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.is_cart_page_visible()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_register_login_on_modal()
    login_signup_page = LoginSignupPage(driver)
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    assert "ACCOUNT CREATED!" in account_created_page.get_account_created_header()
    account_created_page.click_continue()
    assert user_data['name'] in home_page.get_logged_in_user()
    home_page.go_to_cart()
    cart_page.proceed_to_checkout()
    assert user_data['first_name'] in checkout_page.get_delivery_address_text()
    checkout_page.enter_comment("Test order comment.")
    checkout_page.place_order()
    payment_page = PaymentPage(driver)
    card_details = {
        "name": user_data["name"],
        "number": fake.credit_card_number(),
        "cvc": fake.credit_card_security_code(),
        "month": str(fake.random_int(min=1, max=12)).zfill(2),
        "year": str(fake.random_int(min=2025, max=2030))
    }
    payment_page.fill_payment_details(card_details)
    payment_page.click_pay_and_confirm()
    assert "Order Placed" in payment_page.get_order_placed_message()
    home_page.delete_account()
    assert "ACCOUNT DELETED!" in account_created_page.get_account_deleted_header()
    account_created_page.click_continue()

def test_case_15_place_order_register_before_checkout(driver, user_data):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    assert "ACCOUNT CREATED!" in account_created_page.get_account_created_header()
    account_created_page.click_continue()
    assert user_data['name'] in home_page.get_logged_in_user()
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    products_page.add_product_by_id(1)
    products_page.click_continue_shopping()
    home_page.go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.is_cart_page_visible()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(driver)
    assert user_data['first_name'] in checkout_page.get_delivery_address_text()
    checkout_page.enter_comment("Test order comment.")
    checkout_page.place_order()
    payment_page = PaymentPage(driver)
    card_details = {
        "name": user_data["name"],
        "number": fake.credit_card_number(),
        "cvc": fake.credit_card_security_code(),
        "month": str(fake.random_int(min=1, max=12)).zfill(2),
        "year": str(fake.random_int(min=2025, max=2030))
    }
    payment_page.fill_payment_details(card_details)
    payment_page.click_pay_and_confirm()
    assert "Order Placed" in payment_page.get_order_placed_message()
    home_page.delete_account()
    assert "ACCOUNT DELETED!" in account_created_page.get_account_deleted_header()
    account_created_page.click_continue()

def test_case_16_place_order_login_before_checkout(driver, user_data):
    home_page = HomePage(driver)
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    account_created_page.click_continue()
    home_page.logout()
    home_page.go_to_login_signup_page()
    login_signup_page.login(user_data['email'], user_data['password'])
    assert user_data['name'] in home_page.get_logged_in_user()
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    products_page.add_product_by_id(1)
    products_page.click_continue_shopping()
    home_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(driver)
    assert user_data['first_name'] in checkout_page.get_delivery_address_text()
    checkout_page.place_order()
    payment_page = PaymentPage(driver)
    card_details = {
        "name": user_data["name"],
        "number": fake.credit_card_number(),
        "cvc": fake.credit_card_security_code(),
        "month": str(fake.random_int(min=1, max=12)).zfill(2),
        "year": str(fake.random_int(min=2025, max=2030))
    }
    payment_page.fill_payment_details(card_details)
    payment_page.click_pay_and_confirm()
    assert "Order Placed" in payment_page.get_order_placed_message()
    home_page.delete_account()
    assert "ACCOUNT DELETED!" in account_created_page.get_account_deleted_header()
    account_created_page.click_continue()

def test_case_17_remove_products_from_cart(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    products_page.add_product_by_id(1)
    products_page.view_cart_in_modal()
    cart_page = CartPage(driver)
    assert len(cart_page.get_cart_products()) == 1
    cart_page.remove_product_by_id(1)
    assert cart_page.is_cart_empty()

def test_case_18_view_category_products(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    products_page = ProductsPage(driver)
    assert products_page.is_categories_visible()
    products_page.click_women_category()
    products_page.click_dress_subcategory()
    assert "category_products" in products_page.get_current_url()
    assert "WOMEN - DRESS PRODUCTS" in products_page.get_category_header_text().upper()
    products_page.click_men_category()
    products_page.click_tshirts_subcategory()
    assert "MEN - TSHIRTS PRODUCTS" in products_page.get_category_header_text().upper()

def test_case_19_view_and_cart_brand_products(driver):
    home_page = HomePage(driver)
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    assert products_page.are_brands_visible()
    products_page.click_brand("Polo")
    assert "brand_products/Polo" in products_page.get_current_url()
    assert "BRAND - POLO PRODUCTS" in products_page.get_category_header_text().upper()
    products_page.click_brand("H&M")
    assert "brand_products/H&M" in products_page.get_current_url()
    assert "BRAND - H&M PRODUCTS" in products_page.get_category_header_text().upper()

def test_case_20_search_products_and_verify_cart_after_login(driver, user_data):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    account_created_page.click_continue()
    home_page.logout()
    driver.get(home_page.URL)
    product_to_search = "Dress"
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    products_page.search_product(product_to_search)
    assert "SEARCHED PRODUCTS" in products_page.get_searched_products_header()
    product_count = products_page.add_all_searched_products_to_cart()
    assert product_count > 0
    home_page.go_to_cart()
    cart_page = CartPage(driver)
    assert len(cart_page.get_cart_products()) == product_count
    home_page.go_to_login_signup_page()
    login_signup_page.login(user_data['email'], user_data['password'])
    home_page.go_to_cart()
    # Note: Website behavior clears cart on login. Test case expects persistence.
    # This assertion will likely fail, but it matches the test case requirement.
    assert len(cart_page.get_cart_products()) == product_count

def test_case_21_add_review_on_product(driver, user_data):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    products_page.view_first_product()
    product_detail_page = ProductDetailPage(driver)
    assert product_detail_page.is_write_review_visible()
    product_detail_page.submit_review(
        user_data['name'],
        user_data['email'],
        "This is a great product!"
    )
    assert "Thank you for your review." in product_detail_page.get_review_success_message()

def test_case_22_add_to_cart_from_recommended(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_bottom()
    assert home_page.is_recommended_items_visible()
    home_page.add_recommended_product_to_cart()
    home_page.view_cart_in_modal()
    cart_page = CartPage(driver)
    assert len(cart_page.get_cart_products()) > 0, "Cart is empty after adding recommended item"

def test_case_23_verify_address_details(driver, user_data):
    # Registration part
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    account_created_page.click_continue()
    
    # Add product to cart
    home_page.go_to_products()
    products_page = ProductsPage(driver)
    products_page.add_product_by_id(1)
    products_page.view_cart_in_modal()
    
    # Checkout and verify address
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(driver)

    expected_delivery_address = [
        f"Mr. {user_data['first_name']} {user_data['last_name']}",
        user_data['company'],
        user_data['address1'],
        user_data['address2'],
        f"{user_data['city']} {user_data['state']} {user_data['zipcode']}",
        user_data['country'],
        user_data['mobile_number']
    ]
    
    delivery_address_on_page = checkout_page.get_delivery_address_text()
    billing_address_on_page = checkout_page.get_billing_address_text()

    for detail in expected_delivery_address:
        assert detail in delivery_address_on_page
        assert detail in billing_address_on_page

    home_page.delete_account()
    account_created_page.click_continue()

def test_case_24_download_invoice(driver, user_data):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.go_to_login_signup_page()
    login_signup_page = LoginSignupPage(driver)
    login_signup_page.signup(user_data['name'], user_data['email'])
    account_info_page = AccountInfoPage(driver)
    account_info_page.fill_account_info(user_data)
    account_created_page = AccountCreatedPage(driver)
    account_created_page.click_continue()

    home_page.go_to_products()
    products_page = ProductsPage(driver)
    products_page.add_product_by_id(1)
    products_page.click_continue_shopping()
    home_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.place_order()
    
    payment_page = PaymentPage(driver)
    card_details = {
        "name": user_data["name"],
        "number": fake.credit_card_number(),
        "cvc": fake.credit_card_security_code(),
        "month": str(fake.random_int(min=1, max=12)).zfill(2),
        "year": str(fake.random_int(min=2025, max=2030))
    }
    payment_page.fill_payment_details(card_details)
    payment_page.click_pay_and_confirm()
    assert "Order Placed" in payment_page.get_order_placed_message()

    download_path = Path.home() / "Downloads"
    invoice_file = download_path / "invoice.txt"
    if invoice_file.exists():
        invoice_file.unlink()

    payment_page.download_invoice()

    is_downloaded = False
    for _ in range(10): 
        if invoice_file.exists() and invoice_file.stat().st_size > 0:
            is_downloaded = True
            break
        time.sleep(1)
    
    assert is_downloaded, "Invoice file was not downloaded"
    if invoice_file.exists():
        invoice_file.unlink()

    payment_page.continue_after_payment()

    home_page.delete_account()
    account_created_page.click_continue()

def test_case_25_scroll_up_and_down_with_arrow(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.scroll_to_bottom()
    assert "SUBSCRIPTION" in home_page.get_subscription_text()
    home_page.click_scroll_up_arrow()
    time.sleep(1) 
    assert home_page.is_carousel_text_visible()

def test_case_26_scroll_up_and_down_without_arrow(driver):
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible()
    home_page.scroll_to_bottom()
    assert "SUBSCRIPTION" in home_page.get_subscription_text()
    home_page.scroll_to_top()
    time.sleep(1)
    assert home_page.is_carousel_text_visible()
