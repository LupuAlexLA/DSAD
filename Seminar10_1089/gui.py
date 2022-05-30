# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(752, 592)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 391, 521))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 361, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.buton_citire1 = QPushButton(self.verticalLayoutWidget)
        self.buton_citire1.setObjectName(u"buton_citire1")
        self.buton_citire1.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.buton_citire1)

        self.text_fisier1 = QLineEdit(self.verticalLayoutWidget)
        self.text_fisier1.setObjectName(u"text_fisier1")

        self.verticalLayout.addWidget(self.text_fisier1)

        self.buton_citire2 = QPushButton(self.verticalLayoutWidget)
        self.buton_citire2.setObjectName(u"buton_citire2")
        self.buton_citire2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.buton_citire2)

        self.text_fisier2 = QLineEdit(self.verticalLayoutWidget)
        self.text_fisier2.setObjectName(u"text_fisier2")

        self.verticalLayout.addWidget(self.text_fisier2)

        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 150, 361, 71))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.combo_index = QComboBox(self.formLayoutWidget)
        self.combo_index.setObjectName(u"combo_index")
        self.combo_index.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.combo_index)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.combo_tinta = QComboBox(self.formLayoutWidget)
        self.combo_tinta.setObjectName(u"combo_tinta")
        self.combo_tinta.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.combo_tinta)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 230, 361, 271))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.list_variabile = QListWidget(self.verticalLayoutWidget_2)
        self.list_variabile.setObjectName(u"list_variabile")
        self.list_variabile.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.list_variabile)

        self.buton_selectie = QPushButton(self.verticalLayoutWidget_2)
        self.buton_selectie.setObjectName(u"buton_selectie")
        self.buton_selectie.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.buton_selectie)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(430, 40, 291, 501))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.buton_acuratete = QPushButton(self.groupBox_2)
        self.buton_acuratete.setObjectName(u"buton_acuratete")
        self.buton_acuratete.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.buton_acuratete)

        self.buton_matconf = QPushButton(self.groupBox_2)
        self.buton_matconf.setObjectName(u"buton_matconf")
        self.buton_matconf.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.buton_matconf)

        self.buton_clasificare1 = QPushButton(self.groupBox_2)
        self.buton_clasificare1.setObjectName(u"buton_clasificare1")
        self.buton_clasificare1.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.buton_clasificare1)

        self.text_out = QTextEdit(self.groupBox_2)
        self.text_out.setObjectName(u"text_out")
        self.text_out.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")

        self.verticalLayout_4.addWidget(self.text_out)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 752, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Citire date", None))
        self.buton_citire1.setText(QCoreApplication.translate("MainWindow", u"Citire date de antrenare", None))
        self.buton_citire2.setText(QCoreApplication.translate("MainWindow", u"Citire date de aplicare", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Variabila index:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Variabila tinta:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Variabile predictor:", None))
        self.buton_selectie.setText(QCoreApplication.translate("MainWindow", u"Selectie generala", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Clasificarea liniara", None))
        self.buton_acuratete.setText(QCoreApplication.translate("MainWindow", u"Acuratete model", None))
        self.buton_matconf.setText(QCoreApplication.translate("MainWindow", u"Acuratete clase", None))
        self.buton_clasificare1.setText(QCoreApplication.translate("MainWindow", u"Clasificare set antrenare", None))
    # retranslateUi

