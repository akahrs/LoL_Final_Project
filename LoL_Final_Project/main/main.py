from venv import create
from LoL_Final_Project.data.retrieve_data import get_local_data
from LoL_Final_Project.data.prepare_data import filter_major_leagues, aggregate_team_data, create_agg_dataframe
from LoL_Final_Project.logic.preprocess import preprocess
from LoL_Final_Project.logic.model import fit_model, visualize_model
from LoL_Final_Project.logic.predict import predict_teams, visualize_predictions, get_teams_diff
import streamlit as st

def get_data():

    df = get_local_data()
    df = filter_major_leagues(df)
    df = create_agg_dataframe(df)

    print("Data retrieved and prepared!")

    return df

def preprocess_run(df):

    X = preprocess(df)

    model = fit_model(X)

    print("Model run and fitted!")

    return (X, model)

def visualize(model, X, df):

    # model = preprocess_run()[1]

    # X = preprocess_run()[0]

    # df = get_data()

    return visualize_model(model, X, df)

def visualize2(model, X, df, team1, team2):

    # df_classified = predict_teams(model, X, df)

    # model = preprocess_run()[1]

    # X = preprocess_run()[0]

    # df = get_data()

    return visualize_predictions(model, X, df, team1=team1, team2=team2)

def get_team_values(model, team1, team2):

    return get_teams_diff(model, team1, team2)
