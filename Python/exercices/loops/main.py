# Write a for loop so that every item in the list is printed.
item_list = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]

for items in item_list:
    print(items)


# Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"
item_list = ["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]

for items in item_list:
    print(f"Hello!, {items}")


# Write a for loop that iterates through a string and prints every letter.
word = "Antarctica"

for letters in word:
    print(letters)


# Using a for loop and .append() method append each item with a Dr. prefix to the lst.
lst1 = ["Phil", "Oz", "Seuss", "Dre"]
lst2 = []

for items in lst1:
    lst2.append("Dr. " + items)

print(lst2)


# Write a for loop which appends the square of each number to the new list.
lst1 = [3, 7, 6, 8, 9, 11, 15, 25]
lst2 = []

for number in lst1:
    lst2.append(number**2)

print(lst2)


# Write a for loop using an if statement, that appends each number to the new list if it's positive.
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []

for number in lst1:
    if number < 0:
        lst2.append(abs(number))


print(lst2)


# Using for loop and if statement, if the value is < than 1500, should be added to the new list.
dict1 = {"z1": 900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
value_dict = dict1.values()

final_list = []

for value in value_dict:
    if value < 1500:
        final_list.append(value)

print(final_list)


# Write a for loop which appends the type of each element in the first list to the second list.
lst1 = [3.14, 66, "Teddy Bear", True, [], {}]
lst2 = []

for items in lst1:
    lst2.append(type(items))

print(lst2)
