
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
list =[23,'Banana',45,'Siddu']
print(23 in list)
print('Siddu' not in list)

#------------Assignment Operators---------------
input_number = int(input("Enter the number "))
input_number += 3
print("The value of input_number after using += operator is ", input_number)

input_number = int(input("Enter the number "))
input_number -= 3
print("The value of input_number after using -= operator is ", input_number)

input_number = int(input("Enter the number "))
inlut_number *= 3
print("The value of input_number after using *= operator is ", input_number)

input_number = int(input("Enter the number "))
input_number /= 3
print("The value of input_number after using /= operator is", input_number)

input_number = int(input("Enter the number"))
input_number %= 4
print("The value of input_number after using %= operator is", input_number)

input_number = int(input("Enter the number"))
input_number //= 3
print("The value of input_number after using //= operator is", input_number)

input_number = int(input("Enter the number"))
input_number **= 3
print("The value of input_number after using **= operator is", input_number)

input_number = int(input("Enter the number"))
input_number &= 3
print("The value of input_number after using &= operator is", input_number)

input_number = int(input("Enter the number"))
input_number |= 7
print("The value of input_number after using |= operator is", input_number)

input_number = int(input("Enter the number"))
input_number ^= 0
print("The value of input_number after using ^= operator is", input_number)

input_number = int(input("Enter the number"))
input_number >>= 3
print("The value of input_number after using >>= operator is", input_number)

input_number = int(input("Enter the number"))
input_number <<= 3
print("The value of input_number after using <<= operator is", input_number)
