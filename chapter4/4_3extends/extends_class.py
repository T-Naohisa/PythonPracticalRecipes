import unittest
import pathlib


class TestBase(unittest.TestCase):
    def setUp(self):
        self.data_path = pathlib.Path("/tmp/data")

    def tearDown(self):
        for p in self.data_path.iterdir():
            p.unlink()


class TestSample1(TestBase):
    def setUp(self):
        super().setUp()
        p1 = self.data_path / "sample.txt"
        p1.touch()

    def test_two_files(self):
        self.assertEqual(len(list(self.data_path.iterdir())), 2)


class TestSample2(TestBase):
    def setUp(self):
        super().setUp()
        p3 = self.data_path / "sample3.txt"
        p3.touch()

    def test_one_file(self):
        self.assertEqual(len(list(self.data_path.iterdir())), 1)
