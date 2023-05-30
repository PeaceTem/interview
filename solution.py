

"""
Number one
    AND
Number Two
"""

data = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY" : "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY" : "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY" : "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}


colors = {}

# store data in this format {'WHITE' : 7} 
for value in data.values():
    color_list = value.split(', ')
    for color in color_list:
        if color in colors.keys():
            colors[color] += 1
        else:
            colors[color] = 1



# finding the mean color
total = len(data)
mean_color = max(colors, key=lambda x: colors[x] / total)

most_likely = max(colors, key=lambda x: colors[x] / 5)

print("(1) Mean color:", mean_color)

print("(2) The color that is most likely worn throughout the week:", most_likely)

"""
The color that is mostly likely worn throughout the week: will have the highest number
when divided by 5

Number Three
"""
print(colors)
refined_data = {}

for key,value in data.items():
    color_list = value.split(', ')
    refined_data[key] = color_list

colors_list = colors.keys()

r_data = [*refined_data.values()]
# print(r_data)

everyday = []
for color in colors_list:
    for i in r_data:
        if color not in i:
            break

    everyday.append(color)


# print(everyday)

color_data = []

for r in r_data:
    color_data += r    

color_data.sort()

# print(color_data)


"""
The median is the color in the middle after the data has been sorted

"""

median = color_data[round((total+1)/2)]

print(f"(3) The median color is {median}")



"""
Number 4
Get the variance of the colors
variance = summation of (x - mean)^2 divided by n
"""
# mean = 95/12

mean = sum([x for x in colors.values()]) / len(colors)
variance = sum([pow((x - mean), 2) for x in colors.values()]) / len(colors)

print(f"Mean is {round(mean, 2)}")
print(f"(4) Variance is {variance}")



"""
Number 5
P(red) = number of red shirts divided by total number of shirts
"""


number_of_red = colors['RED']

p_red = number_of_red / total

print(f"(5) The probabilty that a shirt chosen at random is red: {p_red}")



"""
Number 6

For localhost postgres connection, check connection.py
"""


from supabase_py import create_client

# Create a Supabase client instance

"""
In production the url and key must be stored as environment variable
"""

supabase_url = 'https://etqvwworwopnpcvbvbli.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV0cXZ3d29yd29wbnBjdmJ2YmxpIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODU0MTM4MzcsImV4cCI6MjAwMDk4OTgzN30.Z7AY2cCMp7r02VFDC9ERY0qYK-UeGhHODMuTU5mVri8'
supabase = create_client(supabase_url, supabase_key)



# Define the table name and record data
table_name = 'color'

record_data = []

for key,value in colors.items():
    record_data.append({'name':key, 'frequency':value})

# Insert the record into the table
response = supabase.table(table_name).insert(record_data)
# print(dir(response))
# Check if the insert was successful
# if response.get_status() == 201:
#     print('Records inserted successfully.')
# else:
#     print('Error inserting record:', response.get_error())

print("(6) The the values has been inserted to the database")


"""
Number seven

other search algorithm can be utilise to solve this problem

Iterative binary search would be a better algorithm
"""

def recursive_search(number, numbers_list, start_index=0):
    # Base case: If the list is empty or all elements have been searched
    if start_index >= len(numbers_list):
        return False
    
    # Check if the current element matches the number
    if numbers_list[start_index] == number:
        return True
    
    # Recursive case: Continue searching in the remaining elements
    return recursive_search(number, numbers_list, start_index + 1)


# Example usage
numbers = [4, 2, 7, 1, 9, 5, 3, 8]
search_number = int(input("Enter a number to search: "))

found = recursive_search(search_number, numbers)

if found:
    print("(7) Number found in the list.")
else:
    print("(7) Number not found in the list.")






"""
Number 8

"""


import random

# Generate random 4-digit number consisting of 0s and 1s
random_number = random.choices([0, 1], k=4)

# Convert the random number to base 10
decimal_number = int(''.join(map(str, random_number)), 2)

# Print the random number and its base 10 representation
print("Random Number:", ''.join(map(str, random_number)))
print("(8) Decimal Equivalent:", decimal_number)




"""
Number 9

The fibonacci function is recursive and it uses dynamic programming to remember past values.
The dynamic algorithm increases its efficiency(Time Complexity).
The space complexity(O(n)) is the same with or without dynamic programming algorithm
"""



def fibonacci(n, memo={}):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


def fibonacci_sum(n):
    sum_fibonacci = 0
    for i in range(1, n+1):
        sum_fibonacci += fibonacci(i)

    return sum_fibonacci


# Calculate the sum of the first 50 Fibonacci numbers
sum_of_fibonacci = fibonacci_sum(50)

print("(9) Sum of the first 50 Fibonacci numbers:", sum_of_fibonacci)


print('Thanks for patiently assessing this work')
print('Art of Programming (AP101)')