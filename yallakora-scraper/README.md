# 🏟️ YallaKora Matches Scraper

This Python script scrapes daily football match data from [YallaKora Match Center](https://www.yallakora.com/match-center) and saves it to an Excel file (`data.xlsx`).

---

## 📂 Project Structure

```
yallakora-scraper/
├── script.py
├── requirements.txt
├── README.md
├── .gitignore
└── data.xlsx         # Generated after script runs
```

---

## 📦 Setup Instructions

### 1️⃣ Create & Activate a Virtual Environment

**For Windows (CMD):**

```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux/WSL:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Script

```bash
python script.py
```
---

## 📁 Example `requirements.txt`

```
requests
beautifulsoup4
pandas
lxml
openpyxl
```

---

### 🔁 Optional: Update Requirements

To regenerate `requirements.txt` after adding new libraries:

```bash
pip freeze > requirements.txt
```

---

## 📄 Output

- The script generates an Excel file named `data.xlsx` with match information for the current day.
- Fields include: `Champion`, `Team A`, `Team B`, `Score`, `Time`, and `Date`.

---

## 🛠 Notes

- An active internet connection is required to fetch live data.
- The script may require updates if the website's structure changes.
- Automate daily scraping using `cron` (Linux/macOS) or Windows Task Scheduler (Windows).