

# make a string
string = 'this is a string'
a_list_of_strings = string.split(" ")
a_list_of_strings[0]
a_list_of_strings[2]

#create function
def print_hello():
    print('hello world')

print_hello()

#rename function + combine function 
new_name = print_hello
new_name()

#new function, adding hello after each string
def add_hello_to_string(string):
    return string + "hello"

add_hello_to_string("test")

# Task 1 - Creat string which uses addition
"westworld" + " " + "rocks"

# Task 2 - Multiplication

("westworld" + " " + "rocks"+ " ") * 10

# Task 3 - use at least one object method
'hej'.capitalize()

# Task 4 - def a function taking two numbers, printing both the sum and the calculation
def calculator(x,y):
    answer = x + y
    print(f"{x}+{y}+{answer}")

calculator(2,5)