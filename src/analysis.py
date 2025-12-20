import pandas as pd
import matplotlib.pyplot as plt

def summary_stats(df):
    """Summary stats for Steam data with corresponding game names"""
    
    max_playtime_idx = df["average_playtime_forever"].idxmax()
    max_meta_idx = df["metacritic_score"].idxmax()
    max_reviews_idx = df["num_reviews_total"].idxmax()
    max_owners_idx = df["estimated_owners"].idxmax()

    # flatten multi-genre rows safely
    genre_counts = (
        df["genres"]
        .dropna()
        .str.split(";")
        .explode()
        .str.strip()
        .value_counts()
    )
    
    return {
        "Highest Playtime": (
            df.loc[max_playtime_idx, "name"],
            int(df["average_playtime_forever"].max())
        ),
        "Highest Metacritic Score": (
            df.loc[max_meta_idx, "name"],
            int(df["metacritic_score"].max())
        ),
        "Highest Amount of Reviews": (
            df.loc[max_reviews_idx, "name"],
            int(df["num_reviews_total"].max())
        ),
        "Highest Estimated Player Count": (
            df.loc[max_owners_idx, "name"],
            df.loc[max_owners_idx, "estimated_owners"]
        ),
        "Biggest Genre": (
            genre_counts.idxmax(),
            genre_counts.max()
        )
    }

def highest_played_games(df):
    """Sorts by the highest average playtime for an individual game and retains other relevant information"""
    a = (
    df
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
