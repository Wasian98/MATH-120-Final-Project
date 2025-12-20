import pandas as pd
import os

def load_raw_data(file_path):
    """Load raw data from CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Cleans up and keeps specific columns"""
    cols_to_keep = ["name", "release_date", "price", "metacritic_score", "genres", "estimated_owners", "average_playtime_forever", "average_playtime_2weeks", "num_reviews_total"]
    df = df[cols_to_keep]
    # Remove titles with metacritic scores of 0
    df = df[df["metacritic_score"] != 0]
    return df

def save_cleaned_data(df, output_path):
    """Save cleaned data to CSV file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
