# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/product_details_dialog.ui',
# licensing of 'views/product_details_dialog.ui' applies.
#
# Created: Mon Oct 28 09:20:43 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 700)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 474, 674))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_nutriments = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_nutriments.sizePolicy().hasHeightForWidth())
        self.lbl_nutriments.setSizePolicy(sizePolicy)
        self.lbl_nutriments.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbl_nutriments.setObjectName("lbl_nutriments")
        self.gridLayout_4.addWidget(self.lbl_nutriments, 10, 0, 1, 1)
        self.lbl_allergens = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_allergens.sizePolicy().hasHeightForWidth())
        self.lbl_allergens.setSizePolicy(sizePolicy)
        self.lbl_allergens.setWordWrap(True)
        self.lbl_allergens.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbl_allergens.setObjectName("lbl_allergens")
        self.gridLayout_4.addWidget(self.lbl_allergens, 5, 0, 1, 1)
        self.lbl_ingredients = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ingredients.sizePolicy().hasHeightForWidth())
        self.lbl_ingredients.setSizePolicy(sizePolicy)
        self.lbl_ingredients.setWordWrap(True)
        self.lbl_ingredients.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbl_ingredients.setObjectName("lbl_ingredients")
        self.gridLayout_4.addWidget(self.lbl_ingredients, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 12, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 7, 0, 1, 1)
        self.lbl_palm_oil = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_palm_oil.setStyleSheet("")
        self.lbl_palm_oil.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_palm_oil.setObjectName("lbl_palm_oil")
        self.gridLayout_4.addWidget(self.lbl_palm_oil, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.lbl_nutriscore = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_nutriscore.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nutriscore.setObjectName("lbl_nutriscore")
        self.gridLayout_4.addWidget(self.lbl_nutriscore, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 3, 0, 2, 1)
        self.lbl_nutriscore_number = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_nutriscore_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nutriscore_number.setObjectName("lbl_nutriscore_number")
        self.gridLayout_4.addWidget(self.lbl_nutriscore_number, 9, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.lbl_nutriments.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))
        self.lbl_allergens.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))
        self.lbl_ingredients.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "<b>Valeurs nutritionnelles pour 100g</b>", None, -1))
        self.lbl_palm_oil.setText(QtWidgets.QApplication.translate("Dialog", "Contient de l\'huile de palme", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "<b>Ingrédients</b>", None, -1))
        self.lbl_nutriscore.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "<b>Allergènes</b>", None, -1))
        self.lbl_nutriscore_number.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))
