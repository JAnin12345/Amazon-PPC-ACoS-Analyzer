# Amazon PPC ACoS Analyzer 📊

An end-to-end data engineering and analytics pipeline designed to ingest raw Amazon Search Term Reports, clean and process the data, perform SQL-based performance analysis, and visualize key advertising metrics like ACoS (Advertising Cost of Sales) and ROAS (Return on Ad Spend) in Power BI.

---

## 🏗️ Project Architecture & Directory Structure

Here is how the project files are organized. The workflow moves from raw data ingestion to SQL storage, Python-based KPI calculations, and finally to visual reporting.

```text
Amazon-PPC-ACoS-Analyzer/
│
├── data/
│   ├── raw/                  # Original Amazon Search Term reports (.xlsx)
│   └── processed/            # Cleaned, structured outputs ready for analysis
│
├── sql/
│   ├── create_database.sql   # Database schemas and tables
│   ├── import_data.sql       # Script to load processed data into SQL
│   └── analysis_queries.sql  # Deep-dive queries (ACoS, target keywords, etc.)
│
├── python/
│   ├── main.py               # Main pipeline execution script
│   ├── data_cleaning.py      # Standardizes raw inputs & handles missing values
│   ├── kpi_calculator.py     # Calculates ACoS, ROAS, CTR, and conversion rates
│   ├── classifier.py         # Categorizes search terms (e.g., Branded vs. Generic)
│   └── export_excel.py       # Formats and exports analysis back to Excel
│
├── powerbi/
│   └── Amazon_PPC_Dashboard.pbix  # Interactive Power BI report file
│
├── screenshots/              # Images used in this README
│   ├── workflow.png
│   ├── dashboard.png
│   └── powerbi.png
│
├── output/                   # Final business-ready Excel reports
│   └── Amazon_PPC_Report.xlsx
│
├── README.md
├── requirements.txt          # Python dependencies
└── LICENSE



Negative targeting: Search terms with $10+ in Spend and exactly 0 Sales.
Keyword Harvesting: High-performing search terms with Sales > 0 and ACoS < 30% (ready to be graduated to exact match keywords).
Optimize keyword: Active search terms with Sales > 0 and ACoS ≥ 30% (needs bid or placement adjustments).
Under Threshold: Terms that have spent less than $10 and have no sales yet (not enough data to call waste




Tech Stack
Tool	Purpose
Excel	Initial data validation, cleaning, and data preparation
SQL Data storage, querying, aggregation, and historical reporting
Python (Pandas, NumPy, OpenPyXL)	KPI calculations, automation, classification, and report generation
Power BI	Interactive dashboards, visualizations, and business insights
GitHub	Version control, portfolio presentation, and documentation

Project Summary

This project demonstrates an end-to-end Amazon PPC analytics pipeline. Amazon Search Term Reports are first validated in Excel, stored and queried in SQL, processed in Python to calculate advertising KPIs (ACoS, ROAS, CTR, CPC, and CVR) and classify keywords into Winner, Watch, and Waste categories. The processed data is then visualized in Power BI through interactive dashboards that help advertisers identify profitable keywords, reduce wasted ad spend, and make data-driven campaign optimization decisions. This workflow highlights practical skills in Excel, SQL, Python, Power BI, and GitHub while addressing a real-world Amazon advertising business problem.


Objective
Amazon sellers generate thousands of search terms from advertising campaigns. 
Manually analyzing these reports is time-consuming and makes it difficult to identify profitable keywords, wasted ad spend, and optimization opportunities.

Goal
Develop an automated Amazon PPC Analyzer that:
Calculates key advertising KPIs
Identifies high-performing keywords
Detects wasted advertising spend
Recommends negative keywords
Generates interactive dashboards for decision-making
