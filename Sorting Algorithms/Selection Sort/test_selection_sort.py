import unittest
from selection_sort import selection_sort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        A = [0, 2, 3, 4, 5]
        input_list = [5, 4, -3, 2, 1]
        result = selection_sort(input_list)
        self.assertListEqual(result, A)

if __name__ == '__main__':
    unittest.main()