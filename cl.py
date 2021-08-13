
print("\nHello World \n")

def add(x , y):
    z = x +y
    return z

def sub(x , y):
    z = x - y
    return z

def mul(x , y):
    z = x * y
    return z

def divi(x , y):
    z = x / y
    return z

def mod(x , y):
    z = x % y
    return z

a = float(input("Enter 1st Num : "))
b = float(input("Enter 2nd Num : "))


choice = input("Enter : \n1). Addition \n2). Subtraction \n3). Division \n4). Modulous \n5). Multiplication \n\n ::::--> ")

print("\nAddition : %0.2f " % add(a,b))
print("Subtract : %0.2f " % sub(a,b))
print("Division : %0.2f " % divi(a,b))
print("Modulous : %0.2f " % mod(a,b))
print("Multiplication : %0.2f " % mul(a,b))

print("\nBefore Swapping : %d , %d" % (a , b))

temp = a
a = b
b = temp

print("After Swapping : %d , %d" % (a , b))

sqrtnum = input("\nFind sqrt for : ")
print("Square root of %s is %0.3f " % (sqrtnum , pow(float(sqrtnum) , 2)) )

a = float(input("\nBase of the Triangle (cm) : "))
b = float(input("Height of the Triangle (cm) : "))
print("Area is : %0.2f cm2" % (0.5*a*b))

