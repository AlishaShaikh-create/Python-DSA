# INVERTED RIGHT ANGLE TRIANGLE
def invertedRightAngle(size):
    for i in range(size):
        count=""
        for j in range(size,i,-1):
            count+="*"
        print(count)    
invertedRightAngle(3)            