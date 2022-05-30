import pandas as pd
from acp import acp
from functii import nan_replace,tabelare_matrice
from grafice import corelograma, plot_corelatii, plot_componente, show
import numpy as np

t = pd.read_csv("FreeLancer.csv",index_col=1)
nan_replace(t)
variabile_observate = list(t)[2:]

model = acp(t,variabile_observate)
model.creare_model()
# print(model.alpha)
tabel_varianta = model.tabelare_varianta()
tabel_varianta.to_csv("Varianta.csv")
print(tabel_varianta)
model.plot_varianta()
r_x_c = model.r_x_c
# print(r_x_c)
r_x_c_t = tabelare_matrice(r_x_c,variabile_observate,
                 model.etichete_componente,
                 "corelatii_factoriale.csv")
print(r_x_c_t)
corelograma(r_x_c_t)
plot_corelatii(r_x_c_t,"comp1","comp2")
plot_corelatii(r_x_c_t,"comp1","comp3")
c = model.c
c_t = tabelare_matrice(c,t.index,model.etichete_componente,"c.csv")
plot_componente(c_t,"comp1","comp2",aspect=1)

# Calcul cosinusuri
c2 = c*c
cosin = np.transpose(c2.T/np.sum(c2,axis=1))
cosin_t = tabelare_matrice(cosin,t.index,
                           model.etichete_componente,"cosin.csv")

r_x_c2 = r_x_c*r_x_c
comm = np.cumsum(r_x_c2,axis=1)
comm_t = tabelare_matrice(comm,variabile_observate,
                 model.etichete_componente,
                 "comm.csv")
corelograma(comm_t,vmin=0,titlu="Comunalitati")

show()