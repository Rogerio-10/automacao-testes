from playwright.sync_api import sync_playwright
import time  # Importa o módulo de tempo

def test_login_sauce_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        time.sleep(5)
        page.fill('input[data-test="username"]', 'standard_user')
        time.sleep(5)
        page.fill('input[data-test="password"]', 'secret_sauce')
        time.sleep(5)
        page.click('input[data-test="login-button"]')
        time.sleep(5)

        assert page.is_visible('.inventory_list'), "Login falhou ou página não carregou corretamente"

        print("Login realizado com sucesso!")

        # Aguarda 5 segundos antes de fechar o navegador
        time.sleep(15)

        browser.close()

test_login_sauce_demo()
