# Method to edit tuple
# Tuple can be edited by using temporary list method
Tup = (1,2,3,4,5,6)
print(Tup)
temp = list(Tup)
temp.append(7)
temp.pop(3)
temp[1] = 8
Tup = tuple(temp)
print(Tup)

# Concatenation = Tuple can also be edited by Concatenating two tuples.
Tup1 = ("a","b","c","d","e")
Tup2 = ("f","g","h","i","j")
print(Tup1,"\n",Tup2) 
Tup3 = Tup1 + Tup2
print(Tup3)


# Count(),Index()&Length() Method

Tup4 = (0,1,2,1,3,1,0,2,3,2,1,0,3,2)
print(Tup4)

val1 = len(Tup4)
print("The length of Tup4 is : ",val1)

val2 = Tup4.count(1)
print("The Count of 1 in Tup4 is : ",val2)

val3 = Tup4.index(3,3,10)
print("The Count of 3 between index[3:10] in Tup4 is : ",val3)
