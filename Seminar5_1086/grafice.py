import matplotlib.pyplot as plt

# Grafic linii
import pandas as pd


def grafic_linii(t, vars, titlu="Grafic linii", eticheta_x="X"):
    fig = plt.figure(figsize=(12, 7))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu)
    ax.set_xlabel(eticheta_x)
    for v in vars:
        ax.plot(t[v], label=v)
    ax.legend()
    plt.show()


# Grafic scatterplot
def scatter2d(t, k1=0, k2=1, titlu="Scatter2D", aspect='auto'):
    if isinstance(t, pd.DataFrame):
        x = t.values
        coloane = list(t)
        linii = list(t.index)
        n, m = x.shape
    else:
        x = t
        n, m = x.shape
        coloane = ["X" + str(i) for i in range(1, m + 1)]
        linii = [str(i) for i in range(1, n + 1)]
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_aspect(aspect)
    ax.set_title(titlu, fontsize=16, color='b')
    ax.set_xlabel(coloane[k1], fontsize=12, color='b')
    ax.set_ylabel(coloane[k2], fontsize=12, color='b')
    ax.scatter(x[:, k1], x[:, k2], c='r')
    for i in range(n):
        ax.text(x[i, k1], x[i, k2], linii[i])
    plt.show()


def scatter3d(t, k1=0, k2=1, k3=2, titlu="Scatter 3D"):
    if isinstance(t, pd.DataFrame):
        x = t.values
        coloane = list(t)
        linii = list(t.index)
        n, m = x.shape
    else:
        x = t
        n, m = x.shape
        coloane = ["X" + str(i) for i in range(1, m + 1)]
        linii = [str(i) for i in range(1, n + 1)]
    fig = plt.figure(figsize=(8, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 18, "color": 'b'})
    ax.set_xlabel(coloane[k1], fontsize=12, color='b')
    ax.set_ylabel(coloane[k2], fontsize=12, color='b')
    ax.set_zlabel(coloane[k3], fontsize=12, color='b')
    ax.scatter(x[:, k1], x[:, k2], x[:, k3], c='r')
    for i in range(n):
        ax.text(x[i, k1], x[i, k2], x[i, k3], linii[i])
    plt.show()

# Grafic histograma
def histograma(t,vars,titlu = "Grafic histograma"):
    for v in vars:
        fig = plt.figure( figsize=(10,6) )
        ax = fig.add_subplot(1,1,1)
        assert isinstance(ax,plt.Axes)
        ax.set_title(titlu,fontdict={"fontsize":16,"color":'b'})
        ax.set_xlabel(v,fontsize = 14)
        ax.set_ylabel("Frecventa",fontsize=12)
        ax.hist(t[v],color='g',rwidth = 0.9)
    plt.show()

def histograma2(t,vars,titlu="Histograme"):
    fig = plt.figure(figsize=(14, 8))
    assert isinstance(fig,plt.Figure)
    fig.suptitle(titlu,fontsize=18,color='b')
    q = len(vars)
    axe = fig.subplots(1,q,sharey=True)
    for i in range(q):
        axa = axe[i]
        assert isinstance(axa,plt.Axes)
        axa.set_xlabel(vars[i])
        x = t[vars[i]].values
        axa.hist(x ,rwidth=0.9, range=( min(x),max(x)) )
    plt.show()
