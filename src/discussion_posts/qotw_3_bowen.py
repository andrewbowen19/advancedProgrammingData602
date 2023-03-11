"""
QOTW #3
Andrew Bowen
"""

### 1
animals = ['cat', 'dog', 'manta ray', 'horse', 'crouching tiger']


### 2
len_animals = len(animals)
for i in range(len_animals):
    print(animals[i])

### 3
countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
countdown.sort(reverse=True)

the_fifth_element = -999
the_fifth_element = countdown[4]

print(the_fifth_element)

### 4
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#Expected output:
#[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

### 5
list2 = [5, 20, 30, 15, 20, 30, 20]

# solve using list comprehensions
list2 = [x for x in list2 if x != 20]

### 6
my_dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}

# course name
course_name = my_dict.get("Course")
print(f"Course Name :{course_name}")

# change course to DATA602
my_dict['Course'] = "DATA602"

# add new info
my_dict['Professor'] = "Schettini"

# Using the len function, find how many keys there are in the dictionary. 
print(len(my_dict.keys()))


### 7
sample_dict = {
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
}

# update salary
sample_dict['Brad'] = 7500