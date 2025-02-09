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
