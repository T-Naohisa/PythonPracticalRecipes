from sample_processing import my_processing
from unittest.mock import patch
import unittest


class ExampleTest(unittest.TestCase):
    def test_my_processing(self):
        with patch("sample_processing.ShopppingSiteAPI") as APIMock:
            api = APIMock()
            api.search_items.return_value = [
                "モック商品1",
                "モック商品2",
                "モック商品3",
            ]
            self.assertEqual(
                my_processing(), "モック商品1,モック商品2,モック商品3が見つかりました"
            )


if __name__ == "__main__":
    unittest.main()
