import pandas as pd
import os

def calculate_age_statistics(df):
    """
    Calculates the mean and median of the 'Vict Age' column in the provided DataFrame.
    """
    mean_age = df['Vict Age'].mean()
    median_age = df['Vict Age'].median()
    
    print(f"Mean Age: {mean_age}")
    print(f"Median Age: {median_age}")

if __name__ == "__main__":
    # Locate the CSV file
    curr_dir = os.path.dirname(__file__)
    file_path = os.path.join(curr_dir, 'Crime_Data_from_2020_to_Present.csv')
    
    # Read the CSV
    df = pd.read_csv(file_path)
    
    # Calculate statistics
    calculate_age_statistics(df)