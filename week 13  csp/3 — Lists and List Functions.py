# # Objective:
# # Students will understand how to create, modify, and access elements in Python lists.

# # Topics Covered:
# # Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# # Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)

#############################################################################################################################################################################################################################
#collections are uzed to store mutliple items in a single vauriab;e
# liosts are ordered collections of items
#lists are mutable, meaning you can change their content without changing their identity
#lists are defined by square brackets []
#items in a list can be of any data type, and a single list can contain items of different data types
#items in a list are indexed, starting from 0 for the first item, 1 for the second item, and so on
#you can also use negative indexing to access items from the end of the list, with -1 being the last item, -2 being the second last item, and so on 
lists_of_friuits = ['apple', 'banana', 'cherry', 'date']
print(lists_of_friuits[0]) #accessing the first item ['apple', 'banana', 'cherry', 'date']
print(type(lists_of_friuits)) # <class 'list'>
#accessing the last item using negative indexing
print(lists_of_friuits[0]) # apple
print(lists_of_friuits[1]) # banana
print(lists_of_friuits[-1]) # date
print(lists_of_friuits[1:3]) # ['banana', 'cherry']\
# reversing a list 2 way
lists_of_friuits.reverse()
print(lists_of_friuits) # ['date', 'cherry', 'banana', 'apple']
print(lists_of_friuits[::-1]) # [ 'apple', 'banana', 'cherry', 'date']
#appending an item to the list
lists_of_friuits.append('elderberry') #add items to the end of the list
print(lists_of_friuits) # ['date', 'cherry', 'banana',]
lists_of_friuits.extend(['fig', 'grape', 'honeydew']) #add multiple items to the end of the list
print(lists_of_friuits)
# popping items from the list
popped_item = lists_of_friuits.pop() #removes and returns the last item
print(popped_item) # honeydew
print(lists_of_friuits)
# inserting items at a specific index
lists_of_friuits.insert(1, 'blueberry') #inserts 'blueberry' at index 1
print(lists_of_friuits)
# removing a specific item by value
lists_of_friuits.remove('banana') #removes the first occurrence of 'banana'
print(lists_of_friuits)
lists_of_friuits.insert(3, 'banana') #inserts 'banana' at index 3
lists_of_friuits.sort() #sorts the list in ascending order
print(lists_of_friuits)
#why use lists? instead of individual variables to store multiple related items together, making it easier to manage and manipulate them.
# imagine you have 100 items to manage
lists_of_items=list(range(1, 1001)) #creates a list of numbers from 1 to 1000
print(lists_of_items)
print(len(lists_of_items)) #1000 items in the list
lists_of_items.extend(range(1001,2001)) #adds numbers from 1001 to 2000 to the list
print(len(lists_of_items)) #2000 items in the list

#why use lists? instead of creating seperate variables for each item, lists allow for easier data management, manipulation, and scalability, especially when dealing with large datasets.

#sets and tuples are other types of collections in Python, each with their own characteristics and use cases. Family in Python Sets examples:
set1={1, 2, 3, 4, 5}
set2={'apple', 'banana', 'cherry'}
print(set1)
print(set2)
print(type(set1)) # <class 'set'>
# why use sets instead of lists? sets automatically handle duplicate values and provide efficient membership testing, making them ideal for scenarios where uniqueness and fast lookups are required.
#examples of tuples
set_with_duplicate={1, 2, 2, 3, 4, 4, 5}
print(set_with_duplicate) # {1, 2, 3, 4,
# sets are useful for memebership testing and eliminating duplicate values from a collection
print(3 in set1) # True
print(6 in set1) # False
# # Tuples examples:
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('apple', 'banana', 'cherry')
print(tuple1)
print(tuple2)
print(type(tuple1)) # <class 'tuple'>
# why use tuples instead of lists? tuples are immutable, making them suitable for fixed collections of items that should not be changed, and they can also be used as keys in dictionaries due to their immutability.
# # Tuples are immutable, meaning once created, their content cannot be changed
# # Tuples are defined by parentheses ()
# # Items in a tuple can be of any data type, and a single tuple can contain items of different data types
# # Items in a tuple are indexed, starting from 0 for the first item, 1 for the second item, and so on
# # You can also use negative indexing to access items from the end of the tuple, with -1 being the last item, -2 being the second last item, and so on
social_security_numbers = (123456789, 987654321, 555667777)
print(social_security_numbers[0]) # 123456789

# # Practice Problems:

# # Create a list with 5 of your favorite foods.

# # Print the second and last item.

# # Add a new item using .append().

# # Remove the first item using .pop(0).

# # Reverse your list using .reverse().

# # Create a list of 3 lists (matrix), and access the middle element.