import pandas as pd
from acp import acp
from functii import nan_replace

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



