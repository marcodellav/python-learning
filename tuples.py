# lists are mutable, tuples are immutable, () instead of []

tuple_1 = ('History', 'Maths', 'Physics')

# sets: unordered and no duplicates, some of the main uses for sets are getting rid of duplicates and efficiently find out if a value is part of a given set. (with the intersection, difference and union methods)

set_1 = {'History', 'Maths', 'Physics'}

set_2 = {'History', 'Music'}

print(set_1.intersection(set_2))

print(set_1.difference(set_2))

print(set_1.union(set_2))

# Empty lists

empty_list = []

# same as:

empty_list = list()

# Empty tuples

empty_tuple = ()

# same as:

empty_tuple = tuple()

# Empty sets

# empty_set = {} is not correct!!!

empty_set = set()
