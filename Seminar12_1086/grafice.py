import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram


def dendrograma(h, instante, titlu, threshold=None):
    fig = plt.figure(titlu, figsize=(15, 9))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontsize=18, color='c')
    dendrogram(h, labels=instante, ax=ax, color_threshold=threshold)


def histograma2(t, var, partitia, titlu="Histograme"):
    titlu = titlu + "-" + var
    fig = plt.figure(titlu, figsize=(14, 8))
    assert isinstance(fig, plt.Figure)
    fig.suptitle(titlu, fontsize=18, color='b')
    v = np.unique(partitia)
    q = len(v)
    axe = fig.subplots(1, q, sharey=True)
    for i in range(q):
        axa = axe[i]
        assert isinstance(axa, plt.Axes)
        axa.set_xlabel(v[i])
        x = t[partitia == v[i]][var].values
        axa.hist(x=x, rwidth=0.9, range=(t[var].min(), t[var].max()))


def show():
    plt.show()
