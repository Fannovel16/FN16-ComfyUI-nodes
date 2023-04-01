def create_class(name):
    class NewClass:
        def __init__(self, value):
            self.value = value

        def display(self):
            print(f"{name} value is {self.value}")

    return NewClass

MyClass = create_class("MyClass")
MyClassB = create_class("MyClassB")

# Create an instance of the returned class
obj = MyClass("Hello World")

# Call the method of the returned class
obj.display()

obj2 = MyClassB("Hello World 2")
obj2.display()