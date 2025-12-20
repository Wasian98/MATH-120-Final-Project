import pandas as pd
import matplotlib.pyplot as plt

def calculate_summary_stats(df, column):
    """Calculate basic summary statistics for a numeric column."""
    return {
        'mean': df[column].mean(),
        'median': df[column].median(),
        'std': df[column].std(),
        'min': df[column].min(),
        'max': df[column].max()
    }

def compare_sentiment(df):
    """Compares critic scores to user scores
    return df.grouby
