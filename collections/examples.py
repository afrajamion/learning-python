# Lists
# ordered, mutable
fruits = ["apple", "pear", "banana", "plum", "cherry", "orange"]
print(fruits[0])
newfruits = ["strawberry", "grape", "blackcurrant"]
fruits.extend(newfruits)
fruits = map(lambda x: x.capitalize() if x == "pear" else x, fruits)
fruits[2] = 'grape'
fruits.sort(key = lambda x: x.count('r'), reverse = True)

# Tuples
# ordered, immutable
fruits_tuple = ("apple", "pear", "banana")
a, b, c = fruits_tuple
print(a, b, c)

# Dictionaries
# > 3.6: ordered, mutable
countries = {'UK':'London', 'France':'Paris', 'Belgium':'Brussels'}
print(list(countries.items()))
print(countries['Belgium'])
print(countries.pop('UK'))
print(countries.get('Germany', 'Not found'))

# Sets
# unordered, mutable
my_set = {3, 4, 2, 1, 5, 3, 2}
my_set.add(6)
my_set.discard(7)
print(my_set)