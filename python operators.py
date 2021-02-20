
#-------------Bitwise Operators------------
#First Number
number_one=int(input("enter a number: "))
#Seconf Number
number_two=int(input("enter another number: "))
print(number_one&number_two)


#First Number
number_one=int(input("enter a number: "))
#Seconf Number
number_two=int(input("enter another number: "))
print(number_one|number_two)


#First Number
number_one=int(input("enter a number: "))
#Second Number
number_two=int(input("enter another number: "))
print(number_one^number_two)


#First Number
number_one=int(input("enter a number: "))
#Second Number
number_two=int(input("enter another number: "))
print(number_one<<1)
print(number_two<<1)


#First Number
number_one=int(input("enter a number: "))
#Second Number
number_two=int(input("enter another number: "))
print(number_one>>1)
print(number_two>>1)

#------------Membership Operators--------------
a =[23,'Banana',45,'Siddu']
print(23 in a)
print('Siddu' not in a)

#------------Assignment Operators---------------
x = int(input("Enter the number "))
x += 3
print("The value of x after using += operator is ", x)

x = int(input("Enter the number "))
x -= 3
print("The value of x after using -= operator is ", x)

x = int(input("Enter the number "))
x *= 3
print("The value of x after using *= operator is ", x)

x = int(input("Enter the number "))
x /= 3
print("The value of x after using /= operator is", x)

x = int(input("Enter the number"))
x %= 4
print("The value of x after using %= operator is", x)

x = int(input("Enter the number"))
x //= 3
print("The value of x after using //= operator is", x)

x = int(input("Enter the number"))
x **= 3
print("The value of x after using **= operator is", x)

x = int(input("Enter the number"))
x &= 3
print("The value of x after using &= operator is", x)

x = int(input("Enter the number"))
x |= 7
print("The value of x after using |= operator is", x)

x = int(input("Enter the number"))
x ^= 0
print("The value of x after using ^= operator is", x)

x = int(input("Enter the number"))
x >>= 3
print("The value of x after using >>= operator is", x)

x = int(input("Enter the number"))
x <<= 3
print("The value of x after using <<= operator is", x)