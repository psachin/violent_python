#!/usr/bin/env python
"""A Zip File password cracker.

Note: Replace dictionary.txt with
http://dazzlepod.com/site_media/txt/uniqpass_preview.txt to test
actual multi-threading. Append the content of dictionary.txt in
uniqpass_preview.txt

Usage:
python unzip.py -f dirs.zip -d dictionary.txt
"""
__author__ = "Sachin"
__email__ = "iclcoolster@gmail.com"
__description__ = "A Zip File password cracker."

import argparse
import random
import time
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
        return
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
    word_list = [word.strip('\n') for word in dict_file.readlines()]
    random.shuffle(word_list)
    for word in word_list:
        thread = Thread(target=extract_file, args=(zfile, word))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--zipfile", help="Protectted zip file name.")
    parser.add_argument("-d", "--dictionary", help="Dictionary file name.")
    args = parser.parse_args()

    if args.zipfile:
        zip_file = args.zipfile
    else:
        zip_file = 'dirs.zip'

    if args.dictionary:
        dictionary_file = args.dictionary
    else:
        dictionary_file = 'dictionary.txt'
    start_time = time.time()
    main(zip_file, dictionary_file)
    end_time = time.time()
    print "Took {0} seconds.".format(end_time - start_time)
