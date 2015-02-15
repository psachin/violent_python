#!/usr/bin/env python
"""
A Password cracker based on crypt python module.
"""
__author__ = "Sachin"
__email__ = "iclcoolster@gmail.com"
__description__ = "A Password cracker based on crypt python module."

import crypt


def test_password(crypt_pass):
    """
    Cross-check encrypted password against dictionary words stored in
    dictionary.txt

    Argument:
    crypt_pass: Encrypted password
    """
    salt = crypt_pass[0:2]
    dict_file = open('dictionary.txt', 'r')
    for word in dict_file.readlines():
        word = word.strip('\n')
        if crypt.crypt(word, salt) == crypt_pass:
            print "[+] Found password: " + word + "\n"
            return

    print "[-] Password not found!\n"
    return


def main():
    """
    Scan passwords.txt, split hashed password and pass to test_password()
    """
    pass_file = open('passwords.txt', 'r')
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            crypt_pass = line.split(':')[1].strip('\n')
            print "[*] Craking password for: " + user
            test_password(crypt_pass)

if __name__ == '__main__':
    main()
