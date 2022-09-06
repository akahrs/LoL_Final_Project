import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def predict_teams(model, X, df):

    # Predict every team's cluster and merge to dataframe

    df_class = df
    df_class = df_class.reset_index(level=0)
    df_class = df_class.rename(columns={"index": "team"})

    predictions = model.predict(X)

    df_class = df_class.join(pd.DataFrame(predictions))
    df_class = df_class.rename(columns={0: "cluster"})

    return df_class

def visualize_predictions(model, X, df):

    # Visualize predicted clusters for two teams

    X_t = pd.DataFrame(X, columns=df.columns)
    X_t["clusters"] = model.labels_

    X_mean = pd.concat([pd.DataFrame(X_t.mean().drop('clusters'), columns=['mean']),
                   X_t.groupby('clusters').mean().T], axis=1)

    sel_teams = df[df.index.isin(["G2 Esports", "Top Esports"])]
    teams = [row["team"] for index, row in sel_teams.iterrows()]
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

    fig = plt.figure(figsize=(12, 12))
    no_features = model.n_features_in_
    radar = Radar(fig, list(model.columns), np.unique(model.labels_))
    location = 0

    for k in model.predict(X_new_sel):
        cluster_data = X_mean[k].values.tolist()
        radar.plot(cluster_data,  '-', lw=2, color=cluster_colors[k], alpha=0.7, label=f"{teams[location]}: Cluster {k}")
        location += 1

    radar.ax.legend(loc="upper right")
    radar.ax.set_title("Playstyle cluster(s) for selected teams", size=22, pad=60)

    return plt.show()
