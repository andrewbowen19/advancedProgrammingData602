#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')
test3 = input('Enter the score for test 3: ') # need to instantiate a test3 variable

# Calculate the average test score.

# Changing input types to int
average = (int(test1) + int(test2) + int(test3)) / 3
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE: # this should be all capitalized to match the HIGH_SCORE variable above
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
width1 = input("Enter rectangle 1's width: ")
length1 = input("Enter rectangle 1's length: ")

width2 = input("Enter rectangle 2's width: ")
length2 = input("Enter rectangle 2's length: ")

area1 = int(width1) * int(length1)
area2 = int(width2) * int(length2)

# Using f-strings to print our values and avoid typing errors
print(f"The area of rectangle 1 is: {area1}")
print(f"The area of rectangle 2 is: {area2}")


#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

name = input("Enter your name: ")
age = int(input("Enter your age: "))

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

# Again, using f-strings to avoid any typing errors when passing name & age variables to print statement
print(f"Happy birthday, {name}! You are {age} years old today!")

