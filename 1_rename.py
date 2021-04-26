import numpy as numpy
import os 
import math as math

count = 0

# Theo3 Übungsblätter
print(":Theo3:")
print("ÜB: ") 
path1 = "/home/julius/3-Sem/Theo3/ÜB/"
for file in os.listdir(path1):
	a = file.split(".")[-1]
	if a == "pdf":
		number = file.split("_")[2].split(".")[0]
		new_name_theo = "Blatt_Theo3_" + number + ".pdf"  

		if file != new_name_theo:
			old_file_path = path1 + file
			new_file_path = path1 + new_name_theo
			os.rename(old_file_path,new_file_path)
			count += 1
			print(file + " --> " + new_name_theo)

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




# Höma3 Übungsblätter
print(": ")
print(": ")
print(":Höma3:")
print("ÜB: ") 
path2 = "/home/julius/3-Sem/Höma3/ÜB/"

for file in os.listdir(path2):
	
	a = file.split(".")[-1]
	if a == "pdf":
		if file.split("_")[0] == "Blatt":
			pass
		else:
			number = file.split(" ")[-1].split(".")[0]

			if len(number) == 1:
				number = "0" + number
			
			new_name_Homa = "Blatt_Höma3_" + number + ".pdf"  

			if file != new_name_Homa:
				old_file_path = path2 + file
				new_file_path = path2 + new_name_Homa
				os.rename(old_file_path,new_file_path)
				count += 1
				print(file + " --> " + new_name_Homa)


# Höma3 Übungsblätter Lösungen
print("Lsg: ")
path6 = "/home/julius/3-Sem/Höma3/ÜB/Lsg_ÜB/"
for file in os.listdir(path6):
	if file[:5] != "Blatt":
		filetype = file.split(".")[-1]
		if filetype == "pdf":
			number = file.split(" ")[-1].split(".")[0]
			
			if len(number) == 1:
				number = "0" + number
			new_name = "Blatt_Höma3_Lsg_" + number + ".pdf"
			
			if file != new_name:
				ofp = path6 + file 
				nfp = path6 + new_name
				os.rename(ofp,nfp)
				count += 1
				print(file + " --> " + new_name)
# Höma3 Vorlesung
print("VL: ")
path_h_vl = "/home/julius/3-Sem/Höma3/Vorlesung/"
for file in os.listdir(path_h_vl):
	if file[:9] != "Vorlesung":
		filetype = file.split(".")[-1]
		if filetype == "mp4":
			number = file.split(" ")[-1].split(".")[0]

			if len(number) == 1:
				number = "0" + number
			new_name = "Vorlesung_Höma3_" + number + ".mp4"

			if file != new_name:
				ofp = path_h_vl + file 
				nfp = path_h_vl + new_name
				os.rename(ofp,nfp)
				count += 1
				print(file + " --> " + new_name)




# Ex3 Übungsblätter		
print(": ")
print(": ")	
print(":Ex3:")
print("ÜB: ") 
path3 = "/home/julius/3-Sem/Ex3/ÜB/"

for file in os.listdir(path3):
	
	a = file.split(".")[-1]
	if a == "pdf":

		if file.split("_")[0] == "Blatt":
			pass
		
		else:
			number = file.split(".")[0][-2:]


			
			
			new_name_Ex = "Blatt_Ex3_" + number + ".pdf"  

			if file != new_name_Ex:
				old_file_path = path3 + file
				new_file_path = path3 + new_name_Ex
				os.rename(old_file_path,new_file_path)
				count += 1
				print(file + " --> " + new_name_Ex)

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


# IPI Übungsblätter	
print(": ")
print(": ")			
print(":IPI:")
print(": ") 
path4 = "/home/julius/3-Sem/IPI/ÜB/"

for file in os.listdir(path4):
	
	a = file.split(".")[-1]
	if a == "pdf":

		if file.split("_")[0] == "Blatt":
			pass
		
		else:
			number = file.split(".")[0][-2:]


			
			
			new_name_ipi = "Blatt_IPI_" + number + ".pdf"  

			if file != new_name_ipi:
				old_file_path = path4 + file
				new_file_path = path4 + new_name_ipi
				os.rename(old_file_path,new_file_path)
				count += 1
				print(file + " --> " + new_name_ipi)

print(": ")
print(": ")	
print(":Summary:")
print(": " + str(count) + " Documents were renamed.")
	