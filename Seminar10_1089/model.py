import numpy as np
import pandas as pd

from gui import *
import controller
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import sklearn.metrics as metrics


class Frame(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model_creat = False
        self.buton_citire1.clicked.connect(self.citire1)
        self.buton_citire2.clicked.connect(self.citire2)
        self.buton_selectie.clicked.connect(lambda x: controller.selectie_generala(self.list_variabile))
        self.buton_acuratete.clicked.connect(self.acuratete)
        self.buton_matconf.clicked.connect(self.matconf)
        self.buton_clasificare1.clicked.connect(self.clasificare1)

    def clasificare1(self):
        if not self.model_creat:
            self.creare_model()
        t_clasificare = pd.DataFrame(
            data={
                self.variabila_tinta:self.y,
                "Predictie LDA":self.y_predict
            }, index=self.instante
        )
        t_err = t_clasificare[ self.y!=self.y_predict ]
        dialog1 = controller.DialogNonModal(self,t_clasificare,titlu="Clasificare in setul de antrenare")
        dialog1.show()
        dialog2 = controller.DialogNonModal(self,t_err,titlu="Erori in clasificare")
        dialog2.show()


    def matconf(self):
        if not self.model_creat:
            self.creare_model()
        t_matconf = pd.DataFrame(self.mat_conf,self.clase,self.clase)
        t_matconf["Acuratete"] = np.diagonal(self.mat_conf)*100/np.sum(self.mat_conf,axis=1)
        dialog = controller.DialogNonModal(self,t_matconf,titlu="Matrice confuzie")
        dialog.show()



    def acuratete(self):
        if not self.model_creat:
            self.creare_model()
        n = len(self.t)
        acuratete_globala = sum(np.diagonal(self.mat_conf)) * 100 / n
        self.text_out.append("Acuratete globala:" + str(acuratete_globala))
        self.text_out.append("Index Kappa-Cohen:" + str(self.index_cohen))

    def citire1(self):
        rez = controller.citire_fisier_variabile(self.combo_index, self.list_variabile)
        if rez is not None:
            self.t = rez[0]
            self.text_fisier1.setText(rez[1])
            controller.init_combo(self.combo_tinta, list(self.t))

    def citire2(self):
        rez = controller.citire_fisier()
        if rez is not None:
            self.t_ = rez[0]
            self.text_fisier2.setText(rez[1])

    def creare_model(self):
        variabila_index = self.combo_index.currentText()
        self.t.index = self.t[variabila_index]
        self.variabile_predictor = controller.selectii_lista(self.list_variabile)
        self.variabila_tinta = self.combo_tinta.currentText()
        self.instante = list(self.t.index)
        x = self.t[self.variabile_predictor].values
        self.y = self.t[self.variabila_tinta].values

        model_lda = LinearDiscriminantAnalysis()
        model_lda.fit(x, self.y)

        self.clase = model_lda.classes_
        self.z = model_lda.transform(x)
        self.g = model_lda.means_
        self.zg = model_lda.transform(self.g)
        self.y_predict = model_lda.predict(x)
        self.mat_conf = metrics.confusion_matrix(self.y, self.y_predict)
        self.index_cohen = metrics.cohen_kappa_score(self.y, self.y_predict)

        self.model_creat = True
