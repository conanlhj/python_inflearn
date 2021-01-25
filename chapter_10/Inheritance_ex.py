class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print('My name is', self.name, 'and my age is', str(self.age))


class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

    def do_work(self):
        print('I work hard.')

    def about_me(self):
        super().about_me()
        print('My payment is', self.salary,
              'and my date of entry is', self.hire_date)


myPerson = Person('John', 21, 'Male')
myEmployee = Employee('Daeho', 23, 'Male', 3000000, '2020/01/20')
myPerson.about_me()
myEmployee.about_me()
