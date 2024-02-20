def sum(num1,num2):
    total = num1 + num2
    return total


def highest(num_list):
    highest_number = max(num_list)
    return highest_number

def vowels_check(string_input):
    vowels_amount = 0
    for i in string_input:
        vowels = ["a","e","i","o","u"]

        if i in vowels:
            vowels_amount += 1

    return vowels_amount

def identical_string(string1, string2):
    identical_strings = False
    if string1 == string2:
        identical_strings = True

    return identical_strings

def length_check(string_list):
    greater_length = []
    for i in string_list:
        if len(i) > 3:
            greater_length.append(i)

    return greater_length

def even_check(num):
    even_test = False
    if num % 2 == 0:
       even_test = True

    else:
        even_test = False 

    return even_test

def common_number(num_list1, num_list2):
    common_numbers = []
    for i in num_list1:

        if i in num_list2:
            if i in common_numbers:
                pass

            else:
                common_numbers.append(i)

    return common_numbers

        

        
addition = sum(5,6)
print(addition)

highest_number_list = highest([4,5,7,11,23,4])
print(highest_number_list)

vowels = vowels_check("Hello")
print(vowels)

string_check = identical_string("Hello","test")
print(string_check)

length = length_check(["hello","hi","test","I"])
print(length)

even_number = even_check(4)
print(even_number)

common_numbers = common_number([5,4,2,4,67,19],[10,4,5,1,3,10])
print(common_numbers)