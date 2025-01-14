#1-5 . Identify the type.
print(type(69), type(2.71), type("sarun"), type(true), type(None))

#6-9 . Convert type.
print("int to float",float(69))
print("float to string",int(2.71))
print("string to int",int("69"))
print("string to list",list("sarun"))


#10-13 . Identify the type
print(type({"key" : "value"}))
print(type([1,2,3]), type((1,2,3,)), type({1,2,3}))

#14. Demonstrate how Python dynamically changes the type of a variab
a = 69 
print(a)
a = "sarun"
print(a)
#15. Check if a variable is of type integer.
print(isinstance(69, int))

#16. Create a complex number and print its real and imaginary parts.
c_num = 1 +2j
print(c_num.real, c_num.imag)

#17. Demonstrate type casting by converting a boolean to an integer.
print("bool to int",int(True))

#18. Create a variable with mixed data types using list.
mix_list = [69, "sarun", 2.71]

#19. Use isinstance() to verify a variable's data type.
print(isinstance("sarun", string)

#20. Write a program to check if an input is a number
      try:
     user_input = int(input("Enter a number:"))
        print("It is a number!")
    execpt ValueError:
        print("Not a Number.")
