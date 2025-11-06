Current Price Comparison - Investing.com
Overview

This project is a Python automation tool that fetches the current market prices of major stocks and cryptocurrencies from Investing.com using Playwright. The script generates a visual comparison chart and a text summary of the prices for quick analysis.

Currently, the project supports the following symbols:

MSFT (Microsoft)
META (Meta Platforms / Facebook)
BTC (Bitcoin)
AAPL (Apple)
NVDA (Nvidia)
TSLA (Tesla)

Features

Automated scraping of live market prices from Investing.com.
Cross-browser automation using Playwright.
Graphical representation of prices using matplotlib.
Exportable analysis in a text file.
Handles cookie popups automatically.
Works on Windows, Linux, and macOS.

Installation

Clone this repository:

git clone <your-repo-url>
cd <repo-folder>


Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/macOS


Install dependencies:

pip install playwright matplotlib
playwright install

Usage

Run the script:
python investing_1d_compare.py


Outputs generated:
Bar chart: current_comparison.png

Text summary: current_analysis.txt
Example output in terminal:

MSFT: 195.32 USD
META: 330.45 USD
BTC: 35,200 USD
AAPL: 177.60 USD
NVDA: 280.75 USD
TSLA: 265.80 USD

Future Enhancements

Add more stocks and cryptocurrencies dynamically.
Run periodic updates and track intraday price changes.
Export data to CSV or Excel for further analysis.
Optimize to fetch all symbols in a single browser session for faster execution.