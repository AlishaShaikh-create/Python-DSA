# Reading the file 
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



# writing the content into the file overwriting the content
        
    
    

        