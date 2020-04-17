# square brackets ([]) indicate a list, and individual elements in the list are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# Zero 0 index
print(bicycles[0])
print(bicycles[0].title())
# last item -1
print(bicycles[-1].title())
print(f"My 1st bycile is {bicycles[-1].title()}!")
print("=========Exercise==========")
# print all name in list
names = ["John", "Anrea", "Caitlyn"]
print(names)
for name in names:
    print(name)
# print greeting message
for name in names:
    print(f"Hello {name}!")
# Changing, adding, and removing elements
# Modifying Elements in a List
names[0] = "Dung"
print(names)
# Adding Elements to a List
# Adding Elements to the End of a List
names.append("Nguyen")
print(names)
motocycles = []
motocycles.append("Honda")
motocycles.append("yamaha")
motocycles.append("suzuki")
print(motocycles)
# Inserting Elements into a List
motocycles.insert(0, "Ducati")
print(motocycles)
# Removing Elements from a List
origin_motocylces = motocycles
print(origin_motocylces)
del motocycles[0]
print(motocycles)
# or using pop, remove the last item of list and store it
print("===============")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# poping from any position
motorcycles = ['honda', 'yamaha', 'suzuki']
second_owned = motorcycles.pop(1)
print('The second motorcycle I owned was a ' + second_owned.title() + '.')
# remove item by value.The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have been removed
print("===============")
print("remote ducati from list!")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# orgnizing a list
print("===============Organizing List===================")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
cars.sort(reverse=True)
print(cars)
# Organizing without changijg the index (sort)
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
# reverse
print(cars)
cars.reverse()
print(cars)
# length

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# exercise
# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit
# •	 Store the locations in a list Make sure the list is not in alphabetical order
# •	 Print your list in its original order Don’t worry about printing the list neatly,
# just print it as a raw Python list
# •	 Use sorted() to print your list in alphabetical order without modifying the
# actual list
# •	 Show that your list is still in its original order by printing it
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
# •	 Show that your list is still in its original order by printing it again
# •	 Use reverse() to change the order of your list Print the list to show that its
# order has changed
# •	 Use reverse() to change the order of your list again Print the list to show
# it’s back to its original order
# •	 Use sort() to change your list so it’s stored in alphabetical order Print the
# list to show that its order has been changed
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order
# Print the list to show that its order has changed
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner
# 3-10. Every Function: Think of something you could store in a list For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least

print("==============================================")
locations = ['Hanoi', 'Danang', "Hochiminh", 'Nghean', 'Bacninh']
print(f"Original list: {locations}")
print(f"Sorted list: {sorted(locations)}")
print(f"Original list: {locations}")
print(f"Revered Sorted list: {sorted(locations, reverse=True)}")
print(f"Original list: {locations}")
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
print(f"I have visited {len(locations)} places!, including:")
i = 1
for location in locations:
    print(f"{i}. {location}")
    i += 1
