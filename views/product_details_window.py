# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/product_details_window.ui',
# licensing of 'views/product_details_window.ui' applies.
#
# Created: Mon Nov  4 08:54:45 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 460, 620))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_allergens = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_allergens.sizePolicy().hasHeightForWidth())
        self.lbl_allergens.setSizePolicy(sizePolicy)
        self.lbl_allergens.setWordWrap(True)
        self.lbl_allergens.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbl_allergens.setObjectName("lbl_allergens")
        self.gridLayout_4.addWidget(self.lbl_allergens, 8, 0, 1, 1)
        self.lbl_nutriscore_number = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_nutriscore_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nutriscore_number.setObjectName("lbl_nutriscore_number")
        self.gridLayout_4.addWidget(self.lbl_nutriscore_number, 12, 0, 1, 1)
        self.lbl_stores = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_stores.setObjectName("lbl_stores")
        self.gridLayout_4.addWidget(self.lbl_stores, 2, 0, 1, 1)
        self.lbl_ingredients = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ingredients.sizePolicy().hasHeightForWidth())
        self.lbl_ingredients.setSizePolicy(sizePolicy)
        self.lbl_ingredients.setWordWrap(True)
        self.lbl_ingredients.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbl_ingredients.setObjectName("lbl_ingredients")
        self.gridLayout_4.addWidget(self.lbl_ingredients, 4, 0, 1, 1)
        self.lbl_nutriments = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_nutriments.sizePolicy().hasHeightForWidth())
        self.lbl_nutriments.setSizePolicy(sizePolicy)
        self.lbl_nutriments.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbl_nutriments.setObjectName("lbl_nutriments")
        self.gridLayout_4.addWidget(self.lbl_nutriments, 13, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 15, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 10, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.lbl_palm_oil = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_palm_oil.setStyleSheet("")
        self.lbl_palm_oil.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_palm_oil.setObjectName("lbl_palm_oil")
        self.gridLayout_4.addWidget(self.lbl_palm_oil, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)
        self.lbl_nutriscore = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_nutriscore.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nutriscore.setObjectName("lbl_nutriscore")
        self.gridLayout_4.addWidget(self.lbl_nutriscore, 11, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 6, 0, 2, 1)
        self.lbl_brands = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_brands.setWordWrap(True)
        self.lbl_brands.setObjectName("lbl_brands")
        self.gridLayout_4.addWidget(self.lbl_brands, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lbl_allergens.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.lbl_nutriscore_number.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.lbl_stores.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.lbl_ingredients.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.lbl_nutriments.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Valeurs nutritionnelles pour 100g</b>", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Magasins</b>", None, -1))
        self.lbl_palm_oil.setText(QtWidgets.QApplication.translate("MainWindow", "Contient de l\'huile de palme", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Ingrédients</b>", None, -1))
        self.lbl_nutriscore.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Allergènes</b>", None, -1))
        self.lbl_brands.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))

