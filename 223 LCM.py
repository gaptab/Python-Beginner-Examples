def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
        
    while(True):
        if((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater +=1
    return lcm

num1=64
num2=24

print("The L.C.M. of",num1,'and',num2,'is:',compute_lcm(num1,num2))

def compute_gcd(x,y):
    while(y):
        x,y=y,x%y
    return x

def compute_lcm(x,y):
    lcm=(x*y)//compute_gcd(x, y)
    return lcm

num1=64
num2=24

print("The L.C.M. is:",compute_lcm(num1,num2))
















