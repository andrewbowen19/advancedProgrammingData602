# Andrew Bowen
# DATA602: Assignment 2

# Q1
numbers = [1, 2, 3, 4, 5]

# print from initial index (0) to last index (-1 instead of -5)
print(numbers[0:-1])

# Q2
print('-------------------------------------')
days_of_week = [
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                "Sunday"
               ]
# Loop over days
daily_sales = []
for d in days_of_week:
    sales = int(input(f'Enter total sales ($) for {d}: '))
    daily_sales.append(sales)

total_sales = sum(daily_sales)
print(f"Total sales: ${total_sales}")


# Q3
print('-------------------------------------')
destinations = ['New Zealand',
                'Australia',
                'Japan',
                'Argentina',
                'Greece'
                ]
# Original order
print(destinations)
 
 # Sorted
destinations.sort()
print(destinations)

# Reverse sort
destinations.sort(reverse=True)
print(destinations)



# Q4
print('-------------------------------------')
course_rooms = { # course : room_number
           "DATA 606": "101",
           "DATA 607": "102",
           "DATA 605": "103",
           "DATA 602": "104"
}

course_instructors = { # course : room_number
           "DATA 606": "Catlin",
           "DATA 607": "Lu",
           "DATA 605": "Fulton",
           "DATA 602": "Schettini"
}

meeting_time = "6pm"
course_number = input("Please enter your course number: ")

print(f"Course: {course_number}")
print(f"Course Room: {course_rooms.get(course_number)}")
print(f"Instructor: {course_instructors.get(course_number)}")
print(f"Meeting time: {meeting_time}")

# Q5
print('-------------------------------------')
# Adding some dummy name : email pairs
email_dict = {"Andrew": "abo123@gmail.com",
              "Julia": "julia.rocks@yahoo.com",   
            }

choice = input("What would you like to do?\n- Add email [A]\n- Update email [U]\n-Remove email [R]\n")

name = input("Please enter your name: ")
email = input("Please enter your email: ")

# Add emails to dict or update existing ones as keys are unique
if choice.lower() == "a" or choice.lower() == "u":
    email_dict[name] = email

# Remove using built-in del method
elif choice.lower() == "r":
    del(email_dict[name])

print("Updated email dictionary: ")
print(email_dict)