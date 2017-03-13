"""
A simple python script that prints all files of a specific suffix
python get_all_files.py pdf -- > get all pdf files in current directory
python get_all_files.py csv --> get all csv files in current directory
Author: Daniel Saldivar-Salas
Date: 3/13/2017
"""

import os
import sys

def get_all_files():
	path = os.getcwd() #get current working directory
	suffix = sys.argv[1] #python zpdfs.py pdf --> suffix == 'pdf'
	for files in os.listdir(path):
		if files.endswith(suffix):
			print(files)
__name__ == '__main__':
	get_all_files()
