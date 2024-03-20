# create empty list
my_list = []

# append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert the value 15
my_list[1] = 15

# Extend another list
my_list2 = [50,60,70]

my_list.extend(my_list2)

# remove the last element from my_list
print(my_list.remove(40))

# Sort my_list
print(my_list.sort())

# Find and print the index of value 30
print(my_list.index(30))

