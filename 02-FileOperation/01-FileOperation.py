# Reading the file 
# read mode
with open("example.txt",'r') as file:
    content=file.read()
    print(content)
    for line in file: #  why does this for loop does not execute its because the file pointer is at the end of the line it has already read the content throught file.read() 
        print(line) 

#Output:
# Hello i am example.txt file 
# This file is only for the understanding purpose
# I does not contain any code 
# You can write what ever u want to write here



# Reading the content of the file line by line
with open("example.txt" , 'r') as file:
    for line in file:
        print(line.strip())  # .strip() removes the new line character    

# Output:
# Hello i am example.txt file 

# This file is only for the understanding purpose

# I does not contain any code

# You can write what ever u want to write here


#WRITE MODE
# writing the content into the file overwriting the content
with open("example.txt", 'w') as file:
    file.write("Hello World \n")        
    file.write("Hi there \n")
    
# Output: The content in the example.txt will get changed


# APPEND MODE
# writing into the file without overwriting

with open("example.txt",'a') as file:
    file.write("Append opention taking place in example file")

# writing a list of lines to a file
lines=['First line \n' , 'second line \n' , 'Third line\n']
with open('example.txt','a') as file:
    file.writelines(lines)


# Binary Files: 
# WRITE MODE
data = b'/x00/x01'
with open ('example.bin','wb') as file:
    file.write(data)

# READ MODE :
with open('example.bin', 'rb') as file :
    print(file.read())   
    

# read the content from the source and then  write it into the destination file

with open('example.txt','r') as file:
    content=file.read()
with open ('destination.txt', 'w') as file:
    file.write(content)    


# Counting the lines words and the number of character in the line

def count(filePath):
    with open(filePath,'r') as file:
        lines=file.readlines()
        line_count=len(lines)
        word_count=sum(len(line.split()) for line in lines)
        char_count=sum(len(line) for line in lines)
    return line_count, word_count, char_count

filepath='example.txt'
lines,words,char=count(filepath)  
print(lines,words,char)      
    


# w+ mode : 
with open("example.txt", 'w+') as file:
     file.write("Hello world \n")
     file.write("This is the second line \n")

     # Move the file cursor to the beginning
     file.seek(0)
     
     content = file.read()
     print(content)
     

# creating a new directory

import os
# os.mkdir("new_directory")
# print("The new directory is created")     


# Listing Files And 
items=os.listdir('.')
print(items)


# Joining Paths
dir_name='folder'
file_name="file.txt"
full_path=os.path.join(dir_name,file_name)
print(full_path)

         
dir_name='folder'
file_name="file.txt"
full_path=os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)


path='example.txt'
if os.path.exists(path):
    print(f" the path {path} exist")        
else:
    print(f" the path {path} exist")    
    
# Getting the absolute path
relative_path='example.txt'    
absolute_path=os.path.abspath(relative_path)
print(absolute_path)

