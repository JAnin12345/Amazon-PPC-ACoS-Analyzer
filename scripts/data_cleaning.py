"""
Amazon PPC ACoS Analyzer
Data Cleaning Script

Functions:
- Remove duplicates
- Handle missing values
- Rename columns
- Export cleaned dataset
"""

import pandas as pd
import os


def clean_amazon_data(input_file, output_file):
    # Load data
    df = pd.read_excel(input_file)

    print("Original Data:")
    print(df.head())

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with all missing values
    df = df.dropna(how="all")

    # Fill missing numeric values with 0
    numeric_columns = df.select_dtypes(include=["number"]).columns
    df[numeric_columns] = df[numeric_columns].fillna(0)

    # Fill missing text values
    text_columns = df.select_dtypes(include=["object"]).columns
    df[text_columns] = df[text_columns].fillna("Unknown")

    # Rename Amazon PPC columns
    column_mapping = {
        "Customer Search Term": "Search_Term",
        "Impressions": "Impressions",
        "Clicks": "Clicks",
        "Spend": "Spend",
        "7 Day Total Sales": "Sales",
        "7 Day Total Orders (#)": "Orders",
        "Total Advertising Cost of Sales (ACOS)": "ACOS",
        "7 Day Total Advertising Cost of Sales (ACOS)": "ACOS"
    }

    df = df.rename(columns=column_mapping)

    # Save cleaned file
    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True
    )

    df.to_csv(output_file, index=False)

    print("Cleaning completed!")
    print(f"Saved file: {output_file}")


if __name__ == "__main__":

    input_path = "data/raw/search_term_report.xlsx"

    output_path = "data/processed/cleaned_search_terms.csv"

    clean_amazon_data(
        input_path,
        output_path
    )
