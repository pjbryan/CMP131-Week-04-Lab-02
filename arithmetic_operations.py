# PJ Bryan
# CMP-131-80230
# Week 04
# Lab 02
# Assignment 4
# 09/18/2026

print ()

# TITLE AND DIVIDERS: store title and characters for customization
programTitle = "ARITHMETIC OPERATIONS"
divider = "___________________"
divider2 = "*******************"
divider3 = "-------------------"

# START OF PROGRAM: print the program title and request user to type in their information
print (programTitle, divider2)
print ("ENTER YOUR VALUES", divider)
firstNumber = "Enter first number: "
secondNumber = "Enter second number: "

# STORE USER INPUT
userInput1 = float(input(firstNumber))
userInput2 = float(input(secondNumber))

# CALCULATIONS
addition = userInput1 + userInput2
subtraction = userInput1 - userInput2
multiplication = userInput1 * userInput2
division = userInput1 / userInput2
power = userInput1 ** userInput2
average = (userInput1 + userInput2) / 2

print ()

# OUTPUT: display calculations
print ("OUTPUT", divider3)
print (f"Addition: {addition:.2f}")
print (f"Subtraction: {subtraction:.2f}")
print (f"Multiplication: {multiplication:.2f}")
print (f"Division: {division:.2f}")
print (f"Power: {power:.2f}")
print (f"Average: {average:.2f}")