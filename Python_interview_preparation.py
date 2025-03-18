class yogi:
    temp = "Testing Temp variable"
    def __init__(self, value1, value2):
        self.a = value1
        self.b = value2
        
    def print_value(self, temp, another_one):
        
        print(self.a, self.b,temp, another_one)
        
    # Class method used to access or operate on class defined variables using directly class.    
    @classmethod
    def get_course(cls):
        return cls.temp
    
    # Static menthods are used as utility and not associated with instancess or class state
    # this can take any parameters and 
    @staticmethod
    def welcome_message(x,y):
        return x+y
        

y = yogi(2,3)
y.print_value(4,"Testing another one")
print(yogi.get_course())
print(yogi.welcome_message(3,4))

count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()

# List , Dictionary and set Comprehension good read link 
# https://medium.com/@vinodkumargr/list-dictionary-and-set-comprehension-in-python-9823719a67da#:~:text=Set%20comprehension%20is%20a%20method,and%20add%20elements%20to%20it.

# 
# List comprehension is an elegant way to define and create lists based on existing lists.
# List comprehension is generally more compact and faster than normal functions 
# and loops for creating list. However, we should avoid writing very long 
# list comprehensions in one line to ensure that code is user-friendly.
#
# list comprehension for odd or even 
lst = [1,2,3,4,5]

sq_lst = [i*i for i in lst]

print(sq_lst)

# just only double if number is even 

sq_evn_lst = [i*i for i in lst if i % 2 == 0]
print(sq_evn_lst)

# nested list comprehension 

lt = [[j for j in range(4)] for i in range(3)]

print(lt)
# ZIP() function 
#The zip() function in Python combines multiple iterables such as lists, tuples, 
# strings, dict etc, into a single iterator of tuples. Each tuple contains elements 
# from the input iterables that are at the same position.

names = ['John', 'Alice', 'Bob', 'Lucy']
scores = [85, 90, 78, 92]

res = zip(names, scores)
print(list(res))

# Output 
# [('John', 85), ('Alice', 90), ('Bob', 78), ('Lucy', 92)]

#Dictionary comprehension is a method for transforming one dictionary into another dictionary.
# During this transformation, items within the original dictionary can be conditionally 
# included in the new dictionary and each item can be transformed as needed.

stu = { k:v for (k, v) in zip(names, scores)}
print(stu)

# Sqare dictionary for even number 

sq_dict = { i: i*i for i in range(1,5)if i % 2 == 0}
print(sq_dict)

# Set comprehension is a method for creating sets in python using the elements from other 
# iterables like lists, sets, or tuples. Just like we use list comprehension to 
# create lists, we can use set comprehension instead of for loop to create a new 
# set and add elements to it.

# set 

sat = {i for i in scores}

print(sat)
for x in sat:
    print(x)


# Time and space complexities in Python 
# https://aman.ai/code/data-structures/#python-time-complexities 
# https://binarybeats.medium.com/python-set-data-structure-methods-use-time-and-space-complexity-366b8c408345

# Python Data Structure, below is the good article 
# https://aman.ai/code/data-structures/ 
# New code commit ++++++++++++++++++++
# fhldhflsj