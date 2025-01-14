people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Neville", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherine"}
]

# sorting using normal function
# def f(person):
#     return person["name"]

# people.sort(key=f)

# sorting using lambda funtion
people.sort(key=lambda person: person["name"])

print(people)