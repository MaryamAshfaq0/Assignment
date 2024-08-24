# Q1    

def calculate_age(current_year, birth_year):
    return current_year - birth_year
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))
age = calculate_age(current_year, birth_year)
print(f"You are {age} years old.")

#Q2
def calculate_area(length, width):
    return length * width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print(f"The area of the rectangle is {area} square units.")

#Q3

radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * (radius ** 2)
print("The area of the circle is:", area)

#Q4

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"The temperature in Celsius is: {celsius:.2f}")

#Q5

side_length = float(input("Enter the side length of the cube: "))
surface_area = 6 * (side_length ** 2)
print(f"The surface area of the cube is: {surface_area:.2f}")

#Q6

total_seconds = int(input("Enter the number of seconds: "))
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds is equal to {minutes} minute(s) and {seconds} second(s).")

#Q7

total_marks = float(input("Enter the total marks: "))
obtained_marks = float(input("Enter the obtained marks: "))
percentage = (obtained_marks / total_marks) * 100
print(f"The percentage is: {percentage:.2f}%")

#Task 02
#Home Assignment 

#Q1

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")


#Q2

import math
def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = calculate_cylinder_volume(radius, height)
print(f"The volume of the cylinder is: {volume:.2f} cubic units")



