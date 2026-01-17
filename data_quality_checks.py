import pandas as pd

# Load KPMG dataset
file_path = "../KPMG_tast1.xlsx"
xls = pd.ExcelFile(file_path)

# Load sheets
customer_df = pd.read_excel(xls, "CustomerDemographic")
transaction_df = pd.read_excel(xls, "Transactions")

def data_quality_report(df, name):
    print(f"\nData Quality Report: {name}")
    print("-" * 40)
    print("Missing values:")
    print(df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

# Run checks
data_quality_report(customer_df, "Customer Demographic")
data_quality_report(transaction_df, "Transactions")
