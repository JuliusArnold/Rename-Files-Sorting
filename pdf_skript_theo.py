import os 
import PyPDF2 
from PyPDF2 import PdfFileMerger
import shutil

# Theo-Skript-Zusammenfügen:
def pdf_combine(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		pdf_path= path + pdf 
		merger.append(pdf_path)
	merger.write(path+pdf_list[0]) 



path = "/home/julius/3-Sem/Theo3/Vorlesung/Folien/"
ziel_name = "NOTE_GES.pdf"
list_pdf = ["NOTE_GES.pdf"]

def create_list(path):
	for file in os.listdir(path):
		if file.split("_")[0] == "note":
			list_pdf.append(file)


def moving_files(pdf_list):
	for i in range(1,len(pdf_list)):
		old_file = pdf_list[i]
		new_file = "Einzeln/" + old_file
		#
		old_file_path = path + old_file
		new_file_path = path + new_file
		shutil.move(old_file_path,new_file_path) 
		print(old_file + "--->" + new_file)


create_list(path)
# print(list_pdf)
pdf_combine(list_pdf)
moving_files(list_pdf)