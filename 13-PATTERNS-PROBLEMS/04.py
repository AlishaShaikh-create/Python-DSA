# RIGHT ANGLE TRIANGLE
def RightAngle(n):
    for i in range(1,n+1):
        count=""
        for j in range(i):
            count=count+"*"
        print(count)    

RightAngle(3)        