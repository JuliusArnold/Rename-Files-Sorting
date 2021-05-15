import numpy as numpy
import os 
import math as math

count = 0

# Theo4 Übungsblätter
print(": ")
print(":Theo4:")
print("ÜB: ") 
path1 = "/home/retro/4-Sem/Theo4/ÜB/"
for file in os.listdir(path1):
	if 'Theo4' in file:
		pass
	else:

		ending = file.split(".")[-1]

		if ending == "pdf":
			pass
			number = file.split(".")[0].split("-")[-1]
			new_name_theo = "Blatt_Theo4_" + number + ".pdf"  		

			old_file_path = path1 + file
			new_file_path = path1 + new_name_theo
			os.rename(old_file_path,new_file_path)
			count += 1
			print(file + " --> " + new_name_theo)

# Theo4 Lösungen
print(": ")
print("Lsg_ÜB: ") 
path2 = "/home/retro/4-Sem/Theo4/ÜB/Lsg_ÜB/"
for file in os.listdir(path2):
	if 'Theo4' in file:
		pass
	else:

		ending = file.split(".")[-1]

		if ending == "pdf":
			number = file.split(".")[0].split("-")[-2]
			new_name_theo = "Blatt_Theo4_Lsg_" + number + ".pdf"  		

			old_file_path = path2 + file
			new_file_path = path2 + new_name_theo
			os.rename(old_file_path,new_file_path)
			count += 1
			print(file + " --> " + new_name_theo)

#Ex Übungsblätter
print(": ")
print(":Ex4:")
print("ÜB: ") 
path3 = "/home/retro/4-Sem/Ex4/ÜB/"

for file in os.listdir(path3):
	if 'Ex4' in file:
		pass 
	else:
		ending = file.split('.')[-1]
		if ending == "pdf":
			number = file.split(".")[0]
			if (len(number)<2):
				number = "0" + number
			new_name_ex = "Blatt_Ex4_" + number +".pdf"

			old_file_path = path3 + file
			new_file_path = path3 + new_name_ex 
			os.rename(old_file_path,new_file_path)
			count +=1
			print(file + " --> " + new_name_ex)

#Ex Lösungen kommen vielleicht noch


# Alda - Übungsblätter
print(": ")
print(":Alda1:")
print("ÜB: ") 
path4 = "/home/retro/4-Sem/IAD/ÜB/"
for file in os.listdir(path4):
	if "IAD" in file:
		pass 
	else:
		ending = file.split(".")[-1]
		if ending == "pdf":
			number = file.split(".")[0][8:]
			if len(number)<2:
				number = "0"+number 
			
			new_name_iad = "Blatt_IAD_" + number + ".pdf"
			old_file_path = path4 + file
			new_file_path = path4 + new_name_iad
			os.rename(old_file_path,new_file_path)
			count+=1
			print(file + " --> " + new_name_iad)


# MMP - Übungsblätter
print(": ")
print(":MMP1:")
print("ÜB: ") 
path5 = "/home/retro/4-Sem/MMP/ÜB/"
for file in os.listdir(path5):
	if "MMP1" in file:
		pass 
	else:
		ending = file.split(".")[-1]
		if ending == "pdf":
			number = file.split(".")[0][16:]
			
			
			new_name_mmp = "Blatt_MMP1_" + number + ".pdf"
			old_file_path = path5 + file
			new_file_path = path5 + new_name_mmp
			os.rename(old_file_path,new_file_path)
			count+=1
			print(file + " --> " + new_name_mmp)



print(" ")
print(": ")
print(": ")	
print(":Summary:")
print(": " + str(count) + " Documents were renamed.")
	
