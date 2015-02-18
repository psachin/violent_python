#!/usr/bin/env python
"""A Zip File password cracker.

Note: Replace dictionary.txt with
http://dazzlepod.com/site_media/txt/uniqpass_preview.txt to test
actual multi-threading. Append the content of dictionary.txt in
uniqpass_preview.txt
"""
__author__ = "Sachin"
__email__ = "iclcoolster@gmail.com"
__description__ = "A Zip File password cracker."

import zipfile
from threading import Thread


def extract_file(zfile, password):
    """Cross-check password against dictionary words stored in
    dictionary.txt

    Arguments:
    zfile: zipfile.ZipFile object
    password: Password from dictionary.txt"""
    try:
        zfile.extractall(pwd=password)
        print "[+] Password = " + password + '\n'
    except Exception, error:
        pass


def main(zip_file, dictionary):
    """
    Scan dictionary file, split string(password) and pass to extract_file()
    Run extract_file as thread object.

    Arguments:
    zip_file: Path to protected zip file.
    dictionary: Path to dictionary file.
    """
    threads = []
    zfile = zipfile.ZipFile(zip_file)
    dict_file = open(dictionary, 'r')
    for word in dict_file.readlines():
        word = word.strip('\n')
        thread = Thread(target=extract_file, args=(zfile, word))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    zip_file = 'dirs.zip'
    dictionary_file = 'dictionary.txt'
    main(zip_file, dictionary_file)
