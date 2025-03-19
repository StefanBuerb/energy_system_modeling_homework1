
def add (x,y):
    return x+y

def sub (x,y):
    return x-y  

def mul (x,y):
    return x*y  

def div (x,y):
    return x/y  

def mod (x,y):
    return x%y  

def power (x,y):
    return x**y 

def floor_div (x,y):
    return x//y 

def sqrt (x):
    return x**0.5  # x**0.5 is the square root of x

def factorial (x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1) # recursive function      
    
def absolute (x):
    if x<0:
        return -x
    else:
        return x
    
def maximum (x,y):
    if x>y:
        return x
    else:
        return y

def minimum (x,y):  
    if x<y:
        return x
    else:
        return y    
