# Current Price Comparison - Investing.com

**Current Price Comparison** is a Python automation tool that fetches live market prices of major stocks and cryptocurrencies from [Investing.com](https://www.investing.com/) using **Playwright**. The tool generates a visual comparison chart and a text summary for quick analysis.

---

## Supported Symbols

Currently, the project supports the following symbols:

* **MSFT** – Microsoft
* **META** – Meta Platforms / Facebook
* **BTC** – Bitcoin
* **AAPL** – Apple
* **NVDA** – Nvidia
* **TSLA** – Tesla

---

## Features

* Automated scraping of **live market prices** from Investing.com.
* **Cross-browser automation** using Playwright.
* Graphical representation of prices using **matplotlib**.
* Exportable **analysis in a text file**.
* Automatically handles **cookie popups**.
* Compatible with **Windows, Linux, and macOS**.

---

## Installation

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. **Create and activate a virtual environment**:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install playwright matplotlib
playwright install
```

---

## Usage

Run the script:

```bash
python investing_1d_compare.py
```

### Outputs

* **Bar chart:** `current_comparison.png`
* **Text summary:** `current_analysis.txt`

**Example terminal output:**

```
MSFT: 195.32 USD
META: 330.45 USD
BTC: 35,200 USD
AAPL: 177.60 USD
NVDA: 280.75 USD
TSLA: 265.80 USD
```

---

## Future Enhancements

* Add support for **more stocks and cryptocurrencies** dynamically.
* Run **periodic updates** and track **intraday price changes**.
* Export data to **CSV or Excel** for further analysis.
* Optimize to **fetch all symbols in a single browser session** for faster execution.
