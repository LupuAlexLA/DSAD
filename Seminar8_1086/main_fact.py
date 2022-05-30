import factor_analyzer as fact
import pandas as pd
from functii import nan_replace, tabelare_varianta,tabelare_matrice
import numpy as np
from grafice import corelograma, show, plot_componente, harta
from geopandas import GeoDataFrame

t = pd.read_csv("FreeLancer.csv", index_col=1)
nan_replace(t)
variabile_observate = list(t)[2:]

x = t[variabile_observate].values
n, m = np.shape(x)

# Validare model
# Testul Bartlett
bartlett_test = fact.calculate_bartlett_sphericity(x)
# print(bartlett_test)
if bartlett_test[1] > 0.001:
    print("Nu exista factori!")
    exit(0)
# Calcul index KMO
kmo = fact.calculate_kmo(x)
# print(kmo)
kmo_t = pd.DataFrame(
    data={
        "Index KMO": np.append(kmo[0], kmo[1])
    }, index=variabile_observate + ["Total"]
)
print(kmo_t)
corelograma(kmo_t, vmin=0, titlu="Index KMO")
show()
if all(kmo_t["Index KMO"] < 0.6):
    print("Nu exista factori!")
    exit(0)

# Construire model
rotatie = ""
if rotatie == "":
    model_fact = fact.FactorAnalyzer(n_factors=m, rotation=None)
else:
    model_fact = fact.FactorAnalyzer(n_factors=m, rotation=rotatie)
model_fact.fit(x)

# Preluare si afisare rezultate
# Varianta factorilor
alpha = model_fact.get_factor_variance()[0]

etichete_factori = ["F" + str(i + 1) for i in range(m)]
tabel_varianta = tabelare_varianta(alpha, etichete_factori)
print(tabel_varianta)
tabel_varianta.to_csv("Varianta_F_" + rotatie + ".csv")

# Corelatiile variabile-factori
l = model_fact.loadings_
# print(l)
l_t = tabelare_matrice(l,variabile_observate,etichete_factori,"l_"+rotatie+".csv")
corelograma(l_t)

# Calcul scoruri
f = model_fact.transform(x)
f_t = tabelare_matrice(f,t.index,etichete_factori,"f_"+rotatie+".csv")
plot_componente(f_t,"F1","F2","Plot scoruri factoriale",aspect=1)

# calcul comunalitati
h = model_fact.get_communalities()
h_t = pd.DataFrame(
    data={"Comunalitati":h}, index = variabile_observate
)
corelograma(h_t,vmin=0,titlu="Comunalitati")
show()

shp = GeoDataFrame.from_file("World_Simplificat/World.shp")
# print(list(shp),shp,sep="\n")
harta(shp,f[:,:3],"iso_a3",t.index)
