# # # Week3
# # # This week we will work on :
# # # Working With Strings


# # # 1.   Working With Numbers
# # # 2.   Getting Input From Users




# # # 1.   Building a Basic Calculator
# # # 2.   Mad Libs Game




































# # # Review
# # create variables for the following :
# # 1. age
# age=input ("how old are you")
# #2. name
# name=input ("what is your name?") 
# # 3. song
# song = input ( "what is your favorite song?")
# # 4. food
# food= input(" what is your favorite food?")
# # 5. number
# number= input (" what is your favorite number?")


# # #now include the variables you just made print in the following...
# print ("I am"+ age)
# print ("my name is Ashley"+ name)
# print ("my favorite song is When I was Your Man By Bruno Mars"+ song)
# print ("my favorite food is pambasos"+ food)
# print ("my favorite number is"+ number)

# # Once upon a time, there was a [age] old coder named [name].
# print (" once upon a time, there was a "+ str(age)+"old coder named"+,name +".")
# #f string 
# print(f" once upon a time, there was a "+ {age}+"old coder named"+,name +".")
# # [name] liked to hum the song [song] while coding. It was so annoying that their teammates would throw [food] until [name] would stop singing.
# print (name+"like to hum to the song "+ song + "while coding. it was so annoying that there teammates would throw " + food + "until"+ name + " would stop singing")


# # Still, [name] was the best coder on the team and could write [number] lines of code every day. Maybe [song] was [name]’s secret power?
# ##########################################################################################
# print (f "still"+ name +"was the best coder on the team and could write" + number + "lines of code every day. Maybe "+ song +"was"+ name+"secret power?")


















# ##########################################################################################
# # The names you use when creating these labels need to follow a few rules:
# # 1. Names can not start with a number.
# # 2. There can be no spaces in the name, use _ instead.
# # 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# # 4. It's considered best practice (PEP8) that names are lowercase.
# # 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
# #    or 'I' (uppercase letter eye) as single character variable names.
# # 6. Avoid using words that have special meaning in Python like "list" and "str"


# # Here are some exercises to practice the rules:


# # Correcting Invalid Names: Below are some invalid names. Correct them according to the rules:


# # FirstName
# # last_name
# # email_address
# # percent
# # variable_name
# # Zero
# # list_of_names
# # Creating Valid Names: Create valid names for the following descriptions:


# # The first name of a person
# # The last name of a person
# # The email address of a person
# # The percentage of marks obtained by a student
# # A variable to store the number of items in a shopping cart




# # Identify Valid and Invalid Names: Identify which of the following names are valid or invalid according to the rules:


# # first_name
# # lastName
# # email_address
# # percentage
# # variable_name
# # First_variable
# # emailaddress
# # percentage
# # Illinois
















# ############################################################################################


# # # **Working with** **numbers** **bold text**
# # We'll learn about the following topics:
# # 1. Types of Numbers in Python
# # 2. Basic Arithmetic
# # 3. Differences between classic division and floor division


# # Python has various "types" of numbers (numeric literals).
# # 1. We'll mainly focus on integers and floating point numbers.
# # Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
# # 2. Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.


# ##########################################################################################
# # #addition
print (2+2)
# # #multiplication
print (2*2)
# # #division
print (2/2)
# # #modulo
print (2%2) # remainder of the division 
# # #powers 
print (2**2)
# # #get the max and min of a number
print (max(2,3)) # max number
print (min(2,3)) #min number 
# # #round a number
print (round(2.5)) # rounds number to the nearest whole number 
# # # absolute value
print (abs(-2)) # absolute value of the number always positive
# # # order of operations
print( 2+ 10 * 10 +3 ) # order of opertaions 
# # #to do more you need to import special math libraries from python
from math import *    
# # #this goes out and grabs some different math functions we can use
# # #floor method
print( floor (3.7)) # floor method 
print (floor(3.3)) # floor method round up
print (floor(3.9)) # floor method 
# floor means it will always round down. 
# # #ceil method
print ( ceil( 3.7)) # ceil method round down 
print (ceil(3.3)) # ceil method 
# ceil means it will always round up 
# # #sqrt method
print (sqrt(36)) # square root method 
# # sqrt method means it will find the square root of the number which is the number multiplied by its given number 










# ##########################################################################################
# # So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
# # # **Getting Input from users**
# # #how do we get input from users?
# # input("what is your name?")
# # # basic math calculator
# # #ask the user for 2 numbers
# # # print out a statement where you:
# # # add them together
# # #multiply
# # # find the max number
# # # find the remainder of the numbers
# # #round one number








# ##########################################################################################
# # # mad libs game
# # print("Roses are {color}")
# # print("{plural noun} are blue")
# # print("I love {celebrity}")
# # # On to codehs.com







