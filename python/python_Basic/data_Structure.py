#1. Create a list of five numbers and print it.
num = [2, 4, 6, 8, 10]
print(num)
#2. Append an element to a list.
num.append(10)
print(num)
#3. Insert an element at the beginning of a list.
num.insert(4,10)
print(num)
#4. Remove an element from a list by value.
num.remove(0)
print(num)
#5. Remove an element from a list by index.
num.pop(3)
print(num)
#6. Sort a list in ascending order.
num.sort()
print(num)
#7. Reverse a list.
num.reverse()
print(num)

#8. Create a dictionary with three key-value pairs.
dictionary = {"name" : "Sarun",
              "age" : 20,
              "job" : "Computer scientist"
              }

#9. Access a value in a dictionary using its key.
print(dictionary["name"])
#10. Add a new key-value pair to a dictionary.
dictionary["location"] = "Cambodia"
#11. Remove a key_value pair from a dictionary.
del dictionary["age"]
#12. Create a tuple with five elements.
me_Tuple = (2, 4, 6, 8)
#13. Access the second element of a tuple.
print(me_Tuple[0])
#14. Unpack a tuple into separate variables.
a, b, c, d, e, f = me_Tuple
#15. Create a set and add an element to it.
me_Set = {2 ,4 ,6}
#16. Remove an element from a set.
me_Set.remove(1)
#17. Check if an element exists in a set.
print(4 in me_Set)
#18. Perform a union operation on two sets.
setA = {2,4,6,8}
setB = {1,2,3,4}
print(setA.union(setB))
#19. Perform an intersection operation on two sets.]
print(setA.intersection(setB))
#20. Create a nested dictionay and access an inner value.
nes_Dic = {"person" : {"name" : "Sarun",
                        "age" : 20
                       }}
print(nes_Dic["person"]["name"])
