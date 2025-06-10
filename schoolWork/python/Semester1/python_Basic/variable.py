#1 . Declear a variable and assign it your name.
name = "Sun Sarun"
print(name)

#2 . Create two variables and assign then integer values, then print their sum
a ,b = 42 ,69
print(a + b)

#3 . Swap the values of two variables without using a third variable.
a, b = 42, 69
print(f"before swap a = {a}, b = {b}")
a, b = b, a
print(f"before after Swap a = {a}, a = {a}")

#4 . Assign a floating-point number to a variable and display it.
a = 3.14
Print("floatingPoint =",a)

#5. Assign a boolean value to a variable and print it.
a = True
print("Boolean Vaule =",a)

#6. Update the value of a variable and print the updated value.
a = 24
print("before update = ",a)
a = 42
print("before after update = ",a)

#7. Declare a constant-like variable using uppercase and demonstrate why Python allows updates.
import math
print("defualt value of pi :",math.pi)
math.pi = 3
print("update value of pi :",math.pi)

#8. Create a variable with a null value and then assign it a string.
a = none
print("unassigned =",A)
a = 19
print(a)

#9. Create three variables in a single line with the same value.
a, b, c = 69

#10. Create three variables in a single line with different values.
a, b, c = 2, 3, 4

#11. Assign multiple types (int, float, string) to variables and print their types.
a = 69
b = 42.2
c = "string"
print(type(a), type(b), type(c))

#12. Create a variable with a string containing your name and age using placeholders.
name = "sarun"
age = 20
info = f"My name is {name}, and i am {age} years old.")

#13. Use the del keyword to delete a variable and try accessing it after deletion.
a = 69
del a

#14. Use type hinting to declare a variable and assign it a value.
name : "jonh"
age : 30
print(name, age)

#15. Assign the same value to multiple variables and verify their memory addresses.
a = b = 69
print(id(a), id(b))

#16. Assign a value to a variable using an expression.
a = 5 * 5
print("express a",a)

#17. Print a variable without assigning it a value.
value
print(value)

#18. Assign a list of numbers to a variable and print the sum of its elements.
num = [1,2,3,4,5]
print(sum(num))

#19. Create a variable inside a function and try accessing it outside.
def funk():
    local_a = 69
print(local_a)

#20. Use global and local variables in a small function example.
global_a = 69
def mod_funk()
    global global_a = 42
mod_funk()
print(global_a)

