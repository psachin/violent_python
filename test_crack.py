#!/usr/bin/env python
"""
Unittest for crack.py
"""
__author__ = "Sachin"
__email__ = "iclcoolster@gmail.com"
__description__ = "Unittest for crack.py"

import unittest

from crack import test_password
from crypt import crypt


class TestCrack(unittest.TestCase):
    """Unittest for crack.py"""
    def test_can_read_dictonary(self):
        """Check dictionary.txt"""
        dict_file = open('dictionary.txt', 'r')
        self.assertTrue(dict_file.read())

    def test_can_read_passwords(self):
        """Check passwords.txt"""
        password_file = open('passwords.txt', 'r')
        self.assertTrue(password_file.read())

    def test_found_password(self):
        """Whether password is present in dictionary.txt"""
        encrypted_password = crypt('egg', 'HX')
        self.assertEqual(test_password(encrypted_password), 0)

    def test_password_not_found(self):
        """Password is not present in dictionary.txt"""
        encrypted_password = crypt('gimp', 'HX')
        self.assertEqual(test_password(encrypted_password), 1)

if __name__ == '__main__':
    unittest.main()
