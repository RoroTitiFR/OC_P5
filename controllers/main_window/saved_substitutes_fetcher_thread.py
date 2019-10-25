from PySide2.QtCore import QThread, Signal

from models.database.models import Substitute, Food


class SavedSubstitutesFetcherThread(QThread):
    result = Signal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        food_alias = Food.alias()
        substitute_alias = Food.alias()

        substitutes = Substitute.select(
            food_alias.food_name.alias("food_name"),
            food_alias.id_food.alias("id_food"),
            substitute_alias.food_name.alias("substitute_name"),
            substitute_alias.id_food.alias("id_substitute")
        ) \
            .join(food_alias, on=Substitute.id_food) \
            .switch(Substitute) \
            .join(substitute_alias, on=Substitute.id_food_substitute) \
            .dicts() \
            .execute()

        self.result.emit(substitutes)