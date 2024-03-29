import numpy as numpy
import os 
import math as math

count = 0


#Ex Übungsblätter
print(": ")
print(":Ex5:")
print("ÜB: ") 
path3 = "/home/julius/5-Sem/Ex5/ÜB/"

for file in os.listdir(path3):
    if 'Ex5' in file:
        pass 
    else:
        ending = file.split('.')[-1]
        if ending == "pdf":
            number = file.split(".")[0].split("_")[1]
            if (len(number)<2):
                number = "0" + number
            new_name_ex = "Blatt_Ex5_" + number +".pdf"

            old_file_path = path3 + file
            new_file_path = path3 + new_name_ex 
            os.rename(old_file_path,new_file_path)
            count +=1
            print(file + " --> " + new_name_ex)

#Ex Lösungen kommen vielleicht noch




# Alda - Übungsblätter
print(": ")
print(":Alda2:")
print("ÜB: ") 
path4 = "/home/julius/5-Sem/IAD2/ÜB/"
for file in os.listdir(path4):
	if "IAD2" in file:
		pass 
	else:
		ending = file.split(".")[-1]
		if ending == "pdf":
			number = file.split(".")[0][8:]
			if len(number)<2:
				number = "0"+number 
			
			new_name_iad = "Blatt_IAD2_" + number + ".pdf"
			old_file_path = path4 + file
			new_file_path = path4 + new_name_iad
			os.rename(old_file_path,new_file_path)
			count+=1
			print(file + " --> " + new_name_iad)

print(": ")
print(":BIC:")
print("ÜB: ") 
path4 = "/home/julius/5-Sem/BIC/ÜB/"
for file in os.listdir(path4):
	if "BIC" in file:
		pass 
	else:
		ending = file.split(".")[-1]
		if ending == "pdf":
			number = file.split("_")[0][8:]
			if len(number)<2:
				number = "0"+number 
			
			new_name_iad = "Blatt_BIC_" + number + ".pdf"
			old_file_path = path4 + file
			new_file_path = path4 + new_name_iad
			os.rename(old_file_path,new_file_path)
			count+=1
			print(file + " --> " + new_name_iad)


#FML Übungsblätter
print(": ")
print(":FML:")
print("ÜB: ") 
path5 = "/home/julius/5-Sem/ML_21-22/ÜB/"

for file in os.listdir(path5):
    if 'Blatt_FML' in file:
        pass 
    else:
        ending = file.split('.')[-1]
        if ending == "pdf":
            number = file.split(".")[4].split(" ")[1]
            print(number)
            if (len(number)<2):
                number = "0" + number
            new_name_ex = "Blatt_FML_" + number +".pdf"

            old_file_path = path5 + file
            new_file_path = path5 + new_name_ex 
            os.rename(old_file_path,new_file_path)
            count +=1
            print(file + " --> " + new_name_ex)

#FML Lösungen
print(": ")
print("Lsg: ") 
path6 = "/home/julius/5-Sem/ML_21-22/ÜB/Lsg_ÜB/"

for file in os.listdir(path6):
    if 'Blatt_FML_Lsg_' in file:
        pass 
    else:
        ending = file.split('.')[-1]
        if ending == "pdf":
            number = file.split(".")[4].split(" ")[-1]
            print(number)
            if (len(number)<2):
                number = "0" + number
            new_name_ex = "Blatt_FML_Lsg_" + number +".pdf"

            old_file_path = path6 + file
            new_file_path = path6 + new_name_ex 
            os.rename(old_file_path,new_file_path)
            count +=1
            print(file + " --> " + new_name_ex)


print(" ")
print(": ")	
print(":Summary:")
print(": " + str(count) + " Documents were renamed.")
	
