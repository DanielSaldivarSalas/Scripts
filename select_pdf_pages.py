"""
python select_pdf_pages.py pages.txt
pages.txt selects the number of pages you want to add from the pdf
Author: Daniel Saldivar-Salas
Date: 3/13/2017
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import fileinput

reader = PdfFileReader(sys.argv[1], 'r')
writer = PdfFileWriter()

for num in fileinput.input(sys.argv[2]):
	page = reader.getPage(int(num)-1)
	writer.addPage(page)

outstream = open("selected-pages"+ sys.argv[1],'wb')
writer.write(outstream)
outstream.close
