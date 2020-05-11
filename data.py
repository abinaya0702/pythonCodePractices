#printing the list after adding an element to each
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list1.append(11)
list2.append(12)
print(list1)
print(list2)

#accessing one element from a tuple
tuple1 = (21,31,41,51)
print(tuple1)
print(tuple1[2])

#deleting an element from a dictionary
dict = {"Hello":1 , "to": 2, "everyone":3}
print(dict)
del dict["to"]
print("the dictionary after deleting an element:")
print(dict)
