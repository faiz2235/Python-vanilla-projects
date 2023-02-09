'''
    Finds a file with the inputted string in the specified folder of your choice.
    ### Prerequisites
    Python3 is the only prerequisites! No external modules are needed to run.
    ### How to run the script
    In order to run this script you must have Python3 installed, not Python2. The
    command to run this is simply `python3 findstring.py`, and you'll be
    prompted with two questions, the string to search, and where to look.
'''

from genericpath import isdir
import os

text = input("input text:")
path = input("path:")

# os.chdir(path)


def getfiles(path):
    f = 0
    os.chdir(path)
    files = os.listdir()
    # print(files)
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            f = open(file_name, "r")
            if text in f.read():
                f = 1
                print(f"{text} found in ")
                final_path = os.path.abspath(file_name)
                print(final_path)
                return True
    if f == 1:
        print(f"{text} not found")
        return False


getfiles(path)
