"""
QOTW 4
Andrew Bowen
DATA 602
"""

### 1
def calculate_rectangle_area(width, height):
    return width * height

def calculate_rectangle_perimeter(width, height):
    return 2* width + 2 * height

### 2
def even_or_odd(number: int) -> str:
    even_or_odd = "Even" if (number % 2) == 0  else  "Odd"
    return even_or_odd

### 3
def count_case(string: str)-> dict:
    counts = {'Upper': 0, 'Lower': 0}
    for s in string:
        if s.isupper():
            counts['Upper'] += 1
        elif s.islower():
            counts['Lower'] += 1
        else:
            pass
    return counts
        
### 4: sum list
def sum_list(l: list)-> int:
    return sum(l)

### 5: global v local
my_var = "global val!"
print(my_var)

def my_func():
    my_var = "local val!"
    print(my_var)

# prints local val
my_func()

# prints global val
print(my_var)

### 6
# Typing here may be a nightmare: proceed with caution (or use Typescript :) )
def multiply_arg(argument, number:int):
    return argument * number