# functions are useful when we need to reuse code, allowing for the code to be kept DRY (Don't Repeat Yourself)


def blank_func():
    pass           # the pass keyword is used if we want to define an empty function and avoid it generating an error (SyntaxError: unexpected EOF while parsing)


def hello_func():
    return'Hello Function!'


print(hello_func().upper())  # we can 'chain' a string method such as upper to the executed function


# we add the 'greeting' parameter as a required argument of the 'hello_func_par' function, the scope of the parameter is local to the function.

def hello_func_par(greeting):
    return'{} Function!'.format(greeting)


print(hello_func_par('Hi'))

# we add a second parameter with a default value of 'You' so that it can be left blank (not required)


def hello_func_par(greeting, name='You'):
    return'{}, {}'.format(greeting, name)


print(hello_func_par('Good morning', name='Marco'))


# '*args' and '**kwargs' are conventions used when we don't have a pre-defined number of positional arguments or keyword arguments


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age='22')

# ('Math', 'Art')  a tuple with all the positional arguments is printed
# {'name': 'John', 'age': '22'} a dictionary with all the keyword values

courses = ['Math', 'Art', 'Music', 'History']  # we define a list named 'courses'
info = {'name': 'John', 'age': 22}  # we define a dictionary named 'info'

student_info(*courses, **info)  # we pass the list preceded by a '*' and the dictionary preceded by '**' and the fuction 'unpacks' the values
