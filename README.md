# 🧮 Analytics on UN Population

## 🎯 Aim
To convert raw open data — country and year-wise population estimates — into visual charts that tell meaningful stories about population growth patterns.

---

## 📊 Data Source
The dataset used in this project is sourced from:
👉 https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv

NOTE You have to construct data for countries in ASEAN and SAARC, references follow 

### Reference Lists:
- **ASEAN Countries:** https://en.wikipedia.org/wiki/ASEAN  
- **SAARC Countries:** https://en.wikipedia.org/wiki/South_Asian_Association_for_Regional_Cooperation

---

## 🧠 Project Overview

This project involves analyzing and visualizing UN population data for ASEAN and SAARC countries.  
You’ll read CSV data, process it using Python, and plot charts using **Matplotlib**.

The project demonstrates:
- Data reading and filtering from CSV files  
- Data aggregation (like summing populations for regions)  
- Visualization with **Matplotlib**

---
# Analytics on UN Population

## ⚙️ How to Run This Project

### 🧾 1. Clone the Repository

```bash
git clone <_repo_link>
cd <repo_folder_name>
```

---

### 🐍 2. Set Up Python Virtual Environment

It’s recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

---

### 📥 3. Install Required Packages

Install the Python libraries needed for this project:

```bash
pip install -r requirements.txt
```

---

### 🗂 4. Download the Data

Download the raw population CSV from the UN Population dataset.

---

### 📝 5. Run the Python Scripts

All code is in Python. To process the data and generate charts, run the Python scripts.

```bash
python main.py
```

---

### ✅ 6. Linting

Check code quality using pylint:

```bash
pylint filename.py
```

---

## 📈 Plots Generated

### 1️⃣ India Population Over Years – Bar Plot

Displays India’s population growth over time.

---

### 2️⃣ ASEAN Population (2014) – Bar Chart

Shows population of ASEAN countries for the year **2014**.

---

### 3️⃣ Total SAARC Population Over Years – Bar Chart

Plots the **sum** of populations of all SAARC countries over the years.

---

### 4️⃣ Grouped Bar Chart – ASEAN Population vs. Years

Displays population of all **10 ASEAN countries** from **2004–2014**, grouped by year.

---

## 🧩 Technologies Used

* **Python 3**
* **Matplotlib** – for plotting

---

## ✅ Code Quality

This project follows Python best practices and uses **pylint** for linting.








