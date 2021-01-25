class Person(object):  # 부모 class
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Korean(Person):  # 자식 class
    pass


first_korean = Korean('Hanjin', 21)
print(first_korean.name)
