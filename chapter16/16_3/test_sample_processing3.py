from sample_processing import my_processing
from unittest.mock import patch
import unittest


class ExampleTest(unittest.TestCase):

    @patch("sample_processing.ShopppingSiteAPI.search_items")
    def test_example(self, search_items_mock):
        search_items_mock.return_value = [
            "モック商品1",
            "モック商品2",
            "モック商品3",
        ]
        actual = my_processing()
        expected = "モック商品1,モック商品2,モック商品3が見つかりました"
        self.assertEqual(actual, expected)
        search_items_mock.assert_called()


if __name__ == "__main__":
    unittest.main()
