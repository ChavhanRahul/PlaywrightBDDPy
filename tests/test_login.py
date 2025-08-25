import pytest
from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate("https://practice.expandtesting.com/login#google_vignette")   # replace with real app URL
    login_page.login("practice", "SuperSecretPassword!")

    # welcome_text = login_page.get_welcome_message()
    # assert "You logged into a secure area!" in welcome_text