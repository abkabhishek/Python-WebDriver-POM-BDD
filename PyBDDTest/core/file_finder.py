""" File finder Module. To fine any files in passed path as per pattern """
import glob
import os
import sys

class FileFinder:
    """ This is class with multiple class method which helps to find files in
    a pass path as per passed pattern match"""


    @classmethod
    def move_to(cls, dire):
        """ pass dir path to change current working directory"""
        try:
            os.chdir(dire)
        except FileNotFoundError as err:
            print("Path not Found : ", err)
            sys.exit()

    @classmethod
    def find_all_these(cls, file_pat):
        """ Pass file pattern to search in current working directory in os module"""
        files = []

        for file in glob.glob(file_pat):
            # print(file)
            files.append(file)
        return files

    @classmethod
    def current(cls):
        """ it just print your current directory"""
        print(os.getcwd())

    @classmethod
    def get_files(cls, file_pat, dire=os.getcwd()):
        """ Pass file patters and directory path
        required - filepat = File pattern to search
        option - dir = Directory path where to search,
        by default it will take current working directory as path"

        It will return
        path of searched directory
        List of Files found (blank list in case of no file found
        """
        cls.move_to(dire)
        files = cls.find_all_these(file_pat)
        return os.getcwd(), files

if __name__ == '__main__':
    print(FileFinder.get_files("input_??_prod*.txt", "../files/input/Old/"))
