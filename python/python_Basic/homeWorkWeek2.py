
#   IF_CONDITION

#1. Check if a num is positive.

num = 20
if num > 0:
    print("The num is positive.")


#2. Check if a num is even.

if num % 2 == 0:
    print("The num is even.")


#3. Check if a num is divisible by 5.

if num % 5 == 0:
    print("The num is divisible by 5.")


#4. Check if a string starts with "A".

me_me_text = "Apend"
if me_me_text.startswith("A"):
    print("The string starts with 'A'.")


#5. Check if a variable is greater than 100.

value = 101
if value > 100:
    print("The value is greater than 100.")


#6. Check if a list contains more than 5 elements.

me_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if len(me_list) > 5:
    print("The list contains more than 5 elements.")


#7. Check if a variable is of type `int`.

num = 42
if isinstance(num, int):
    print("The variable is an integer.")



#8. Check if a given character is a vowel.

char = 'i'
if char in "aeiouAEIOU":
    print("The character is a vowel.")


#9. Check if a year is a leap year.

year = 2025
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")


#10. Check if a num is a multiple of 10.
num = 20
if num % 10 == 0:
    print("The num is a multiple of 10.")


#11. Check if a string contains the word "".

sentence = "I love Python programming."
if "Python" in sentence:
    print("The string contains the word 'Python'.")


#12. Check if a num is within the range 1 to 100.

num = 69
if 1 <= num <= 100:
    print("The num is within the range 1 to 100.")


#13. Check if a tuple is empty.

me_tuple = ()
if not me_tuple:
    print("The tuple is empty.")


#14. Check if a dictionary has a specific key.

me_dict = {"name": "Joe", "age": 25}
if "name" in me_dict:
    print("The dictionary has the key 'name'.")



#15. Check if a num is negative.
num = -1
if num < 0:
    print("The num is negative.")


#16. Check if a string length is greater than 5.
me_me_text = "helloworld"
if len(me_me_text) > 5:
    print("The string length is greater than 5.")


#17. Check if the sum of two nums is greater than 50.

a, b = 69, 42
if a + b > 50:
    print("The sum of the nums is greater than 50.")


#18. Check if a list contains the num 7.

if 7 in me_list:
    print("The list contains the num 7.")


#19. Check if a variable is not `None`.

variable = "Hello"
if variable is not None:
    print("The variable is not None.")


#20. Check if a string ends with a period (`.`).

if sentence.endswith("."):
    print("The string ends with a period.")





#   IF-ELSE

#1. Check if a num is positive or negative.
num = -20
if num > 0:
    print("The num is positive.")
else:
    print("The num is negative.")

#2. Check if a num is even or odd.
if num % 2 == 0:
    print("The num is even.")
else:
    print("The num is odd.")

#3. Check if a string is empty or not.
me_me_text = "hello world"
if len(me_me_text) == 0:
    print("The string is empty.")
else:
    print("The string is not empty.")

#4. Check if a num is divisible by 3.
if num % 3 == 0:
    print("The num is divisible by 3.")
else:
    print("The num is not divisible by 3.")

#5. Check if a variable is a boolean or not.
num = True
if isinstance(num, bool):
    print("The variable is a boolean.")
else:
    print("The variable is not a boolean.")

# 6. Check if a string starts with a capital letter.
me_me_text = "Hello world"
if me_me_text[0].isupper():
    print("The string starts with a capital letter")
else:
    print("The string does not start with a capital letter.")

#7. Check if the length of a list is even or odd.
me_list = [1, 2, 3, 4, 5, 6 ,7 ,8, 9]
if len(me_list) % 2 == 0:
    print("The length of the list is even.")
else:
    print("The length of the list is odd.")

# 8, Check if a num is prime or not.
num = 9
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("The num is not prime.")
            break
    else:
        print("The num is prime.")
else:
    print("The num is not prime.")

#9. Check if a year is a leap year or not.
year = 2025

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

#10. Check if a num is in a list.
if 9 in me_list:
    print("The num is in the list.")
else:
    print("The num is not in the list.")

#11. Check if a num is greater than 10 or not.
if num > 5:
    print("The num is greater than 10.")
else:
    print("The num is not greater than 10.")

#12. check if two nums are equal or not.

a, b = 11, 11
if a == b:
    print("The nums are equal.")
else:
    print("The nums are not equal.")

#13. Check if a nufiber)is-divisible by both 3 and 5.
num = 30
if num % 3 == 0 and num % 5 == 0:
    print("The num is divisible by both 3 and 5.")
else:
    print("The num is not divisible by both 3 and 5.")

#14, Check if a string contains only alphabets.
me_me_text = "Hello123world"
if me_me_text.isalpha():
    print("The string contains only alphabets.")
else:
    print("The string does not contain only alphabets.")

#15. Check if the first character of a string is uppercase or lowercase.
me_me_text = "Banana"
if me_me_text[0].isupper():
    print("The first character is uppercase.")
else:
    print("The first character is lowercase.")

#16. Check if a string contains spaces or not.
me_me_text = "hello world"
if " "in me_me_text:
    print("The string contains spaces.")
else:
    print("The string does not contain spaces.")

#17. Check if the absolute value of a num is greater than 10.
num = 100
if abs(num) > 10:
    print("The absolute value of the num is greater than 10.")
else:
    print("The absolute value of the num is not greater than 10.")

# 18. Check if the length of a string(is\exactly 8 characters.
me_me_text = "helloworld!"
if len(me_me_text) == 9:
    print("The string has exactly 8 characters.")
else:
    print("The string does not have exactly 8 characters.")

#19. Check if a file path ends with >.txt™.
file_path = "example.txt"
if file_path.endswith(".txt"):
    print("The file path ends with .txt.")
else:
    print("The file path does not end with .txt.")

# 20. Check if the temperature is above or below freezing point.
temperature = -50
if temperature >= 0:
    print("The temperature is above freezing point.")
else:
    print("The temperature is below freezing point.")




#   IF-ELIF-ELSE

#1. Check if a num is positive, negative, or zero.
num = 1
if num > 0:
    print("The num is positive.")
elif num < 0:
    print("The num is negative.")
else:
    print("The num is zero.")

#2. Check if a num is small (<10), medium (10-100), or large (>100).
num = 69
if num < 10:
    print("The num is small.")
elif 10 <= num <= 100:

    print("The num is medium.")
else:
    print("The num is large.")


#3. Grade a student based on their scone.(A} B, C, D, F)-
score = 69
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: 8")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# 4. Check the season based on the month num.
month = 1
if month in [12, 1, 2]:
    print("Season: Winter")
elif month in [3, 4, 5]:
    print("Season: Spring")
elif month in [6, 7, 8]:
    print("Season: Summer")
else:
    print("Season: Autumn")


#5. Determine if a person is a child, teenager, adult, on senior.
age = 20
if age < 13:
    print ("Child")
elif 13 < age < 20:
    print("Teenager")
elif 20 <= age < 60:
    print("Adult")
else:
    print("Senior")

#6. Determine if a day is a weekday or weekend.

day = "Saturday"

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Weekday")

elif day in ["Saturday", "Sunday"]:
    print("Weekend")

else:
    print("Invalid day")

#7. Check if a year is ancient (<19@0), modern (1900-2000), or recent (>200@).
year = 2025
if year < 1900:
    print ("Ancient")
elif 1900 <= year <= 2000:
    print("Modern")
else:
    print("Recent")

# 8. Determine if a string is short, medium, or long based on its length.
me_me_text = "Hello World."
if len(me_me_text) < 5:
    print("Short")
elif 5 < len(me_me_text) < 10:
    print ("Medium")
else:
    print ("Long")



#9. Classify a num as even, odd, or zero.
num = 9
if num == 0:
    print("The num is zero.")
elif num % 2 == 0:
    print("The num is even")
else:
    print("The num is odd.")

#10. Determine the price category based on product cost.
price = 75
if price < 2:
    print("Cheap")
elif 20 <= price <= 100:
    print("Affordable")
else:
    print ("Expensive")

#11. Classify an angle as acute, right, obtuse, or straight.
angle = 180
if angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
elif 90 < angle < 180:
    print("Obtuse angle")
else:
    print("Straight angle")

# 12. Classify a triangle based on side lengths.
a, b, c = 4, 5, 6
if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


#13. Check if a character is a vowel, consonant, or other.
char = "e"
if char.lower() in "aeiou":
    print ("Vowel")
elif char.isalpha():
    print ("Consonant")
else:
    print ("Other")

#14. Check if a num is a single digit, double digit, or larger.
num = 69
if 0 <= num < 10:
    print("Single digit")
elif 10 <= num < 100:
    print("Double digit")
else:
    print("Larger than double digit")

#15. Determine a traffic light color’s action (red, yellow, green).

Light = "green"
if Light.lower() == "red":
    print("Stop")
elif Light.lower() == "yellow":
    print ("Caution")
elif Light.lower():
    print("Go")
else:
    print("Invalid light color")

# 16. Classify 2 temperature as cold, warm, or hot.

temperature = 50
if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 30:
    print("Warm")

else:
    print("Hot")


# 17. Determine a student's result: pass, merit, or distinction.
marks = 69
if marks < 50:
    print("Fail")
elif 50 <= marks < 75:
    print("Pass")

elif 75 <= marks < 90:
    print("Merit")

else:
    print ("Distinction")


# 18. Classify an animal as mammal, bird, or reptile.
animal = "parrot"
if animal in ["dog", "cat", "human"]:
    print ("Mammal")
elif animal in ["eagle", "parrot", "penguin"]:
    print ("Bird")
elif animal in ["snake", "lizard", "turtle"]:
    print ("Reptile")
else:
    print("Unknown category")



# 19. Determine if a vehicle is(a\bike,) Car, or truck.

vehicle = "bike"
if vehicle == "bike":
    print("Two-wheeler")
elif vehicle == "car":
    print("Four-wheeler")
elif vehicle == "truck":
    print("Heavy vehicle")
else:  
    print("Unknown vehicle type")


# 20. Classify a sports player as beginner, intermediate, or advanced.
experience = 9
if experience < 1:
    print ("Beginner")
elif 1 <= experience <= 3:
    print("Intermediate")
else:
    print ("Advanced")





#   NESTED CONDITIONALS

 #1. Check if a num is positive and even.
num = 42

if num > 0:
    if num % 2 == 0:
        print("The num is positive and even.")
    else:
        print("The num is positive but odd.")
else:
    print("the num is not positive.")


 # 2. Check if a num is negative and divisible by 3.
num = -50
if num < 0:
    if num % 3 == 0:
        print("The num is negative and divisible by 3.")
    else:
        print("The num is negative but not divisible by 3.")
else:
    print("The num is not negative.")



#3. Check if a year is(a)leap year and divisible by 100.
year = 2025
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if year % 100 == 0:
        print("The year is a leap year and divisible by 100.")
    else:
        print("The year is a leap year but not divisible by 100.")
else:
    print("The year is not a leap year.")



# 4. Check if a string starts with
me_me_text = "Amazon"
if me_me_text.startswith("A"):
    if me_me_text.endswith("Z"):
        print("The string starts with ‘A’ and ends with 'Z'")
    else:
        print("The string starts with ‘A’ but does not end with 'Z'")
else:
    print("The string does not start with 'A'.")




#5. Check if @ num is even and greater than 50.

num = 69
if num % 2 == 0:
    if num > 50:
         print ("The num is even and greater than 50.")
    else:
        print ("The num is even but not greater than 50.")
else:
    print ("The num is not even.")

#6. Check if a variable is not “None” and is of type “ste"
me_string = "Hello World"
if me_string is not None:
    if isinstance(me_string, str):
        print("The variable is not None and is a string.")
    else:
        print("The variable is not None but is not a string.")
else:
    print("The variable is None.")

#7. Check if a string length is greater than 10 and contains the word “Python”.

me_me_text = "I love Python programming."
if len(me_me_text) > 10:
    if "Python" in me_me_text:
        print ("The steing length is greater than 10 and contains 'Python'")
    else:
        print ("The string length is greater than 10 but does not contain ‘Python’")
else:
    print ("The string length is not greater than 10.")

# 8. Check if a list 4s not empty and has more than 5 elements.
me_list = [1, 2, 3, 4, 5, 6]
if me_list:
    if len(me_list) > 5:
        print ("The List is not empty and has more than 5 elenents.")
    else:
        print("The list is not empty but has 5 or fewer elements.")
else:
        print("The list is empty.")


#9. Check if a num is divisible by 2, 3, and 5.
num = 69
if num % 2 == 0:
    if num % 3 == 0:
        if num % 5 == 0:
            print("The num is divisible by 2, 3, and 5.")
        else:
            print("The num is divisible by 2 and 3 but not by 5.")
    else:
        print("The nunber is divisible by 2 but not by 3.")
else:
    print("The num is not divisible by 2.")

#10. Check if a person is eligible to vote based on age and citizenship.
age = 20
citizenship = "Cambodia"
if age >= 18:
    if citizenship == "Cambodia":
        print("The person is eligible to vote.")
    else:
        print("The person is not a citizen.")
else:
    print("The person is not old enough. to vote.")

#11. Check if a student passed both Math and Science exams.
math_score, science_score =69 , 96
if math_score >= 50:
    if science_score >= 50:
        print("The student passed both Math and Science.")
    else:
        print("The student passed Math but failed Science.")
else:
    print("The student failed Math.")


# 12. Check if a person is eligible for a senior discount (age > 60) and a loyalty program.
age = 69
loyalty = True

if age > 60:
    if loyalty:
        print("The person is eligible for a senior discount and loyalty program.")
    else:
        print("The person is eligible for a senior discount but not loyalty program.")
else:
    print("The person is not eligible for a senior discount.")

# 13. Check if a file path ends with `.py` and starts with `project_`.
file_path = "project_main.py"
if file_path.endswith(".py"):
    if file_path.startswith("project_"):
        print("The file path ends with '.py' and starts with 'project_'.")
    else:
        print("The file path ends with '.py' but does not start with 'project_'.")
else:
    print("The file path does not end with '.py'.")

# 14. Check if a triangle is equilateral and right-angled.
a, b, c = 4, 5, 6
if a == b == c:
    print("The triangle is equilateral.")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("The triangle is right-angled.")
else:
    print("The triangle is neither equilateral nor right-angled.")

# 15. Check if a string contains uppercase letters and digits.
me_text = "Hello123World"
if any(char.isupper() for char in me_text):
    if any(char.isdigit() for char in me_text):
        print("The string contains both uppercase letters and digits.")
    else:
        print("The string contains uppercase letters but no digits.")
else:
    print("The string does not contain uppercase letters.")

# 16. Check if a dictionary has a specific key and value.
my_dict = {"name": "John", "age": 30}
if "name" in my_dict:
    if my_dict["name"] == "John":
        print("The dictionary has the key 'name' with value 'John'.")
    else:
        print("The dictionary has the key 'name' but with a different value.")
else:
    print("The dictionary does not have the key 'name'.")

# 17. Check if a number is odd and within the range 1-100.
number = 42
if number % 2 != 0:
    if 1 < number <= 100:
        print("The number is odd and within the range 1-100.")
    else:
        print("The number is odd but not within the range 1-100.")
else:
    print("The number is not odd.")

# 18. Check if a string starts with "H", contains "e", and ends with "o".
me_text = "Hello"
if me_text.startswith("H"):
    if "e" in me_text:
        if me_text.endswith("o"):
            print("The string starts with 'H', contains 'e', and ends with 'o'.")
        else:
            print("The string starts with 'H' and contains 'e' but does not end with 'o'.")
    else:
        print("The string starts with 'H' but does not contain 'e'.")
else:
    print("The string does not start with 'H'.")

# 19. Check if a tuple contains exactly 3 elements, all integers.
me_tuple = (2, 3, 4)
if len(me_tuple) == 3:
    if all(isinstance(x, int) for x in me_tuple):
        print("The tuple contains exactly 3 elements, all integers.")
    else:
        print("The tuple contains 3 elements but not all are integers.")
else:
    print("The tuple does not contain exactly 3 elements.")

# 20. Check if a number is divisible by 4 and not divisible by 8.
number = 69
if number % 4 == 0:
    if number % 8 != 0:
        print("The number is divisible by 4 and not divisible by 8.")
    else:
        print("The number is divisible by 4 and also divisible by 8.")
else:
    print("The number is not divisible by 4.")
