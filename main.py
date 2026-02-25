#task 1
name = ("Daiana")
age = 20
height = 1.65
is_student = True
print(name)
print(age)

#variable for number
number=[1, 2, 3, 4, 5]
print(number[0])


#variable for text (string)
name = "Daiana"
city = 'London'
message = "Hello, world!"

#create a list of numbers
numbers = [1, 2, 3, 4, 5]
print(type(numbers))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Daiana", 20)
print(p1.name, p1.age)


class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

p1 = Person("Daniel", 20)
p2 = Person("Daiana", 20)
p3 = Person("Emir", 20)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)
print("Total Persons created:", Person.counter)

name = ("Daiana")
print (name)