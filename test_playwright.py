from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True roda sem abrir janela
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        browser.close()

if __name__ == "__main__":
    test_google_title()
