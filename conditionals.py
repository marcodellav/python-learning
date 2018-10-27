language = 'JavaScript'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

# Python does not have a switch case

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:  # if both these conditions are True / we could change 'and' to 'or' if we only wanted one of the conditons to evaluate to True
    print('Admin page')
else:
    print('Bad Creds')

# 'is' evaluates to True if 2 objects have the same location in memory

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # a and b are two lists containing the same values but are not the same object in memory. If we print the variables ids, these don't match
print(id(b))

print (a == b)
print (a is b)

b = a  # a and b are the same object

print(id(a))
print(id(b))

print (a == b)
print (a is b)  # same as -> print(id(a) == id(b))
