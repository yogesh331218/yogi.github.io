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

#Dictionary comprehension is a method for transforming one dictionary into another dictionary.
# During this transformation, items within the original dictionary can be conditionally 
# included in the new dictionary and each item can be transformed as needed.