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

print(" ")
print(": ")
print(": ")	
print(":Summary:")
print(": " + str(count) + " Documents were renamed.")
	
