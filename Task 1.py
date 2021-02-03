import math
print("Task 1")
R=float(input("Enter the radius of circle:"))
a=math.pi*R*R
print("Area of circle is: ",a)
print()
print("Task 2")

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
