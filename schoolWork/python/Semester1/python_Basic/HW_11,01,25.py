 
# Variables
# 1. Declare a variable and assign it your name.
name = "Sun Sarun"
print(name)

# 2. Create two variables and assign them integer values, then print their sum.
a, b = 42, 69
print(a + b)

# 3. Swap the values of two variables without using a third variable.
a, b = 42, 69
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# 4. Assign a floating-point number to a variable and display it.
a = 3.14
print("Floating Point =", a)

# 5. Assign a boolean value to a variable and print it.
a = True
print("Boolean Value =", a)

# 6. Update the value of a variable and print the updated value.
a = 24
print("Before update =", a)
a = 42
print("After update =", a)

# 7. Declare a constant-like variable using uppercase and demonstrate why Python allows updates.
import math
print("Default value of pi:", math.pi)
math.pi = 3
print("Updated value of pi:", math.pi)

# 8. Create a variable with a null value and then assign it a string.
a = None
print("Unassigned =", a)
a = "Assigned value"
print(a)

# 9. Create three variables in a single line with the same value.
a = b = c = 69

# 10. Create three variables in a single line with different values.
a, b, c = 2, 3, 4

# 11. Assign multiple types (int, float, string) to variables and print their types.
a = 69
b = 42.2
c = "string"
print(type(a), type(b), type(c))

# 12. Create a variable with a string containing your name and age using placeholders.
name = "Sarun"
age = 20
info = f"My name is {name}, and I am {age} years old."
print(info)

# 13. Use the del keyword to delete a variable and try accessing it after deletion.
a = 69
del a
# print(a) # Uncommenting this will raise a NameError.

# 14. Use type hinting to declare a variable and assign it a value.
name: str = "Sarun"
age: int = 20
print(name, age)

# 15. Assign the same value to multiple variables and verify their memory addresses.
a = b = 69
print(id(a), id(b))

# 16. Assign a value to a variable using an expression.
a = 5 * 5
print("Expression result =", a)

# 17. Print a variable without assigning it a value. (This will raise an error.)
# print(value) # Uncommenting this will raise a NameError.

# 18. Assign a list of numbers to a variable and print the sum of its elements.
num = [1, 2, 3, 4, 5]
print(sum(num))

# 19. Create a variable inside a function and try accessing it outside.
def func():
    local_a = 69
    print(local_a)

func()
# print(local_a) # Uncommenting this will raise a NameError.

# 20. Use global and local variables in a small function example.
global_a = 69

def modify_func():
    global global_a
    global_a = 42

modify_func()
print(global_a)

# Data Types and Operations
# 1-5. Identify types
print(type(69), type(2.71), type("sarun"), type(True), type(None))

# 6-9. Convert types
print("int to float:", float(69))
print("float to int:", int(2.71))
print("string to int:", int("69"))
print("string to list:", list("sarun"))

# 10-13. Identify the type
print(type({"key": "value"}))
print(type([1, 2, 3]), type((1, 2, 3)), type({1, 2, 3}))

# 14. Demonstrate dynamic type changes
a = 69
print(a)
a = "sarun"
print(a)

# 15. Check if a variable is an integer.
print(isinstance(69, int))

# 16. Create a complex number and print its real and imaginary parts.
c_num = 1 + 2j
print(c_num.real, c_num.imag)

# 17. Demonstrate type casting with a boolean.
print("bool to int:", int(True))

# 18. Create a list with mixed types.
mix_list = [69, "sarun", 2.71]
print(mix_list)

# 19. Use isinstance() to verify a variable's type.
print(isinstance("sarun", str))

# 20. Check if input is a number.
try:
    user_input = int(input("Enter a number: "))
    print("It is a number!")
except ValueError:
    print("Not a number.")


# Variables
# 1. Declare a variable and assign it your name.
name = "Sun Sarun"
print(name)

# 2. Create two variables and assign them integer values, then print their sum.
a, b = 42, 69
print(a + b)

# 3. Swap the values of two variables without using a third variable.
a, b = 42, 69
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# 4. Assign a floating-point number to a variable and display it.
a = 3.14
print("Floating Point =", a)

# 5. Assign a boolean value to a variable and print it.
a = True
print("Boolean Value =", a)

# 6. Update the value of a variable and print the updated value.
a = 24
print("Before update =", a)
a = 42
print("After update =", a)

# 7. Declare a constant-like variable using uppercase and demonstrate why Python allows updates.
import math
print("Default value of pi:", math.pi)
math.pi = 3
print("Updated value of pi:", math.pi)

# 8. Create a variable with a null value and then assign it a string.
a = None
print("Unassigned =", a)
a = "Assigned value"
print(a)

# 9. Create three variables in a single line with the same value.
a = b = c = 69

# 10. Create three variables in a single line with different values.
a, b, c = 2, 3, 4

# 11. Assign multiple types (int, float, string) to variables and print their types.
a = 69
b = 42.2
c = "string"
print(type(a), type(b), type(c))

# 12. Create a variable with a string containing your name and age using placeholders.
name = "Sarun"
age = 20
info = f"My name is {name}, and I am {age} years old."
print(info)

# 13. Use the del keyword to delete a variable and try accessing it after deletion.
a = 69
del a
# print(a)  # Uncommenting this will raise a NameError.

# 14. Use type hinting to declare a variable and assign it a value.
name: str = "Sarun"
age: int = 20
print(name, age)

# 15. Assign the same value to multiple variables and verify their memory addresses.
a = b = 69
print(id(a), id(b))

# 16. Assign a value to a variable using an expression.
a = 5 * 5
print("Expression result =", a)

# 17. Print a variable without assigning it a value. (This will raise an error.)
# print(value)  # Uncommenting this will raise a NameError.

# 18. Assign a list of numbers to a variable and print the sum of its elements.
num = [1, 2, 3, 4, 5]
print(sum(num))

# 19. Create a variable inside a function and try accessing it outside.
def func():
    local_a = 69
    print(local_a)

func()
# print(local_a)  # Uncommenting this will raise a NameError.

# 20. Use global and local variables in a small function example.
global_a = 69

def modify_func():
    global global_a
    global_a = 42

modify_func()
print(global_a)

# Data Types
# 1-5. Identify types
print(type(69), type(2.71), type("sarun"), type(True), type(None))

# 6-9. Convert types
print("int to float:", float(69))
print("float to int:", int(2.71))
print("string to int:", int("69"))
print("string to list:", list("sarun"))

# 10-13. Identify the type
print(type({"key": "value"}))
print(type([1, 2, 3]), type((1, 2, 3)), type({1, 2, 3}))

# 14. Demonstrate dynamic type changes
a = 69
print(a)
a = "sarun"
print(a)

# 15. Check if a variable is an integer.
print(isinstance(69, int))

# 16. Create a complex number and print its real and imaginary parts.
c_num = 1 + 2j
print(c_num.real, c_num.imag)

# 17. Demonstrate type casting with a boolean.
print("bool to int:", int(True))

# 18. Create a list with mixed types.
mix_list = [69, "sarun", 2.71]
print(mix_list)

# 19. Use isinstance() to verify a variable's type.
print(isinstance("sarun", str))

# 20. Check if input is a number.
try:
    user_input = int(input("Enter a number: "))
    print("It is a number!")
except ValueError:
    print("Not a number.")

# Data Structures
# 1. Create a list of five numbers and print it.
num = [2, 4, 6, 8, 10]
print(num)

# 2. Append an element to a list.
num.append(12)
print(num)

# 3. Insert an element at the beginning of a list.
num.insert(0, 1)
print(num)

# 4. Remove an element from a list by value.
num.remove(6)
print(num)

# 5. Remove an element from a list by index.
num.pop(3)
print(num)

# 6. Sort a list in ascending order.
num.sort()
print(num)

# 7. Reverse a list.
num.reverse()
print(num)

# 8. Create a dictionary with three key-value pairs.
dictionary = {"name": "Sarun", "age": 20, "job": "Computer scientist"}
print(dictionary)

# 9. Access a value in a dictionary using its key.
print(dictionary["name"])

# 10. Add a new key-value pair to a dictionary.
dictionary["location"] = "Cambodia"
print(dictionary)

# 11. Remove a key-value pair from a dictionary.
del dictionary["age"]
print(dictionary)

# 12. Create a tuple with five elements.
me_tuple = (2, 4, 6, 8, 10)
print(me_tuple)

# 13. Access the second element of a tuple.
print(me_tuple[1])

# 14. Unpack a tuple into separate variables.
a, b, c, d, e = me_tuple
print(a, b, c, d, e)

# 15. Create a set and add an element to it.
me_set = {2, 4, 6}
me_set.add(8)
print(me_set)

# 16. Remove an element from a set.
me_set.remove(4)
print(me_set)

# 17. Check if an element exists in a set.
print(6 in me_set)

# 18. Perform a union operation on two sets.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))

# 19. Perform an intersection operation on two sets.
print(set_a.intersection(set_b))

# 20. Create a nested dictionary and access an inner value.
nested_dict = {"person": {"name": "Sarun", "age": 20}}
print(nested_dict["person"]["name"])

# Basic Operations
# 1. Add two numbers.
print(4 + 5)

# 2. Subtract two numbers.
print(8 - 4)

# 3. Multiply two numbers.
print(4 * 5)

# 4. Divide two numbers and print the result as a float.
print(9 / 2)

# 5. Perform integer division.
print(9 // 2)

# 6. Find the remainder of a division.
print(9 % 2)

# 7. Raise a number to a power.
print(2 ** 3)

# 8. Use the floor division operator.
print(10 // 6)

# 9. Compare two numbers using `==`.
print(9 == 2)

# 10. Compare two numbers using `!=`.
print(4 != 2)

# 11. Use logical AND on two boolean values.
print(True and False)

# 12. Use logical OR on two boolean values.
print(False or True)

# 13. Use a bitwise AND on two integers.
print(5 & 1)

# 14. Use a bitwise OR on two integers.
print(5 | 1)

# 15. Increment a variable using `+=`.
num = 6
num += 2
print(num)

# 16. Decrement a variable using `-=`.
num -= 3
print(num)

# 17. Use a conditional statement to compare two values.
if 9 > 1:
    print("9 is greater than 1")

# 18. Check if a number is divisible by 3 and 5.
if 30 % 3 == 0 and 30 % 5 == 0:
    print("Divisible by both")

# 19. Write a program to find the maximum of three numbers.
print(max(20, 30, 40))

# 20. Write a program to find the factorial of a number using a loop.
factorial = 1
num = 5
for i in range(1, num + 1):
    factorial *= i
print(factorial)

# String Manipulation
# 1. Print the length of a string.
string = "Hello, World!"
print(len(string))

# 2. Concatenate two strings.
string_part1 = "hello "
string_part2 = "world"
print(string_part1 + string_part2)

# 3. Repeat a string three times.
print(string * 3)

# 4. Access the first character of a string.
print(string[0])

# 5. Access the last character of a string.
print(string[-1])

# 6. Slice a string to get the first three characters.
print(string[:3])

# 7. Convert a string to uppercase.
print(string.upper())

# 8. Convert a string to lowercase.
print(string.lower())

# 9. Check if a string starts with a specific letter.
print(string.startswith("H"))

# 10. Check if a string ends with a specific letter.
print(string.endswith("!"))

# 11. Find the index of a substring in a string.
print(string.find("e"))

# 12. Replace a word in a string with another word.
print(string.replace("World", "Sarun"))

# 13. Split a string into a list of words.
string = "hello world"
print(string.split())

# 14. Join a list of strings into a single string.
words = ["hello", "world"]
print(" ".join(words))

# 15. Remove whitespace from both ends of a string.
print(" hello ".strip())

# 16. Check if a string is alphanumeric.
print("hello456".isalnum())

# 17. Reverse a string.
print(string[::-1])

# 18. Count the occurrences of a character in a string.
print(string.count("l"))

# 19. Format a string using f-strings.
name, age = "Sarun", 20
print(f"My name is {name}, and I am {age} years old.")

# 20. Write a program to check if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))


