"""
Write a program that cover the basics of python. and add comments that define which concept is used.
"""
 
"""
Solution:
Basic concepts.
variable
arithmetic operators
Conditional statement
loops
list
DataType
Function



You are given a list of names called name_list. Write a Python function called find_longest_name that takes in name_list as a parameter and returns the longest name from the list.

In your function, use the following steps:

Initialize a variable longest_name to an empty string to store the longest name.
Iterate over each name in name_list using a loop.
Inside the loop, check if the current name is longer than the longest_name.
If it is, update the value of longest_name to the current name.
Finally, return the value of longest_name.

Example Input:

name_list = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
find_longest_name(name_list) should return "Charlie"

"""
name_list = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

def find_longest_name(name_list):
    longest_name = ""
    for current_name in name_list:
         if (len(current_name) > len(longest_name)):
            longest_name = current_name;
    print("Longed Name should is ", longest_name)
find_longest_name(name_list)
"""
You are given a list of numbers called number_list. Write a Python function called find_odd_squares that takes in number_list as a parameter and returns a new list containing the squares of all the odd numbers in the original list.
In your function, use the following steps:
Initialize an empty list called odd_squares to store the squares of the odd numbers.
Iterate over each number in number_list using a loop.
Inside the loop, check if the current number is odd. If it is, square the number and append the result to the odd_squares list.
Finally, return the odd_squares list.
Example input/output:
number_list = [2, 3, 4, 5, 6, 7]
find_odd_squares(number_list) should return [9, 25, 49]
Write the function find_odd_squares according to the given specifications.

"""
number_list = [2, 3, 4, 5, 6, 7]
odd_squares = []

def find_odd_squares(number_list):
    for i in  number_list:
        if i % 2 != 0:
            square = i**2
            odd_squares.append(square)
    print(odd_squares)




find_odd_squares(number_list)