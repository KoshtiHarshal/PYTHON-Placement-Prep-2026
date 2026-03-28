# LIST
list1=[1,2,3,4,5,6]
list2=[7,8]

# TUPLE
tup1=(1,2,3,4,5,6)
tup2=(7,8)

# Print
print(list1)
print(tup1)

# Type
print(type(list1),list1)
print(type(tup1),tup1)

# Changing the values
list2[1] = 9
print(list2)
# tup2[1] = 9  <--this can't be done in tuple

# Indexing = Using index value to print value
print(list1[0],tup1[0])
print(list1[1],tup1[1])
print(list1[2],tup1[2])
print(list1[3],tup1[3])
print(list1[4],tup1[4])

# Condition = Check for item
if 3 in list1:
    print("Yes, 3 is there in the given list.")
else:
    print("nahi hai bhai list me :)")
# ------------------------------------------       
if 7 in tup1:
    print("Yes, 4 is there in the given tuple.")
else:
    print("nahi hai bhai tuple me :)")

# Slicing
print(list1[1:3])
print(tup1[:-3])


