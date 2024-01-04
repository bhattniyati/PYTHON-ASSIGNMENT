'''
    Write a Python program to calculate surface volume and area of a cylinder.
'''


# Define value of pi
pi=22/7

# input a height
height= float(input("Enter Height: "))

# input a radian 
radian= float(input("Enter Radius: "))

# formula of volume
volume= pi * radian * radian * height

# formula of area
area= ((2*pi*radian)*height) + ((pi*radian*radian)*2)

# display the result
print("Volume is: ",volume)
print("Surface Area is: ",area)
