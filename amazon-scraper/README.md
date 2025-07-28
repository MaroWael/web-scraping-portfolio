# 🛍️ Amazon Egypt Web Scraper

A headless Selenium scraper that searches for a product on [Amazon.eg](https://www.amazon.eg/), collects details like title, price, rating, and specifications, then exports the data to an Excel file.

---

## 📌 Features

- 🔎 Product search via configurable query
- 🧠 Collects title, price, link, star rating, and technical specs
- 🔗 Opens product pages in new tabs for deeper scraping
- 📄 Outputs clean `amazon_products.xlsx` file
- 🧰 Logging system with warnings and errors
- 🛡️ Headless mode + real browser user-agent
- ✅ Cleaned and production-ready

---

## 🚀 Getting Started

### 📦 Install Requirements

1. **Create & Activate a Virtual Environment**

   **Windows CMD:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Linux/macOS:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes:
   ```
   selenium
   pandas
   webdriver-manager
   openpyxl
   ```

### 🧪 Run the Scraper

```bash
python scraper.py
```

The output will be saved to:

```
amazon_products.xlsx
```

⚠️ **Note**: The Excel file is excluded from the repo (via `.gitignore`).

---

## ⚙️ Configuration

Change the search keyword in `scraper.py`:

```python
query = 'iphone'
```

---

## 📁 Project Structure

```
amazon_scraper/
├── scraper.py
├── README.md
├── scraper.log
├── requirements.txt
├── .gitignore
└── venv/ # Virtual environment directory
```

---

## 🪵 Logging

All logs are written to `scraper.log`:

- Warnings for missing ratings/specs
- Errors for failed cards or network issues

---

## 📌 Notes

- Designed for Amazon Egypt with English interface.
- Website structure may change; always inspect elements before reusing selectors.
- Avoid scraping too frequently to prevent being blocked.
- Check [Amazon's Terms of Service](https://www.amazon.eg/gp/help/customer/display.html?nodeId=200505540) and consider using the [Amazon Product Advertising API](https://affiliate-program.amazon.com/) for legal data access.