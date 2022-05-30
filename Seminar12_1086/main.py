import pandas as pd
from pandas import read_csv, DataFrame
from clusterizare import ierarhie
from grafice import show, histograma2

t = read_csv("ADN/ADN_Tari.csv", index_col=0)
variabile = list(t)[1:]
# print(variabile)
clusterizare_ierarhica = ierarhie(t, variabile, "ward")
partitie_o = clusterizare_ierarhica.partitie()
partitii = DataFrame(
    data={
        "Partitia optimala": partitie_o
    }, index=clusterizare_ierarhica.instante
)
numar_clusteri = 5
partitie_5 = clusterizare_ierarhica.partitie("Partitia cu" + str(numar_clusteri) + "clusteri", numar_clusteri)
partitii["Partitie 5 clusteri"] = partitie_5

print(partitii)
partitii.to_csv("partitii.csv")

for variabila in variabile:
    histograma2(t, variabila, partitie_5)

show()
