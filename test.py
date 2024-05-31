class Person:
    pass


class Human(Person):
    id: Person[int] 

p = Human(id=2)

print(p.id)

