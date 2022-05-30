import matplotlib.pyplot as plt
import numpy as np


def scatter2d(t_z, varz1, varz2, t_u, varu1, varu2, titlu="Plot scoruri", aspect=1):
    fig = plt.figure(figsize=(12, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(varz1 + "/" + varu1, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(varz2 + "/" + varu2, fontdict={"fontsize": 12, "color": "b"})
    ax.set_aspect(aspect)
    ax.scatter(t_z[varz1], t_z[varz2], c="r", label="Spatiul X")
    ax.scatter(t_u[varu1], t_u[varu2], c="b", label="Spatiul Y")
    for i in range(len(t_z)):
        ax.text(t_z[varz1].iloc[i], t_z[varz2].iloc[i], t_z.index[i])
        ax.text(t_u[varu1].iloc[i], t_u[varu2].iloc[i], t_u.index[i])
    ax.legend()


def plot_corelatii(t_z, varz1, varz2, t_u, varu1, varu2, titlu="Plot corelatii", aspect=1):
    fig = plt.figure(figsize=(9, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(varz1 + "/" + varu1, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(varz2 + "/" + varu2, fontdict={"fontsize": 12, "color": "b"})
    ax.set_aspect(aspect)
    u = np.arange(0, np.pi * 2, 0.01)
    ax.plot(np.cos(u), np.sin(u))
    ax.plot(0.7 * np.cos(u), 0.7 * np.sin(u), color='orange')
    ax.axvline(0)
    ax.axhline(0)
    ax.scatter(t_z[varz1], t_z[varz2], c="r", label="Spatiul X")
    ax.scatter(t_u[varu1], t_u[varu2], c="b", label="Spatiul Y")
    for i in range(len(t_z)):
        ax.text(t_z[varz1].iloc[i], t_z[varz2].iloc[i], t_z.index[i])
    for i in range(len(t_u)):
        ax.text(t_u[varu1].iloc[i], t_u[varu2].iloc[i], t_u.index[i])
    ax.legend()


def show():
    plt.show()
