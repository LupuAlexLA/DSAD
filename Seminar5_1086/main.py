import pandas as pd
from functii import nan_replace
from functii import citireTabelaDb
from grafice import grafic_linii, \
    scatter2d, scatter3d,\
    histograma,histograma2

t = citireTabelaDb("db5.db", "Teritorial")
nan_replace(t)
variabile = list(t)
variabile1 = variabile[:4]
variabile2 = variabile[4:]
print(variabile1, variabile2, sep="\n")
t.index = t["Indicativ"]

# Grafic linii
grafic_linii(t, ["PIB", "ExecBVenituri", "ExecBSubventii", "Export"],
             eticheta_x="Judete")

# Grafic tip scatter

scatter2d(t, 6, 14)
scatter3d(t, 6, 14, 16)

# Histograma
histograma(t,variabile2,"Teritorial")
histograma2(t,["PIB","Export","ExecBVenituri"])
