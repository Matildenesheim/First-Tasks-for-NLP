

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

