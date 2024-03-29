import os
import webbrowser

import markdown
from PySide2.QtCore import Qt
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QMainWindow

from views import product_details_window


class ProductDetailsWindowController(QMainWindow):
    """
    Controller of the product details window
    """

    def __init__(self, parent: QMainWindow, product_details: dict):
        """
        Initialize a ProductDetailsWindowController object

        :param parent: The parent window of the product details window
        :param product_details: The details of the product to display
        """
        super(ProductDetailsWindowController, self).__init__(parent)
        self.product_details = product_details

        self.setWindowModality(Qt.NonModal)

        self.ui = product_details_window.Ui_MainWindow()
        self.ui.setupUi(self)

        food = self.product_details

        self.setWindowTitle(food["food_name"])

        self.ui.btn_openfoodfacts.clicked.connect(self.open_web_page)

        brands_list_content = "<b>Marques : </b>"

        for brand in food["brands"]:
            brands_list_content += f"{brand['brand_name']}, "

        self.ui.lbl_brands.setText(brands_list_content[:-2])

        stores_list_content = "<ul>"

        for store in food["stores"]:
            stores_list_content += f"<li>{store['store_name']}</li>"

        stores_list_content += "</ul>"

        self.ui.lbl_stores.setText(stores_list_content)

        self.ui.lbl_ingredients.setText(markdown.markdown(food["ingredients"]))

        palm_oil_presence = food["ingredients_from_palm_oil_n"] > 0

        self.ui.lbl_palm_oil.setStyleSheet(
            "* { background-color: red; color: white; padding: 3 px; }"
            if palm_oil_presence else
            "* { background-color: green; color: white; padding: 3 px; }"
        )

        self.ui.lbl_palm_oil.setText(
            "Contient de l'huile de palme"
            if palm_oil_presence else
            "Ne contient pas d'huile de palme"
        )

        self.ui.lbl_allergens.setText(markdown.markdown(food["allergens"]) if food["allergens"] else "<i>Aucun</i>")

        if food["energy_unit"] == "kcal":
            kj = round(food["energy_100g"] * 4.18, 1)
            energy_string = f"{food['energy_100g']} kcal ({kj} kj)"
        else:
            kcal = round(food["energy_100g"] / 4.18, 1)
            energy_string = f"{kcal} kcal ({food['energy_100g']} kj)"

        html_spaces = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"

        nutriments = [
            ["<b>Energie</b>", energy_string],
            ["<b>Glucides</b>", f"{food['carbohydrates_100g']} g"],
            [f"{html_spaces}Sucres", f"{food['sugars_100g']} g"],
            ["<b>Matières grasses</b>", f"{food['fat_100g']} g"],
            [f"{html_spaces}Acides gras saturés", f"{food['saturated_fat_100g']} g"],
            ["<b>Sel</b>", f"{food['salt_100g']} g"],
            [f"{html_spaces}Sodium", f"{food['sodium_100g']} g"],
            ["<b>Fibres</b>", f"{food['fiber_100g']} g"],
            ["<b>Protéines</b>", f"{food['proteins_100g']} g"]
        ]

        nutriments_table_content = "<style>td { padding: 3px; }</style>"

        nutriments_table_content += "<table width=100% border=1 cellspacing=0 cellpadding=0>"

        for nutriment in nutriments:
            nutriments_table_content += "<tr>"
            for column in nutriment:
                nutriments_table_content += "<td>"
                nutriments_table_content += str(column)
                nutriments_table_content += "</td>"
            nutriments_table_content += "</tr>"

        nutriments_table_content += "</table>"

        self.ui.lbl_nutriments.setText(nutriments_table_content)

        current_directory = os.path.dirname(__file__)
        filename = os.path.join(current_directory, "..", "..", "assets", f"nutriscore_{food['nutrition_grade']}.png")

        image = QImage(filename)
        pix_map = QPixmap()
        pix_map.convertFromImage(image.scaledToHeight(100, Qt.SmoothTransformation))

        self.ui.lbl_nutriscore.setPixmap(pix_map)
        self.ui.lbl_nutriscore_number.setText(f"<b>Indice NUTRI-SCORE:</b> {food['nutriscore']}")

    def open_web_page(self) -> None:
        """
        Open the full OpenFoodFacts product details page on default web browser
        """
        webbrowser.open(f"https://fr.openfoodfacts.org/produit/{self.product_details['food_code']}")  # Go to example.com
