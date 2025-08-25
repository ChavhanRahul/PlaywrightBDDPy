from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button:has-text('Login')"
    SUCCESS_TEXT = "h1"

    def __init__(self, page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.fill_text(self.USERNAME_INPUT, username)
        self.fill_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_welcome_message(self):
        return self.get_text(self.SUCCESS_TEXT)