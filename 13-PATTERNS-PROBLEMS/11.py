# ord('A')=> convert the character to its ascii value which is 65
# chr() => convert the ascii value to the character



n=4
for i in range(n):
            for j in range(ord('A'),ord('A')+i+1,):
                print(chr(j),end='')
            print()    