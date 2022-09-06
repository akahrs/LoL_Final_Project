from sklearn.cluster import AffinityPropagation
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fit_model(X):

    # Fit model and print out number of clusters found

    af = AffinityPropagation(preference=-15, random_state=0).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_

    n_clusters_ = len(cluster_centers_indices)

    print("Estimated number of clusters: %d" % n_clusters_)

    return af

def visualize_model(model, X, df):

    # Visualize model clustering across all features by taking features' mean for each cluster

    X_t = pd.DataFrame(X, columns=df.columns)
    X_t["clusters"] = model.labels_

    X_mean = pd.concat([pd.DataFrame(X_t.mean().drop('clusters'), columns=['mean']),
                   X_t.groupby('clusters').mean().T], axis=1)

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

    for k in range(0,len(np.unique(model.labels_))):
        cluster_data = X_mean[k].values.tolist()
        radar.plot(cluster_data,  '-', lw=2, color=cluster_colors[k], alpha=0.7, label='Cluster {}'.format(k))

    radar.ax.legend(loc="upper right")
    radar.ax.set_title("Playstyle cluster characteristics: Feature means per cluster", size=22, pad=60)

    return plt.show()
