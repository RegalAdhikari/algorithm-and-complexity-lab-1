import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        input_list = [5, 4, 3, 2, 1]
        insertion_sort(input_list)
        self.assertEqual(input_list, [1, 2, 3, 4, 5])
if __name__ == '__main__':
     unittest.main()
