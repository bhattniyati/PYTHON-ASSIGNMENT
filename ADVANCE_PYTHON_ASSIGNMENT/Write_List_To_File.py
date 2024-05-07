'''
    Write a Python program to write a list to a file. 
'''

# Open file and write file
f= open("Write_List.txt","w") 

# Define list
item_list=["Mango","Orange","Apple","Graps"]

# Use loop : items in store item_list and write file in text file 
for items in item_list:
    f.write(items+"\n")

# close file
f.close()
