# Define a decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper

# Decorate a function using the decorator
@my_decorator
def my_function(x, y):
    print("Inside my_function.")
    return x + y

# Decorate a method using the decorator
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @my_decorator
    def my_method(self):
        print("Inside my_method.")
        return self.x * self.y

# Call the decorated function and method
result1 = my_function(2, 3)
print(result1)

my_object = MyClass(4, 5)
result2 = my_object.my_method()
print(result2)
