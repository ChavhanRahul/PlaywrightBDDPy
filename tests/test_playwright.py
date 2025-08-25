def test_open_page(page):
    page.goto("https://playwright.dev/python/")
    assert "Playwright" in page.title()