import numpy as numpy
import os 
import math as math
count = 0 
# Theo3 Übungsblätter Lösungen 
print("Lsg: ")
path5 = "/home/julius/3-Sem/Theo3/ÜB/Lsg_ÜB/"
for file in os.listdir(path5):
	if file[:5] != "Blatt":
		filetype = file.split(".")[-1]
		if filetype == "pdf":
			number = file.split("_")[-2]
			new_name = "Blatt_Theo3_Lsg_" + number + ".pdf"

			if file != new_name:
				ofp = path5 + file 
				nfp = path5 + new_name
				os.rename(ofp,nfp)
				count += 1
				print(file + " --> " + new_name)

# Höma3 Übungsblätter Lösungen
print("Lsg: ")
path6 = "/home/julius/3-Sem/Höma3/ÜB/Lsg_ÜB/"
for file in os.listdir(path6):
	if file[:5] != "Blatt":
		filetype = file.split(".")[-1]
		if filetype == "pdf":
			number = file.split(" ")[-1].split(".")[0]
			new_name = "Blatt_Höma3_Lsg_" + number + ".pdf"

			if file != new_name:
				ofp = path6 + file 
				nfp = path6 + new_name
				os.rename(ofp,nfp)
				count += 1
				print(file + " --> " + new_name)




# Ex3 Übungsblätter Lösungen
print("Lsg: ")
path7 = "/home/julius/3-Sem/Ex3/ÜB/Lsg/"
for file in os.listdir(path7):
	filetype = file.split(".")[-1]
	if filetype == "pdf":
		if file[:14] != "Blatt_Ex3_Lsg_":
			number = file.split("_")[0][-2:]
			new_name = "Blatt_Ex3_Lsg_" + number + ".pdf"

			ofp = path7 + file 
			nfp = path7 + new_name
			os.rename(ofp,nfp)
			count += 1
			print(file + " --> " + new_name)


