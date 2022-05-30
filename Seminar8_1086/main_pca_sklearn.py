import pandas as pd
from functii import nan_replace,tabelare_matrice
from sklearn.decomposition import PCA
from grafice import plot_componente,show

t = pd.read_csv("FreeLancer.csv",index_col=1)
nan_replace(t)
variabile_observate = list(t)[2:]

model_acp = PCA()
model_acp.fit(t[variabile_observate])

alpha = model_acp.explained_variance_
# print(alpha)
a = model_acp.components_
c = model_acp.transform(t[variabile_observate])


c_t = tabelare_matrice(c,t.index,
                       ["comp"+str(i+1) for i in range(len(alpha))],"c_.csv")
plot_componente(c_t,"comp1","comp2")

show()


