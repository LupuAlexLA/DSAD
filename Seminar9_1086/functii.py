import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
import scipy.stats as stts


def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    nume_variabile = list(t.columns)
    for v in nume_variabile:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                modulul = t[v].mode()[0]
                t[v].fillna(modulul, inplace=True)


def tabelare_matrice(x, nume_linii=None, nume_coloane=None, out=None):
    t = pd.DataFrame(x, nume_linii, nume_coloane)
    if out is not None:
        t.to_csv(out)
    return t


def test_bartlett(r2, n, p, q, m):
    v = 1 - r2
    chi2 = (-n + 1 + (p + q + 1) / 2) * np.log(np.flip(np.cumprod(np.flip(v))))
    dof = [(p - k + 1) * (q - k + 1) for k in range(1, m + 1)]
    p_values = 1 - stts.chi2.cdf(chi2, dof)
    return p_values
