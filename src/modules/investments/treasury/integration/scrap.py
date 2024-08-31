from playwright.sync_api import sync_playwright

url = 'https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json'

def scrap_treasury_data() -> str | None:
    text_content = None

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_extra_http_headers({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        })
        page.goto("https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json")
    
        import time
        import random
        time.sleep(random.randint(1, 3))

        page.evaluate('() => window.scrollBy(0, window.innerHeight)')

        text_content = page.query_selector('body > pre').text_content()

        browser.close()
    
    return text_content

