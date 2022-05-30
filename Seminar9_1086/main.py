import numpy as np

from functii import *
from sklearn.cross_decomposition import CCA
from sklearn.preprocessing import normalize
from grafice import *

t = pd.read_csv("Freelancer/FreeLancer.csv", index_col=1)
nan_replace(t)
variabile = list(t)
var1 = variabile[2:10]
var2 = variabile[10:]
instante = list(t.index)
# print(var1,var2,sep="\n")

x = t[var1].values
y = t[var2].values
n, p = x.shape
q = y.shape[1]
m = min(p, q)

# Construire model
model_cca = CCA(m)
model_cca.fit(x, y)

# Rezultate
# Calcul scoruri
z, u = model_cca.transform(x, y)
# print(z,u)
normalize(z, axis=0, copy=False)
normalize(u, axis=0, copy=False)

etichete_z = ["z" + str(i + 1) for i in range(m)]
etichete_u = ["u" + str(i + 1) for i in range(m)]
etichete_rad = ["root" + str(i + 1) for i in range(m)]

t_z = tabelare_matrice(z, instante, etichete_z, "z.csv")
t_u = tabelare_matrice(u, instante, etichete_u, "u.csv")

r = np.diagonal(np.corrcoef(z, u, rowvar=False)[:m, m:])
# print(r)
r2 = r * r
p_values = test_bartlett(r2, n, p, q, m)
# print(p_values)
t_root = pd.DataFrame(
    data={
        "R": r,
        "R2": r2,
        "P_Values": np.round(p_values, 3)
    }, index=etichete_rad
)
print(t_root)
t_root.to_csv("radacini_canonice.csv")
n_rad = np.where(p_values > 0.01)[0][0]

for i in range(1, n_rad):
    scatter2d(t_z, "z1", etichete_z[i], t_u, "u1", etichete_u[i])

r_xz = np.corrcoef(x, z, rowvar=False)[:p, p:]
r_yu = np.corrcoef(y, u, rowvar=False)[:q, q:]
t_r_xz = tabelare_matrice(r_xz, var1, etichete_z, "rxz.csv")
t_r_yu = tabelare_matrice(r_yu, var2, etichete_u, "ryu.csv")
for i in range(1, n_rad):
    plot_corelatii(t_r_xz, "z1", etichete_z[i], t_r_yu, "u1", etichete_u[i])

show()
