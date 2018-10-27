# key value pairs

student = {'Name': 'John', 'Surname': 'Smith', 'Age': '25', 'Courses': ['Maths', 'ComputerScience']}

print(student['Name'], student['Surname'])

# if a key doesn't exist it will throw an error so we can use the get method, which returns 'none' or a default value

print(student.get('Phone'))  # the 'phone' key doesn't exist so the get method returns 'none'

print(student.get('Phone', 'Not Found'))  # we can specify the value to return when the key is not found

student['Accomodation'] = 'B05-F01-R09'  # we can add single key/value pairs to the dictionary, or change existing ones

student.update({'Name': 'Paul', 'Surname': 'McKenna', 'Age': '27', 'Phone': '+44 20 3666 6666'})  # the update method is useful when we want to update more than one pair in a dictionary or add keys/values to it

# del student['Age']  # to remove key/value form the dictionary

age = student.pop('Age')  # pop the age value from the dictionary and save it in a var
print(age)

print(len(student))  # prints the number of keys in the dictionary

print(student.keys())  # print the dictionary's keys

print(student.values())  # print the dictionary's values

print(student.items())  # print the dictionary's key/value pairs

for key, value in student.items():  # using the items method as otherwise only keys or values will be printed
    print(key, value)
