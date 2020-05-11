#python code to generate the positive numbers in a list
#first list
list1 = [12,-7,5,64,-14]
print("the original list")
print(list1)
no =0
print("the positive numbers:")
for no in range(0,5):
    if(list1[no]>0):
      print(list1[no], end = "," )
    no = no +1
#second list
list2 = [12,14,-95,3]
print("\nthe original list")
print(list2)
no =0
print("the positive numbers:")
for no in range(0,4):
    if(list2[no]>0):
      print(list2[no], end = "," )
    no = no +1
