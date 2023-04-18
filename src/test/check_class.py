class Person:
    pass

p = Person()

class Person:
    def __init__(self, name):
        self.name = name

p = Person("John")
print(p.name) # 輸出 John

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)

p = Person("John")
p.say_hello() # 輸出 Hello, my name is John
