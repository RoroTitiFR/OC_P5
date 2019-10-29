from PySide2.QtCore import QThread, Signal

from models.database.models import Substitute, Food, Brand, BrandFood


class SavedSubstitutesFetcherThread(QThread):
    result = Signal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        food_alias = Food.alias()
        substitute_alias = Food.alias()

        brand_food_food_alias = BrandFood.alias()
        brand_food_substitute_alias = BrandFood.alias()

        brand_food_alias = Brand.alias()
        brand_substitute_alias = Brand.alias()

        substitutes = Substitute.select(
            food_alias.food_name.alias("food_name"),
            food_alias.id_food.alias("id_food"),
            brand_food_alias.brand_name.alias("food_brand_name"),
            substitute_alias.food_name.alias("substitute_name"),
            substitute_alias.id_food.alias("id_substitute"),
            brand_substitute_alias.brand_name.alias("substitute_brand_name"),
        ) \
            .join(food_alias, on=Substitute.id_food) \
            .join(brand_food_food_alias, on=(food_alias.id_food == brand_food_food_alias.id_food)) \
            .join(brand_food_alias, on=brand_food_food_alias.id_brand) \
            .switch(Substitute) \
            .join(substitute_alias, on=Substitute.id_food_substitute) \
            .join(brand_food_substitute_alias, on=(substitute_alias.id_food == brand_food_substitute_alias.id_food)) \
            .join(brand_substitute_alias, on=brand_food_substitute_alias.id_brand) \
            .dicts() \
            .group_by(food_alias.id_food, substitute_alias.id_food) \
            .execute()

        print(substitutes)

        products_with_substitutes = []

        for substitute in substitutes:
            lol = {
                "product": {
                    "id_food": substitute["id_food"],
                    "food_name": substitute["food_name"],
                    "brand_name": substitute["food_brand_name"]
                },
                "substitute": {
                    "id_food": substitute["id_substitute"],
                    "food_name": substitute["substitute_name"],
                    "brand_name": substitute["substitute_brand_name"]
                }
            }

            products_with_substitutes.append(lol)

        self.result.emit(products_with_substitutes)
