import unittest

from recursion import *

class TestRecursiveOperations(unittest.TestCase):

    def setUp(self):
        self.one = 1
        self.five = 5
        self.numlist_one = [0]
        self.numlist_many = [1, 2, 3, 4, 5]
        self.nonpstring = "mari"
        self.pstring = "aya"

    def test_multiply_list(self):
        self.assertEqual(multiply_list(self.numlist_one), 0)
        self.assertEqual(multiply_list(self.numlist_many), 120)

    def test_factorial(self):
        self.assertEqual(factorial(self.one), 1)
        self.assertEqual(factorial(self.five), 120)

    def test_count_list(self):
        self.assertEqual(count_list(self.numlist_one), 1)
        self.assertEqual(count_list(self.numlist_many), 5)

    def test_sum_list(self):
        self.assertEqual(sum_list(self.numlist_one), 0)
        self.assertEqual(sum_list(self.numlist_many), 15)

    def test_reverse(self):
        self.assertEqual(reverse(self.numlist_one), [0])
        self.assertEqual(reverse(self.numlist_many), [5, 4, 3, 2, 1])

    def test_fibonacci(self):
        self.assertEqual(fibonacci(self.one), 0)
        self.assertEqual(fibonacci(self.five), 3)

    def test_find(self):
        self.assertEqual(find(self.numlist_many, self.one), 0)
        self.assertEqual(find(self.numlist_many, self.five), 4)

    def test_palindrome(self):
        self.assertEqual(palindrome(self.nonpstring), False)
        self.assertEqual(palindrome(self.pstring), True)

    def test_fold_paper(self):
        self.assertEqual(fold_paper(10, 0, 1), (5, 0))
        self.assertEqual(fold_paper(10, 8, 2), (5, 4))

    def test_count_up(self):
        pass

if __name__ == '__main__':
    unittest.main()
