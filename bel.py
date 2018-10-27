# list

courses = ['History', 'Maths', 'Physics', 'ComputerScience']

print(courses)

print(len(courses))  # prints the total number of values in the list

print(courses[3])  # prints the 4th value (starts from 0)

print(courses[-1])  # prints the last value

print(courses[0:2])  # prints values at index 0 and 1/up to (but not including) 2

# list methods

courses.append('Art')  # appends a value to the end of the list

courses.insert(0, 'Music')  # insert takes 2 arguments: the position were it inserts and the value to insert

# the extend method

courses_2 = ['Literature', 'Philosophy']  # defining another list with more values

# if we used the insert method to add all the values in courses_2 to the courses list we would get a list within a list, so we use extend instead

courses.extend(courses_2)

print(courses)

# Removing values

courses.remove('Maths')

# courses.pop()  # the pop method removes the last value from the list, useful when using the list like a stack/queue

popped = courses.pop()  # pop returns the value that it removed

print(popped)

# Sorting lists

courses.reverse()  # reverses the order of the values

courses.sort()  # sorts alphabetically, works with numbers as well

courses.sort(reverse=True)

print(courses)

# the sorted function (as opposed to the sort method) is useful when we don't want to modify the original list

sorted_courses = sorted(courses)

print(sorted_courses)

print(min(courses))  # or max prints the first or last (alphabetically) value. sum can also be used with numerical values

print(courses)

print(courses.index('Music'))  # to find out the index of a value that exist in a list

print('Art' in (courses))  # returns True/False if the value is in the list (or not)

# for loop with enumerate function to print the values of the list and the index, in this case starting from 1

for index, course in enumerate(courses, start=1):
    print (index, course)

# if we want to turn a list into a string of comma separated values, with the join method

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)
