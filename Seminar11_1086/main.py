import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from functii import tabelare_matrice, acuratete
from grafice import scatter2d, show

set_antrenare = pd.read_csv("Hernia/hernia.csv", index_col=0)

variabile = list(set_antrenare)
variabile_predictor = variabile[:-1]
variabila_tinta = variabile[len(variabile) - 1]
instante = list(set_antrenare.index)
# print(variabile_predictor,variabila_tinta)
x = set_antrenare[variabile_predictor].values
y = set_antrenare[variabila_tinta].values

predictie_set_antrenare = pd.DataFrame(
    data={
        variabila_tinta: y
    }, index=instante
)

# Construire model liniar de clasificare
model_lda = LinearDiscriminantAnalysis()
model_lda.fit(x, y)

# Aplicare model pe setul de antrenare si evaluare model
clase = model_lda.classes_
q = len(clase)
m = len(variabile_predictor)
numar_axe = min(q - 1, m)
z = model_lda.transform(x)
etichete_discriminatori = ["z" + str(i + 1) for i in range(numar_axe)]
t_z = tabelare_matrice(z, instante, etichete_discriminatori, "z.csv")
g = model_lda.means_
zg = model_lda.transform(g)
etichete_centrii = ["g" + str(i + 1) for i in range(numar_axe)]
# print(zg)
t_zg = tabelare_matrice(zg, clase, etichete_centrii, "zg.csv")
if numar_axe > 1:
    scatter2d(t_z, "z1", "z2", t_zg, "g1", "g2", y, clase)
clasificare_lda = model_lda.predict(x)
predictie_set_antrenare["Predictie LDA"] = clasificare_lda
erori_lda = predictie_set_antrenare[clasificare_lda != y]
erori_lda.to_csv("Erori_lda.csv")
print(erori_lda)

acuratete_lda = acuratete(y, clasificare_lda, clase)
acuratete_lda[0].to_csv("Mat_conf_lda.csv")
print(acuratete_lda[0])
print("Acuratete globala LDA:", acuratete_lda[1])
print("Acuratete medie LDA:", acuratete_lda[2])
print("Index Cohen-Kappa LDA:", acuratete_lda[3])

# Aplicare model pe setul de testare-aplicare
set_aplicare_testare = pd.read_csv("Hernia/hernia_test.csv", index_col=0)
x_ = set_aplicare_testare[variabile_predictor].values
clasificare_lda_test = model_lda.predict(x_)
set_aplicare_testare["Predictie LDA"] = clasificare_lda_test

show()

# Model Bayesian
model_bayes = GaussianNB()
model_bayes.fit(x, y)

clasificare_bayes = model_bayes.predict(x)
predictie_set_antrenare["Predictie Bayes"] = clasificare_bayes
erori_bayes = predictie_set_antrenare[clasificare_bayes != y]
erori_bayes.to_csv("Erori_bayes.csv")
print(erori_bayes)

acuratete_bayes = acuratete(y, clasificare_bayes, clase)
acuratete_bayes[0].to_csv("Mat_conf_bayes.csv")
print(acuratete_bayes[0])
print("Acuratete globala Bayes:", acuratete_bayes[1])
print("Acuratete medie Bayes:", acuratete_bayes[2])
print("Index Cohen-Kappa Bayes:", acuratete_bayes[3])

clasificare_bayes_test = model_bayes.predict(x_)
set_aplicare_testare["Predictie Bayes"] = clasificare_bayes_test

predictie_set_antrenare.to_csv("Predictii_set_antrenare.csv")
set_aplicare_testare.to_csv("Predictii.csv")
