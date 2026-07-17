# Amazon-PPC-ACoS-Analyzer
Python tool for analyzing Amazon PPC search term reports and optimizing ACoS.using other tools such as 

Amazon-PPC-ACoS-Analyzer/
│
├── data/
│   ├── raw/
│   │     amazon_search_term_report.xlsx
│   ├── processed/
│   │     processed_amazon_ppc.xlsx
│
├── sql/
│   ├── create_database.sql
│   ├── import_data.sql
│   ├── analysis_queries.sql
│
├── python/
│   ├── main.py
│   ├── data_cleaning.py
│   ├── kpi_calculator.py
│   ├── classifier.py
│   ├── export_excel.py
│
├── powerbi/
│   ├── Amazon_PPC_Dashboard.pbix
│
├── screenshots/
│   ├── dashboard.png
│   ├── powerbi.png
│   ├── workflow.png
│
├── output/
│   ├── Amazon_PPC_Report.xlsx
│
├── README.md
├── requirements.txt
└── LICENSE

Tech Stack
Tool	Purpose
Excel	Initial data validation, cleaning, and data preparation
SQL (MySQL/PostgreSQL)	Data storage, querying, aggregation, and historical reporting
Python (Pandas, NumPy, OpenPyXL)	KPI calculations, automation, classification, and report generation
Power BI	Interactive dashboards, visualizations, and business insights
GitHub	Version control, portfolio presentation, and documentation
Project Summary

This project demonstrates an end-to-end Amazon PPC analytics pipeline. Amazon Search Term Reports are first validated in Excel, stored and queried in SQL, processed in Python to calculate advertising KPIs (ACoS, ROAS, CTR, CPC, and CVR) and classify keywords into Winner, Watch, and Waste categories. The processed data is then visualized in Power BI through interactive dashboards that help advertisers identify profitable keywords, reduce wasted ad spend, and make data-driven campaign optimization decisions. This workflow highlights practical skills in Excel, SQL, Python, Power BI, and GitHub while addressing a real-world Amazon advertising business problem.


Excel SQL Power BI


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
