import pandas as pd
import os

def validate_victim_data(df):
    """
    Validates the 'Vict Sex' and 'Vict Age' columns in the provided DataFrame.
    - 'Vict Sex' should only contain 'M' or 'F' and not be null.
    - 'Vict Age' should be between 1 and 100 and not be null.
    """
    invalid_sex = df[(df['Vict Sex'].isnull()) | (~df['Vict Sex'].isin(['M', 'F']))]
    invalid_age = df[(df['Vict Age'].isnull()) | (df['Vict Age'] < 1) | (df['Vict Age'] > 100)]
    
    print(f"Invalid 'Vict Sex' entries: {len(invalid_sex)}")
    print(f"Invalid 'Vict Age' entries: {len(invalid_age)}")

if __name__ == "__main__":
    # Locate the CSV file
    curr_dir = os.path.dirname(__file__)
    file_path = os.path.join(curr_dir, 'Crime_Data_from_2020_to_Present.csv')
    
    # Read the CSV
    df = pd.read_csv(file_path)
    
    # Validate the data
    validate_victim_data(df)