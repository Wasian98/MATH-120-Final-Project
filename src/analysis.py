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

def meta_genre_check(df):
    """Sorts by the highest metacritic score and checks the genre count for those scores"""
    a = (
    df
    .groupby("genres")
    .agg(
        genre_count=("genres", "size"),
        meta_score=("metacritic_score", "mean"),
    )
    .query("genre_count > 10 and meta_score > 0")
    .sort_values(by="meta_score", ascending=False)
    )
    return a

def genre_meta_check(df):
    """Sorts by the highest genre count and checks what the metacritic score is"""
    b = (
    def
    .groupby("genres")
    .agg(
        genre_count=("genres", "size"),
        meta_score=("metacritic_score", "mean"),
    )
    .query("genre_count > 10 and meta_score > 0")
    .sort_values(by="genre_count", ascending=False)
    )
    return b
