import pandas as pd
import numpy as np


def analyze_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)

    #count rows
    print(f"Total records: {len(df)}")

    #get column names
    print(f"Columns: {df.columns.tolist()}")

    #check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Basic statistics
    print("Basic Statistics:")
    print(df.describe())

    # Distribution of prices
    print("\nPrice Distribution:")
    print(df['Price'].value_counts().head(10))

    # Correlation between price and mileage
    correlation = df['Price'].corr(df['Mileage'])
    print(f"\nCorrelation between Price and Mileage: {correlation:.2f}")

    # Average price by year
    avg_price_by_year = df.groupby('Year')['Price'].mean()
    print("\nAverage Price by Year:")
    print(avg_price_by_year)

if __name__ == "__main__":
    analyze_data("data/vehicles.csv")
