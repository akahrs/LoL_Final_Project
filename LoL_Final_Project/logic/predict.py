import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def predict_teams(model, X, df):

    # Predict every team's cluster and merge to dataframe

    df_class = df
    df_class = df_class.reset_index(level=0)
    df_class = df_class.rename(columns={"index": "team"})

    predictions = model.predict(X)

    df_class = df_class.join(pd.DataFrame(predictions))
    df_class = df_class.rename(columns={0: "cluster"})

    return df_class


def visualize_predictions(model, X, df, team1, team2):

    # Visualize predicted clusters for two teams

    df_reset = df.copy()
    df_reset.reset_index(inplace=True)

    X_t = pd.DataFrame(X, columns=df.columns)
    X_t["clusters"] = model.labels_

    X_mean = pd.concat([pd.DataFrame(X_t.mean().drop('clusters'), columns=['mean']),
                   X_t.groupby('clusters').mean().T], axis=1)

    X_to_show = X_t.drop(columns=("clusters"))
    X_to_show = X_to_show.T

    sel_teams = df_reset[df_reset["index"].isin([team1, team2])]
    teams = [row["index"] for index, row in sel_teams.iterrows()]
    index_pos = sel_teams.index.tolist()

    X_new_sel = pd.DataFrame(X).loc[[index_pos[0], index_pos[1]],:]

    cluster_colors = ['b', 'g', 'r', 'c', "m", "y", "k", "maroon"]

    class Radar(object):
        def __init__(self, figure, title, labels, rect=None):
            if rect is None:
                rect = [0.05, 0.05, 0.9, 0.9]

            self.n = len(title)
            self.angles = np.arange(0, 360, 360.0/self.n)

            self.axes = [figure.add_axes(rect, projection='polar', label='axes%d' % i) for i in range(self.n)]
            self.ax = self.axes[0]
            self.ax.set_thetagrids(self.angles, labels=title, fontsize=14, backgroundcolor="white",zorder=999) # Feature names
            self.ax.set_yticklabels([])

            for ax in self.axes[1:]:
                ax.xaxis.set_visible(False)
                ax.set_yticklabels([])
                ax.set_zorder(-99)

            for ax, angle, label in zip(self.axes, self.angles, labels):
                ax.spines['polar'].set_color('black')
                ax.spines['polar'].set_zorder(-99)

        def plot(self, values, *args, **kw):
            angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
            values = np.r_[values, values[0]]
            self.ax.plot(angle, values, *args, **kw)
            kw['label'] = '_noLabel'
            self.ax.fill(angle, values,*args,**kw)

    fig = plt.figure(figsize=(8, 8))
    no_features = model.n_features_in_
    radar = Radar(fig, list(df.columns), np.unique(model.labels_))
    location = 0

    for k in model.predict(X_new_sel):
        #cluster_data = X_mean[k].values.tolist()
        cluster_data = X_to_show[index_pos[location]].values.tolist()
        radar.plot(cluster_data,  '-', lw=2, color=cluster_colors[k], alpha=0.7, label=f"{teams[location]}: Cluster {k}")
        location += 1

    radar.ax.legend(loc="upper right")
    radar.ax.set_title("Playstyle cluster(s) for selected teams", size=22, pad=60)

    return plt.show()

def get_teams_diff(df, team1, team2):

    # Get values and differences for two selected teams

    df_new = df.copy()
    df_new.reset_index(inplace=True)
    df_new = df_new = df_new.rename({"index": "team"}, axis=1)

    sel_teams = df_new[df_new["team"].isin([team1, team2])]
    diff_btw_teams = sel_teams.drop(columns=["team"])
    diff_btw_teams = diff_btw_teams.T

    index_num1 = df_new.index[df_new["team"] == team1][0]
    index_num2 = df_new.index[df_new["team"] == team2][0]
    diff_btw_teams["Difference"] = diff_btw_teams[index_num1] - diff_btw_teams[index_num2]

    diff_btw_teams = diff_btw_teams.rename({index_num1: team1, index_num2: team2}, axis=1)

    return diff_btw_teams.round(decimals=2)
