from unittest.mock import MagicMock


class ShopppingSiteAPI:
    def search_items(self, name):
        return ["商品1", "商品2", "商品3"]

    def purchase(self, item_id):
        pass


def my_processing():
    api = ShopppingSiteAPI()
    return ",".join(api.search_items("商品")) + "が見つかりました"


# api = ShopppingSiteAPI()
# api.search_items = MagicMock()
# api.search_items.return_value = ["モック商品1", "モック商品2", "モック商品3"]


if __name__ == "__main__":
    print(my_processing())
