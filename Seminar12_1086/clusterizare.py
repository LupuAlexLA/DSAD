import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage
from grafice import dendrograma


class ierarhie():
    def __init__(self, t, variabile=None, metoda="single"):
        if variabile is None:
            variabile = list(variabile)
        self.x = t[variabile].values
        self.metoda = metoda
        self.instante = list(t.index)
        self.h = linkage(self.x, method=metoda)
        print(self.h)

    def partitie(self, titlu="PLot ierarhie", nr_clusteri=None):
        p = self.h.shape[0]
        if nr_clusteri is None:
            k_dif_max = np.argmax(self.h[1:, 2] - self.h[:(p - 1), 2])
            nr_clusteri = p - k_dif_max
        else:
            k_dif_max = p - nr_clusteri
        threshold = (self.h[k_dif_max, 2] + self.h[k_dif_max + 1, 2]) / 2
        dendrograma(self.h, self.instante, titlu, threshold)
        n = p + 1
        c = np.arange(n)
        for i in range(n - nr_clusteri):
            k1 = self.h[i, 0]
            k2 = self.h[i, 1]
            c[c == k1] = n + i
            c[c == k2] = n + i
        coduri = pd.Categorical(c).codes
        return np.array(["c" + str(cod + 1) for cod in coduri])
