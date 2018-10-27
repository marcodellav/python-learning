# Using f-strings (only Python >= 3.6). A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. Instead of using empty placeholders {} we insert the variable name(s) within the brackets

greeting = 'Good Afternoon'
name = 'Marco Della Vedova'

message = f'{greeting}, {name.upper()}. Welcome!'

print(message)
