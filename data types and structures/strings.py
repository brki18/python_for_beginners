# var1 = 10 #statement
#
# var1 = var1 + 15 # expression
#
# print(var1) # statement

text = 'This is text'
text2 = "This is also a text"

# print(text)
# print(text2)
# print(type(text))

multilineString = """This is
    multiline 
    String"""
# print(multilineString)

converted = 5
string_to_int = '10'
# print(type(converted))
# print(type(str(converted)))
# print(type(int(string_to_int)))

# year = input("Guess the current year")

# print(int(year) == 2023)

# print("\"Golf\"\n \t is my car")
concanate_string = "This is string."
additional_string = "Which is cool"

# concanate_string = concanate_string + " Everything is object in Python. " + additional_string
concanate_string += "New text" # concanate_string = concanate_string + "New text"

# print(concanate_string)

# Formatted strings
name = 'Marko'
email = 'marko@gmail.com'

# Strings are immutable
# name[2] = 'z'

# user_info = 'Your name is: ' + name + ' and you email is: ' + email
user_info = f"Your name is: {name} and your email is: {email}"
# print(user_info)

#String indexes
# print(name[2])
# print(name[0:3])
# print(name[0:])
# print(name[2:])
# print(name[::2])
# print(name[::-2])
# print(name[::-1])

# Function and methods

print("This functions") # This is function
print(name.upper())