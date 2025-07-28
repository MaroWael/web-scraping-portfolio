# 🕸️ Web Scraping Portfolio

Welcome to my web scraping project portfolio! This repository includes real-world scraping projects built with Python using `requests`, `BeautifulSoup`, and `Selenium`.

Each project includes:
- A clean, modular Python script
- Logging & error handling
- Export to Excel (`.xlsx`)
- A dedicated README with usage instructions

---

## 📁 Projects

### 📦 [1. Amazon.eg Product Scraper](./amazon_scraper/)
Scrapes product details (title, price, rating, specifications) for a given query from [Amazon Egypt](https://www.amazon.eg).

**Tech**: Selenium, headless Chrome, logging  
**Output**: `amazon_products.xlsx`

🔗 [View Project →](./amazon_scraper)

---

### 💼 [2. Wuzzuf Job Scraper](./wuzzuf_scraper/)
Extracts job titles, companies, and locations from [Wuzzuf](https://wuzzuf.net/) across multiple pages.

**Tech**: requests, BeautifulSoup, pagination  
**Output**: `wuzzuf_jobs.xlsx`

🔗 [View Project →](./wuzzuf_scraper)

---

### ⚽ [3. YallaKora Match Scraper](./yallakora_scraper/)
Scrapes football match info by date (teams, scores, league) from [YallaKora](https://www.yallakora.com/).

**Tech**: requests, BeautifulSoup  
**Output**: `matches.xlsx`

🔗 [View Project →](./yallakora_scraper)

---

## 🔧 Environment Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run any script using:

```bash
python script.py
```

For Selenium-based projects, make sure:
- Chrome is installed
- `webdriver_manager` is used (no manual driver setup required)

---

## 📂 Structure

```
web-scraping-portfolio/
│
├── amazon_scraper/
│   ├── amazon_scraper.py
│   ├── README.md
│   ├── requirements.txt
│   ├── scraper.log
│   ├── .gitignore
│   └── amazon_products.xlsx # after code execution 
│
├── wuzzuf_scraper/
│   ├── wuzzuf_scraper.py
│   ├── README.md
│   ├── requirements.txt
│   ├── .gitignore
│   └── jobs.xlsx # after code execution 
│
├── yallakora_scraper/
│   ├── yallakora_scraper.py
│   ├── README.md
│   ├── requirements.txt
│   ├── .gitignore
│   └── data.xlsx # after code execution 

```
