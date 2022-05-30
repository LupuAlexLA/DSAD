import scipy.stats as stts
import numpy as np
import pandas as pd


def test_independenta(tabel, variabile):
    q = len(variabile)
    chi2 = np.zeros(shape=(q, q))
    p_values = np.zeros(shape=(q, q))
    # Frecvente efective si teoretice
    t = dict()
    t_ = dict()
    for i in range(q):
        v1 = variabile[i]
        for j in range(i + 1, q):
            v2 = variabile[j]
            tabel_contingenta = pd.crosstab(tabel[v1], tabel[v2])
            # print(v1+":"+v2,tabel_contingenta,sep="\n")
            test = stts.chi2_contingency(tabel_contingenta)
            # print(test)
            chi2[i, j] = test[0]
            p_values[i, j] = test[1]
            chi2[j, i] = chi2[i, j]
            p_values[j, i] = p_values[i, j]
            t[v1 + ":" + v2] = tabel_contingenta
            t_[v1 + ":" + v2] = test[3]
    return chi2, p_values, t, t_


def analiza_bivariata(t, t_):
    n = np.sum(t)
    # Frecvente relative reale
    f = t / n
    # Frecvente relative teoretice
    f_ = t_ / n
    # Frecventele linie
    f_lin = np.sum(f, axis=1)
    f_col = np.sum(f, axis=0)
    # Matrice de abateri standard
    r = (f - f_) / np.sqrt(f_)
    # Aplicare SVD
    u, s, vt = np.linalg.svd(r, full_matrices=False)
    l = np.diag(1 / np.sqrt(f_lin)) @ u @ np.diag(s)
    c = np.diag(1 / np.sqrt(f_col)) @ vt.T @ np.diag(s)
    return u, vt.T, l, c, s * s
