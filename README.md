<<<<<<< HEAD
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
```
# 1. Current Price Comparison - (Playwright)
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

----------------------------------------------------------------------------------------------


# 2. Windows Temp Files Cleanup Automation (Pyautogui)

**Windows Temp Files Cleanup Automation** is a Python script that uses **PyAutoGUI** to automatically clean up temporary files on Windows. The script simulates keyboard and mouse actions to free up disk space quickly and safely.

---

## Overview

The script automates the following tasks:

* Opens the **Run dialog**.
* Accesses **%temp%** and **C:\Windows\Temp** folders.
* Selects and deletes all temporary files.
* Closes **File Explorer** automatically.

It provides a fast and hands-free way to clean up temporary files without manually navigating folders.

---

## Features

* Automates deletion of **user temp files** (`%temp%`) and **system temp files** (`C:\Windows\Temp`).
* Fully automated using **PyAutoGUI**.
* Optional **fail-safe**: move the mouse to the top-left corner to immediately stop the script.
* Works on **Windows OS**.
* Includes **pauses** to prevent accidental mistakes.

---

## Installation

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. **Install PyAutoGUI**:

```bash
pip install pyautogui
```

3. **Optional (for Windows 10/11)** – install Pillow for screenshots:

```bash
pip install pillow
```

---

## Usage

Run the script:

```bash
python cleanup_temp.py
```

### Script Workflow

1. Opens **Run dialog** → `%temp%` → selects all files → deletes → confirms.
2. Repeats for **system temp folder** (`C:\Windows\Temp`).
3. Closes **File Explorer** after cleanup.

**Example terminal output:**

```
✅ Temp files cleanup automated successfully!
```

---

## Notes / Safety Tips

* **PyAutoGUI FAILSAFE** is enabled: move your mouse to the top-left corner to stop the script immediately.
* Save any important files before running, as **deleting temp files cannot be undone**.
* Run the script as a **user with administrative privileges** to clear system temp files.

---

## Future Enhancements

* Add a **GUI** for easier execution.
* Log deleted files and **disk space freed**.
* Include **scheduled automatic cleanup**.
* Add an option to **skip certain folders/files** for safety.
