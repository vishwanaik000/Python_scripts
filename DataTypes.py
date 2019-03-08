#int,float
a = 101

print(a)

type(a)

a = a + 6

a = a - 890

#float 
a = 87/12

a = a/12

#bool
flag = bool()
flag = True

#string
a = "My name is Vishu"
a.capitalize()
a.title()

b = a + " " + "and i'm cool"
b
#List
list1 = [1,2,3,4,5]
list1[0]
list1[2:4]
list1[2:]

list2 = [3,5,9,7,6,58]

list3 = list1 + list2

list3.append(14)
print(list3)
len(list3)

#hetrogenous list
list_hetro = [1,1.0,"string",[1,2,3,4]]
list_hetro[3] = "NewReplacedString"
print(list_hetro)

#tuple
tuple = tuple(list_hetro)
tuple[1]
tuple[1] = 100 #error

#set
set1 = set(list_hetro)
set1 #1.0 is ignored as copy

set_new = set([1,2,3,4,4,4,4,4,5,5,5,5])
set_new #ignores repeated values.