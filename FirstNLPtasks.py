# Task 1 - Defining a function called calculator
def calculator(x,y):
    answer = x+y
    print(answer)

calculator(-1,8)

#check that it works with floating numbers
calculator(1.2,5.09)

# Task 2 - define a function with two diff. types + count
def character_counter(my_string_variable,my_letter_variable):
    total_count = my_string_variable.upper().count(my_letter_variable.upper())
    print(total_count)

character_counter('Vasketøj','v')

#displaying what the .upper() function actually does
'vasketøj'.upper()

# Task 3 - define isEven function which prints boolean values 
def is_even(int_number):
    my_answer=int_number %2 == 0
    return(my_answer)

is_even(12)
is_even(19)

# Task 3 - Count even numbers using is_even function 
def is_even_list(my_list):
    answer_list = []
    for i in my_list:
        even = is_even(i)
        answer_list.append(even)
    print(answer_list.count(True))

is_even_list([1,3,6,7,21,7,9,5])

# Task 4 - find the highest number in list n
def find_largest(the_list):
    highest_num = max(the_list)
    print(highest_num)

find_largest([124,2435,67,87,652,1,56,954])

# Task 5 - String and Loops
my_string = "Thisdoesntwork"

#index = 0
#len(my_string)
#letter = my_string[0]

print(my_string[::1])


# Task 6 - Dictionary - first defining 
dict = {
    "class": "NLP",
    "student": "Me",
    "year": "2019"
}
print(dict)

#printing all key names in dictonary in a list
for x in dict: 
    print(x)

