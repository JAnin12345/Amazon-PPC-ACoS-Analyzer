# Amazon PPC ACoS Analyzer 📊

An end-to-end data analytics project that automates the analysis of Amazon Sponsored Products Search Term Reports. This project cleans raw advertising data, calculates key PPC KPIs using Python, stores processed data in SQL, and visualizes campaign performance through an interactive Power BI dashboard.

---

# 🚀 Project Overview

The Amazon PPC ACoS Analyzer helps Amazon sellers and PPC specialists quickly identify:

- Winning keywords
- High ACoS search terms
- Negative keyword opportunities
- Low CTR campaigns
- High ROAS keywords
- Campaign performance trends

Instead of manually analyzing thousands of search terms, this project automates the complete workflow.

---

# 🏗️ Project Architecture

```
                  Amazon Search Term Report (.xlsx)
                               │
                               ▼
                     Excel Data Validation
              (Missing Values • Duplicates • Formatting)
                               │
                               ▼
                    Python Data Cleaning (Pandas)
                               │
                               ▼
                      KPI Calculations
        CTR • CPC • CVR • ACoS • ROAS • TACoS
                               │
                               ▼
                 Search Term Classification
       Winner • Watch • Waste • Negate Keywords
                               │
                               ▼
                  Export Clean Dataset (.xlsx)
                               │
                               ▼
                    PostgreSQL Database
                               │
                               ▼
                      SQL Analysis Queries
                               │
                               ▼
                    Power BI Dashboard
                               │
                               ▼
                   Business Recommendations
```

---

# 📂 Directory Structure

```text
Amazon-PPC-ACoS-Analyzer/
│
├── data/
│   ├── raw/
│   │   └── Amazon_Search_Term_Report.xlsx
│   │
│   └── processed/
│       ├── cleaned_data.xlsx
│       ├── keyword_summary.xlsx
│       └── classified_keywords.xlsx
│
├── python/
│   ├── main.py
│   ├── data_cleaning.py
│   ├── validation.py
│   ├── kpi_calculator.py
│   ├── classifier.py
│   ├── charts.py
│   ├── export_excel.py
│   └── utils.py
│
├── sql/
│   ├── create_database.sql
│   ├── create_tables.sql
│   ├── import_data.sql
│   ├── views.sql
│   └── analysis_queries.sql
│
├── powerbi/
│   ├── Amazon_PPC_Dashboard.pbix
│   └── Dashboard.pdf
│
├── output/
│   ├── Amazon_PPC_Report.xlsx
│   ├── Top_Winners.xlsx
│   ├── Negative_Keywords.xlsx
│   └── Dashboard_Summary.pdf
│
├── screenshots/
│   ├── workflow.png
│   ├── gui.png
│   ├── dashboard.png
│   ├── sql_results.png
│   └── excel_report.png
│
├── docs/
│   ├── Project_Report.pdf
│   ├── Data_Dictionary.pdf
│   └── Presentation.pptx
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🛠️ Technology Stack

| Tool | Purpose |
|-------|---------|
| Excel | Raw data validation |
| Python | Data cleaning & KPI calculations |
| Pandas | Data transformation |
| NumPy | Numerical calculations |
| PostgreSQL | Database storage |
| SQL | Business analysis |
| Power BI | Dashboard & visualization |
| Git | Version control |
| GitHub | Portfolio hosting |

---

# 📊 KPI Calculations

| KPI | Formula |
|------|----------|
| CTR | Clicks ÷ Impressions |
| CPC | Spend ÷ Clicks |
| CVR | Orders ÷ Clicks |
| ACoS | Spend ÷ Sales |
| ROAS | Sales ÷ Spend |
| TACoS | Spend ÷ Total Sales |

---

# 📈 Workflow

### 1. Data Validation (Excel)

- Verify column names
- Remove duplicates
- Check missing values
- Format numeric columns
- Standardize dates

Output:

```
Raw Data
      ↓
Validated Data
```

---

### 2. Data Cleaning (Python)

- Handle NaN values
- Remove blank search terms
- Convert data types
- Normalize text
- Remove invalid rows

Output:

```
cleaned_data.xlsx
```

---

### 3. KPI Calculation

Python calculates:

- CTR
- CPC
- CVR
- ACoS
- ROAS
- TACoS

---

### 4. Search Term Classification

Business Rules

| Condition | Classification |
|------------|---------------|
| ACoS ≤ 30% | Winner |
| 30% < ACoS ≤ 40% | Watch |
| ACoS > 40% | Waste |
| Spend > $10 & Sales = 0 | Negate |
| Clicks > 20 & Orders = 0 | Negate |

---

### 5. SQL Analysis

Example analyses:

- Top 20 profitable keywords
- Highest ACoS keywords
- Campaign performance
- Search term performance
- Match type analysis
- Monthly trends
- Branded vs Generic keywords

---

### 6. Power BI Dashboard

Dashboard includes:

- KPI Cards
- Total Spend
- Total Sales
- Average ACoS
- Average ROAS
- CTR
- Conversion Rate
- Top Winning Keywords
- High ACoS Keywords
- Campaign Performance
- Match Type Performance
- Search Term Analysis
- Spend vs Sales
- Monthly Trends
- Interactive Filters

---

# 📁 Expected Outputs

```
Amazon_PPC_Report.xlsx

Sheets
------
✔ Cleaned Data
✔ KPI Summary
✔ Winners
✔ Watch
✔ Waste
✔ Negative Keywords
✔ Campaign Summary
```

---

# 📷 Project Screenshots

```
screenshots/

GUI.png

PowerBI.png

Excel_Report.png

SQL_Query.png

Workflow.png
```

---

# 🎯 Business Insights

This project helps Amazon sellers:

- Reduce wasted advertising spend
- Improve campaign profitability
- Identify high-converting keywords
- Discover negative keywords
- Increase ROAS
- Lower ACoS
- Make data-driven bidding decisions

---

# 🚀 Future Improvements

- Tkinter desktop GUI
- Drag-and-drop Excel upload
- Automated Excel report generation
- Streamlit web application
- Machine Learning keyword clustering
- Amazon Ads API integration
- Scheduled ETL pipeline
- Docker deployment
- Cloud database integration
- Real-time Power BI refresh

---

# 👤 Author

**Alvin Vela**

**Amazon PPC Specialist | Data Analyst | Python | SQL | Power BI**

## Skills

- Amazon PPC Optimization
- Python
- SQL
- Power BI
- Excel
- Data Cleaning
- Data Visualization
- ETL
- Business Intelligence

---

## ⭐ Project Highlights

- End-to-end data analytics pipeline
- Real Amazon PPC dataset
- Automated KPI calculations
- SQL business analysis
- Interactive Power BI dashboard
- Portfolio-ready GitHub project
- Demonstrates data engineering, analytics, and business intelligence skills
