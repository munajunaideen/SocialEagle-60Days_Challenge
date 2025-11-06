from playwright.sync_api import sync_playwright
import matplotlib.pyplot as plt
import time

urls = {
    "MSFT": "https://www.investing.com/equities/microsoft-corp",
    "META": "https://www.investing.com/equities/facebook-inc",
    "AAPL": "https://www.investing.com/equities/apple-computer-inc",
    "NVDA": "https://www.investing.com/equities/nvidia-corp",
    "TSLA": "https://www.investing.com/equities/tesla-motors"
}

def get_current_price(symbol):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        )
        page.goto(urls[symbol], timeout=60000, wait_until="domcontentloaded")

        # Close cookie popup if exists
        try:
            btn = page.query_selector("button.js-accept-all-close")
            if btn:
                btn.click()
                time.sleep(1)
        except:
            pass

        # Wait for the price using stable data-test attribute
        price_selector = 'span[data-test="instrument-price-last"]'
        page.wait_for_selector(price_selector, timeout=30000)
        price_text = page.query_selector(price_selector).inner_text()
        price = float(price_text.replace(",", ""))
        browser.close()
        return price

# Fetch current prices
prices = {}
for s in urls.keys():
    prices[s] = get_current_price(s)
    print(f"{s}: {prices[s]} USD")

# Quick bar chart
plt.bar(prices.keys(), prices.values(), color=["blue", "green", "orange"])
plt.title("Current Price Comparison")
plt.ylabel("Price (USD)")
plt.savefig("current_comparison.png")
plt.show()

# Export analysis
with open("current_analysis.txt", "w") as f:
    for s, p in prices.items():
        f.write(f"{s}: {p} USD\n")

print("Analysis saved to current_analysis.txt")
