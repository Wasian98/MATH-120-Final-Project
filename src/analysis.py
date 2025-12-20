import pandas as pd
import matplotlib.pyplot as plt

def summary_stats(df):
    """Summary stats for Steam data"""
    return {
        'Highest Playtime': df["average_playtime_forever"].max(),
        'Biggest Genre': df["genres"].count(),
        'Highest Metacritic Score': df["metacritic_score"].max(),
        'Highest Amount of Reviews': df["num_reviews_total"].max(),
        'Highest Estimated Player Count': df["estimated_owners"].max()
    }

def highest_played_games(df):
    """Sorts by the highest average playtime for an individual game and retains other relevant information"""
    a = (
    steam_clean
    .groupby("name", as_index=False)
    .agg(
        genres=("genres", lambda x: ", ".join(sorted(set(x)))),
        playtime=("average_playtime_forever", "mean"),
        metacritic_score=("metacritic_score", "mean"),
        player_reviews=("num_reviews_total", "mean")
    )
    .sort_values(by="playtime", ascending=False)
    )
    return a

def stats_by_genre(df):
    """Counts the number of entries per genre while checking the average metacritic score and average playtime"""
    b = (
    df
    .groupby("genres")
    .agg(
        genre_count=("genres", "size"),
        meta_score=("metacritic_score", "mean"),
        average_playtime=("average_playtime_forever", "mean")
    )
    .query("genre_count > 10 and meta_score > 0")
    )
    return b
