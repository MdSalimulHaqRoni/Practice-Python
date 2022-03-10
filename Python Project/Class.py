def method_name(a, b):
        print("Method")
class Person:
    def __init__(self, person_name):
        self.name = person_name
    def get_name(self):
        return self.name

method_name(15, 20)
a_person = Person("Data science")
b_person = Person("Machine learning")

print(a_person.get_name())
print(b_person.get_name())