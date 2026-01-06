# variable scope 

x=10
def fn():
    x=11
    
    print("This is local variable ", x)

fn()    
print("This is global variable",x)

# global key word to make the varible global


# nonlocal :
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x  # -> this  make variable to work with the outer function 
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
