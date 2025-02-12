# Import necessary libraries
import pandas as pd  # For handling data
import numpy as np  # For numerical operations

# Load the dataset (replace 'healthcare_dataset.csv' with the actual file name)
df = pd.read_csv("healthcare_dataset.csv")

# Display first few rows to understand structure
print("First 5 Rows of the Dataset:")
print(df.head())

# Check column names and data types
print("\nDataset Information:")
print(df.info())
# Check for missing values

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Get summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Check for duplicate rows
print("\nNumber of Duplicates:")
print(df.duplicated().sum())


# Handle missing values
# Fill numerical columns with the median
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical columns with the most frequent value (mode)
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Standardize text format (e.g., gender column)
if 'gender' in df.columns:
    df['gender'] = df['gender'].str.lower().str.strip()

# Convert date columns to datetime format (modify column name as needed)
date_columns = ["appointment_date", "birth_date"]  # Change based on dataset
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Remove duplicate rows
df = df.drop_duplicates()

# Save the cleaned dataset for Power BI
df.to_csv("cleaned_healthcare_data.csv", index=False)

print("\nData Cleaning Completed. Cleaned dataset saved as 'cleaned_healthcare_data.csv'.")

