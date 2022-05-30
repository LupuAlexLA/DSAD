import pandas as pd
import functii
import numpy as np
import grafice

tabel = pd.read_csv("IAC.csv",index_col=0)
variabile = list(tabel)
nr_variabile = len(variabile)

# Test independenta
chi2, p_values, dict_t, dict_t_ = functii.test_independenta(tabel,variabile)
tabel_chi2 = pd.DataFrame(chi2,variabile,variabile)
tabel_chi2.to_csv("Chi2.csv")
tabel_p_values = pd.DataFrame( np.round(p_values,5),variabile,variabile )
tabel_p_values.to_csv("p_values.csv")
test = tabel_p_values<0.01
test.to_csv("test.csv")

# Analiza bivariata
for k1 in range(nr_variabile):
    v1 = variabile[k1]
    for k2 in range(k1+1,nr_variabile):
        v2 = variabile[k2]
        if p_values[k1,k2]<0.01:
            t_contingenta = dict_t[v1+":"+v2]
            print("Analiza "+v1+":"+v2)
            print("Tabel contingenta:",t_contingenta,sep="\n")
            profile_linie = list(t_contingenta.index)
            profile_coloana = list(t_contingenta.columns)
            p = len(profile_linie)
            q = len(profile_coloana)
            m = min(p,q)
            u, v, l, c, alpha = functii.analiza_bivariata(
                t_contingenta.values,
                dict_t_[v1+":"+v2]
            )
            procent_inertie = np.round( alpha*100/sum(alpha),2 )
            procent_inertie_cumulat = np.cumsum(procent_inertie)
            etichete_axe = ["a"+str(i+1) for i in range(m)]
            tabel_inertie = pd.DataFrame(
                data={
                    "Inertie":np.append(alpha,sum(alpha)),
                    "Procent inertie":np.append(procent_inertie,sum(procent_inertie)),
                    "Procent cumulat":np.append(procent_inertie_cumulat,100)
                }, index=[ etichete_axe + ["Total"]]
            )
            tabel_inertie.to_csv("Inertie_"+str(k1)+"_"+str(k2)+".csv")

            grafice.plot_profile(u,v,profile_linie,profile_coloana,
                                 v1,v2,procent_inertie)
            grafice.show()




