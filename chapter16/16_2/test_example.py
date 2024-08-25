import unittest
from example import add


class AddTest(unittest.TestCase):
    def test_get_the_sum_of_one_integers(self):
        actual = add(1, 2)
        expected = 3
        self.assertEqual(actual, expected)

    def test_get_the_sum_of_two_integers(self):
        examples = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for idx, example in enumerate(examples):
            a, b, expected = example
            with self.subTest(f"{a} + {b} = {expected}", idx=idx):
                self.assertEqual(add(a, b), expected)


if __name__ == "__main__":
    unittest.main()
