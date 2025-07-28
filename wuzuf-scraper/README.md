# 💼 Wuzzuf Job Scraper

This Python script scrapes job listings from [Wuzzuf.net](https://wuzzuf.net/) based on a search keyword (default: `python`). It extracts job title, location, company, job type, and work style for the first 3 pages of results.

---

## 📂 Project Structure

```
wuzzuf-scraper/
├── script.py
├── requirements.txt
├── README.md
├── .gitignore
└── jobs.xlsx # Generated output file
```

---

## ⚙️ Features

- Scrapes job listings for a given keyword
- Supports multi-page scraping (currently 3 pages)
- Saves results to Excel (`jobs.xlsx`)
- Handles partial data gracefully with `zip_longest`

---

## 📦 Setup Instructions

### 1️⃣ Create & Activate a Virtual Environment

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

### 2️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Script

```bash
python script.py
```

---

## 📁 Example `requirements.txt`

```
requests
beautifulsoup4
lxml
pandas
openpyxl
```

---

## 📄 Output

The script generates an Excel file named `jobs.xlsx` with the following columns:

- **title**: Job title
- **location**: Job location
- **company**: Company name
- **type**: Job type (e.g., Full Time)
- **place**: Work style (e.g., On-site, Remote)