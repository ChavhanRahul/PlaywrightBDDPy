from behave import given, when, then
from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

def after_all(context):
    context.browser.close()
    context.playwright.stop()

@given("I open the browser")
def step_open_browser(context):
    # Already handled in before_all
    pass

@when('I navigate to "{url}"')
def step_go_to(context, url):
    context.page.goto(url)

@when('I fill "{field}" with "{value}"')
def step_fill_field(context, field, value):
    context.page.fill(f'input[name="{field}"]', value)
@when('I click "{button}"')
def step_click_button(context, button):
    context.page.click(f'button:has-text("{button}")')

@then('I should see "{text}"')
def step_should_see_text(context, text):
    assert text in context.page.inner_text("body")