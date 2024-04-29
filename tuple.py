# How to add more than one item and deleting an item in a tuple
one_tuple = ('orange', 34.46, 'mango', 44, '45', [3,5,4,'laura'], (0.33, 0.55, 78.457))
first_list = list(one_tuple)
first_list.append('fruits')
first_list.extend(['Anitab', 'Lovelace', 'Akirachix'])
one_tuple = tuple(first_list)
print(one_tuple)

# how to add an item in a list within a nested tuple
one_tuple[5].append(20)
print(one_tuple)
# how to insert items in a list within nested tuple
one_tuple[5][0] = 'Ilara'
print(one_tuple)

# how to delete an item in a tuple
first_list = list(one_tuple)
first_list.pop()
one_tuple= tuple(first_list)
print(one_tuple)

# how to access items in tuple
print(one_tuple[6])
print(one_tuple[5][2])
print(one_tuple[2])
print(-4)

# how to slice a tuple
print(one_tuple[4:5])
print(one_tuple[-4:])
print(one_tuple[-5:-2])

# how to find the length of a tuple
print(len(one_tuple))
# how to concatenate two tuple
two_tuple = ('book',True, 36.897785, 784, 'pens',(10,20,30,40))
print(one_tuple + two_tuple)
Name_tupple = ("Laura", "Nyaaga", "Terry", "Viavian")
print(Name_tupple)
# an example of tupple

print(Name_tupple[1])
print(Name_tupple[3])
print(Name_tupple[-1])
print(Name_tupple[-3])
# Accesing an item

print(Name_tupple[1:3])
print(Name_tupple[2:-1])
# slicing an item

for a in Name_tupple:
    print(a)
old_tupple = [i for i in Name_tupple]
print(old_tupple)
# looping in tupple

New_tupple = (1, 2, "dog", 3, "cow", 4, "cat")
New_list = list(New_tupple)
New_list.append(34)
added_List = tuple(New_list)
print(added_List)
# How to add to an item

tuple = (1,2,3)
del tuple
print(tuple)
#how to delete


