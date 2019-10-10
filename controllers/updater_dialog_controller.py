import typing

import PySide2
from PySide2.QtCore import QJsonDocument, QAbstractTableModel, Qt, QUrl, QItemSelection
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PySide2.QtWidgets import QDialog, QProgressDialog, QAbstractItemView, QHeaderView

from views import updater_dialog


class UpdaterDialogController(QDialog):
    def __init__(self):
        super(UpdaterDialogController, self).__init__()
        self.progress = QProgressDialog("Récupération des catégories...", "", 0, 0, self)
        self.progress.setFixedWidth(300)

        # noinspection PyTypeChecker
        self.progress.setCancelButton(None)

        self.fetch_categories_manager = QNetworkAccessManager()
        self.fetch_categories_manager.finished.connect(self.handle_api_categories)

        self.ui = updater_dialog.Ui_Dialog()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui.btn_load_list.clicked.connect(self.fetch_categories)

    def fetch_categories(self):
        self.progress.open()

        request = QNetworkRequest(QUrl("https://fr.openfoodfacts.org/categories.json"))
        self.fetch_categories_manager.get(request)

    def handle_api_categories(self, reply: QNetworkReply):
        er = reply.error()

        if er == QNetworkReply.NoError:
            bytes_string = reply.readAll()

            json = QJsonDocument.fromJson(bytes_string)
            obj = json.object()["tags"]

            categories_gt_5000 = []

            for item in obj:
                if item["products"] >= 5000:
                    categories_gt_5000.append(Item(item["name"], item["products"]))

            categories_gt_5000.sort(key=lambda x: x.name)

            table_model = MyTableModel(self, categories_gt_5000, ["Catégorie", "Nombre de produits"])

            self.ui.table_categories.setModel(table_model)
            self.ui.table_categories.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.table_categories.setSelectionMode(QAbstractItemView.SingleSelection)
            self.ui.table_categories.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.ui.table_categories.setSortingEnabled(True)
            self.ui.table_categories.sortByColumn(0, Qt.AscendingOrder)

            selection_model = self.ui.table_categories.selectionModel()
            selection_model.selectionChanged.connect(self.lol)

        else:
            print("Error occured: ", er)
            print(reply.errorString())

        self.progress.close()

    def lol(self, selected: QItemSelection, deselected: QItemSelection):
        for lol in self.ui.table_categories.selectionModel().selectedRows():
            print(lol.row())


class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, my_list, my_header):
        QAbstractTableModel.__init__(self, parent)
        self.my_list: [Item] = my_list
        self.header = my_header

    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int:
        return len(self.my_list)

    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int:
        return 2

    def data(self, index: PySide2.QtCore.QModelIndex, role: int = ...) -> typing.Any:
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None

        if index.column() == 0:
            return self.my_list[index.row()].name
        elif index.column() == 1:
            return self.my_list[index.row()].products

    def headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...) -> typing.Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[section]
        return None

    def sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = ...):
        self.layoutAboutToBeChanged.emit()

        def test(elem: Item):
            if column == 0:
                return elem.name
            elif column == 1:
                return elem.products

        self.my_list = sorted(self.my_list, key=test)
        if order == Qt.DescendingOrder:
            self.my_list.reverse()

        self.layoutChanged.emit()


class Item:
    def __init__(self, name, products):
        self.name: str = name
        self.products: int = products
