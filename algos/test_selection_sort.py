#!/usr/bin/env python
import unittest

from selection_sort import selection_sort

class SelectionSort(unittest.TestCase):
    '''
    Test case for selection_sort.py
    '''
    def test_sample1(self):
        '''
        Test int & negative int
        '''
        sample = [12, 1, 5, -7, 0, 56, 3]
        ans = [-7, 0, 1, 3, 5, 12, 56]
        self.assertEqual(selection_sort(sample), ans)

    def test_sample2(self):
        '''
        Test zeros
        '''
        sample = [0, 0, 0, 0, 0]
        ans = [0, 0, 0, 0, 0]
        self.assertEqual(selection_sort(sample), ans)

    def test_sample3(self):
        '''
        Test negatives
        '''
        sample = [-1, -2, -3, -4, -4, -4, -5]
        ans = [-5, -4, -4, -4, -3, -2, -1]
        self.assertEqual(selection_sort(sample), ans)

    def test_sample4(self):
        '''
        Test negatives and zeros
        '''
        sample = [-1, -2, -3, -4, 0, 0, 0, -4, -5]
        ans = [-5, -4, -4, -3, -2, -1, 0, 0, 0]
        self.assertEqual(selection_sort(sample), ans)

    def test_sample5(self):
        '''
        Test long list
        '''
        sample = range(100, 0, -1)
        ans = range(1, 101)
        self.assertEqual(selection_sort(sample), ans)

    def test_sample6(self):
        '''
        Test looooong list
        '''
        sample = range(1000000, 0, -1)
        ans = range(1, 1000001)
        self.assertEqual(selection_sort(sample), ans)

    def test_sample7(self):
        '''
        Test decimals
        '''
        sample = [0.5, 0.0, 0.001, 78]
        ans = [0.0, 0.001, 0.5, 78]
        self.assertEqual(selection_sort(sample), ans)

    def test_empty_sample(self):
        '''
        Test empty list
        '''
        sample = []
        ans = []
        self.assertEqual(selection_sort(sample), ans)

    def test_is_list(self):
        '''
        Test non-list
        '''
        sample = 'a_list'
        self.assertFalse(selection_sort(sample))
        sample = 1
        self.assertFalse(selection_sort(sample))

if __name__ == '__main__':
    unittest.main()
