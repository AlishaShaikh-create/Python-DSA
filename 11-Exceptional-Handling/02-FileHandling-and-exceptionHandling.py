# File Handling and Exceptional Handling in python

try:
    file=open("example.txt",'r')
    content=file.read()
    print(content)
except FileNotFoundError:
    print("File does not exists")
finally:
     if 'file' in locals() and not file.closed():
         file.close()
         print('file closed')
            