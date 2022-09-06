from venv import create
from LoL_Final_Project.data.retrieve_data import get_local_data
from LoL_Final_Project.data.prepare_data import filter_major_leagues, aggregate_team_data, create_agg_dataframe
from LoL_Final_Project.logic.preprocess import preprocess
from LoL_Final_Project.logic.model import fit_model, visualize_model
from LoL_Final_Project.logic.predict import predict_teams, visualize_predictions

def get_data():

    df = get_local_data()
    df = filter_major_leagues(df)
    df = create_agg_dataframe(df)

    print("Data retrieved and prepared!")

    return df

def preprocess_run_model(df = get_data()):

    X = preprocess(df)

    model = fit_model(X)

    print("Model run and fitted!")

    return (X, model)

def visualize_model():

    model = preprocess_run_model()[1]

    X = preprocess_run_model()[0]

    df = get_data()

    return visualize_model(model, X, df)

def visualize_predictions(model = preprocess_run_model()[1], X = preprocess_run_model()[0], df = get_data()):

    # df_classified = predict_teams(model, X, df)

    return visualize_predictions(model, X, df)
