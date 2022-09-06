import pandas as pd

def filter_major_leagues (df):

    # Select major national leagues and filter data for those

    ImportantLEAGUES=['LPL', 'NA LCS', 'EU LCS', 'LEC', 'LMS', 'LCK', 'LCS', 'PCS']

    df_major = df[df["league"].isin(ImportantLEAGUES)]
    df_major = df_major.drop(columns=["Unnamed: 0"])

    return df_major

def aggregate_team_data(df_major, team, n_games):

    # Aggregate each teams' data for given number of games

    df_major_agg = df_major[df_major["teamname"] == team].tail(n_games).groupby("teamname").aggregate(
    {"gamelength": "mean",
        "result": "mean",
        "teamdeaths": "mean",
        "firstblood": "mean",
        "team kpm": "mean",
        "dpm": "mean",
        "vspm": "mean",
        "earned gpm": "mean",
        "monsterkills": "mean",
        "structures": "mean",
        "big_monsters_taken": "mean"})

    return df_major_agg

def create_agg_dataframe(df_major_agg):

    # Created aggregated dataframe for each team

    df_new = pd.DataFrame(columns=aggregate_team_data(df_major_agg, "T1", 10).columns)

    for i in list(df_major_agg["teamname"].unique()):
        df_new = df_new.append(aggregate_team_data(df_major_agg, i, 10))

    df_new["teamsdeaths_pm"] = df_new["teamdeaths"] / (df_new["gamelength"] / 60)
    df_new["monsterkills_pm"] = df_new["monsterkills"] / (df_new["gamelength"] / 60)
    df_new["structures_pm"] = df_new["structures"] / (df_new["gamelength"] / 60)
    df_new["big_monsters_taken_pm"] = df_new["big_monsters_taken"] / (df_new["gamelength"] / 60)

    df_new = df_new.drop(columns=["teamdeaths", "monsterkills", "structures", "big_monsters_taken"])

    return df_new
