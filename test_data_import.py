import unittest
import data_import as di


class TestImportData(unittest.TestCase):
    def test_linear_search_one_match(self):
        self._roundtimeStr = [9, 0, 2, 1, 0]
        self._value = [8, 9, 3, 6, 1]
        r = di.ImportData.linear_search_value(self, 2)
        self.assertEqual(r, [3])

    def test_linear_search_two_match(self):
        self._roundtimeStr = [9, 0, 2, 1, 0]
        self._value = [8, 9, 3, 6, 1]
        r = di.ImportData.linear_search_value(self, 0)
        self.assertEqual(r, [9, 1])

    def test_linear_search_no_match(self):
        self._roundtimeStr = [9, 0, 2, 1, 0]
        self._value = [8, 9, 3, 6, 1]
        r = di.ImportData.linear_search_value(self, 8)
        self.assertEqual(r, [])

    def test_binary_search_no_match(self):
        self._time = [9, 0, 2, 1, 0]
        self._value = [8, 9, 3, 6, 1]
        r = di.ImportData.binary_search_value(self, 1)
        self.assertEqual(r, [8])


if __name__ == '__main__':
    unittest.main()
