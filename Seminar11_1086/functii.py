import numpy as np
import pandas as pd
import sklearn.metrics as metrics

def tabelare_matrice(x, nume_linii=None, nume_coloane=None, out=None):
    t = pd.DataFrame(x, nume_linii, nume_coloane)
    if out is not None:
        t.to_csv(out)
    return t

def acuratete(y,predictie,clase):
    matrice_confuzie = metrics.confusion_matrix(y,predictie)
    t_mat_conf = tabelare_matrice(matrice_confuzie,clase,clase)
    t_mat_conf["Acuratete"] = np.diagonal(matrice_confuzie)*100/np.sum(matrice_confuzie,axis=1)
    n = len(y)
    acuratete_globala = sum(np.diagonal(matrice_confuzie))*100/n
    index_cohen_kappa = metrics.cohen_kappa_score(y,predictie)
    acuratete_medie = np.mean(t_mat_conf["Acuratete"])
    return t_mat_conf,acuratete_globala,acuratete_medie,index_cohen_kappa



