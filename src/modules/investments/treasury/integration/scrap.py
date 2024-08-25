from playwright.sync_api import sync_playwright

url = 'https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json'

def scrap_treasury_data() -> str | None:
    text_content = None

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json")
    
        text_content = page.query_selector('body > pre').text_content()

        browser.close()
    
    return text_content

