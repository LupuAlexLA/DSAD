from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt


class acp():
    def __init__(self, t, variabile=None):
        assert isinstance(t, DataFrame)
        if variabile is None:
            variabile = list(t)
        self.__x = t[variabile].values

    def creare_model(self, std=True, nlib=0):
        if std:
            x_ = (self.__x - np.mean(self.__x, axis=0)) / np.std(self.__x, axis=0)
        else:
            x_ = self.__x - np.mean(self.__x, axis=0)
        n, m = np.shape(self.__x)
        mat = (1 / (n - nlib)) * x_.T @ x_
        valp, vecp = np.linalg.eig(mat)
        k = np.flipud(np.argsort(valp))
        self.__alpha = valp[k]
        self.__a = vecp[:, k]
        self.__c = x_ @ self.__a
        self.etichete_componente = ["comp" + str(i + 1) for i in range(m)]

    def tabelare_varianta(self):
        procent_varianta = self.alpha * 100 / sum(self.alpha)
        tabel_varianta = DataFrame(data={
            "Varianta": self.alpha,
            "Varianta cumulata": np.cumsum(self.alpha),
            "Procent varianta": procent_varianta,
            "Procent cumulat": np.cumsum(procent_varianta)},
            index=self.etichete_componente
        )
        return tabel_varianta

    def plot_varianta(self):
        fig = plt.figure("Plot varianta", figsize=(12, 7))
        ax = fig.add_subplot(1, 1, 1)
        assert isinstance(ax, plt.Axes)
        ax.set_title("Plot varianta componente", fontsize=18, color='b')
        ax.set_xlabel("Componente")
        ax.set_ylabel("Varianta")
        m = len(self.alpha)
        x = np.arange(1, m + 1)
        ax.set_xticks(x)
        ax.plot(x, self.alpha)
        ax.scatter(x, self.alpha, c='r')
        ax.axhline(1, c='g', label="Kaiser")
        ax.legend()
        plt.show()

    @property
    def x(self):
        return self.__x

    @property
    def alpha(self):
        return self.__alpha

    @property
    def a(self):
        return self.__a

    @property
    def c(self):
        return self.__c
