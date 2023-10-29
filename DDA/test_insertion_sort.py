import unittest
from insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        # Test case 1
        arr1 = [12, 4, 90, 2, 1, 0, 3]
        expected_output1 = [0, 1, 2, 3, 4, 12, 90]
        self.assertEqual(insertion_sort(arr1), expected_output1)

        # Test case 2
        arr2 = [5, 2, 8, 3, 9, 1]
        expected_output2 = [1, 2, 3, 5, 8, 9]
        self.assertEqual(insertion_sort(arr2), expected_output2)

        # Test case 3
        arr3 = [1, 2, 3, 4, 5]
        expected_output3 = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(arr3), expected_output3)

        # Test case 4
        arr4 = [5, 4, 3, 2, 1]
        expected_output4 = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(arr4), expected_output4)

if __name__ == '__main__':
    unittest.main()