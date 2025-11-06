from playwright.sync_api import sync_playwright

websites = [
    "https://cleev.ch",
    "https://b-mashura.com",
    "https://mashurajournal.com",
    "https://imjct.com",
    "https://pro-translators.com",
    "https://seefeldresidenz.ch",
    "https://seefeldappartement.ch",
    "https://baitak.qa",
    "https://ifcdoha.com",
    "https://dhlc.edu.lk"

]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for site in websites:
        try:
            page.goto(site, timeout=10000)  # 10 sec timeout
            print(f"{site} loaded successfully ✅")
            page.screenshot(path=f"screenshot_{site.replace('https://', '').replace('/', '_')}.png")
        except Exception as e:
            print(f"❌ Could not load {site}: {e}")

    browser.close()
