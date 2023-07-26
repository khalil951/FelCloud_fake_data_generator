from .behavior import PersonaBehavior
from random import randint

class Persona:
    def __init__(self, name="khalil", age=31, occupation="developer"):
        id
        self.name = name
        self.age = age
        self.occupation = occupation
        self.project = [PersonaBehavior() for _ in range(randint(1,10))]

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Occupation: {self.occupation}")
        print("")
        for behavior in self.project:
            behavior.describe()
    
    def to_dict(self):
        data = [
            {
                "name":self.name,
                "age":self.age,
                "occupation":self.occupation,
                "flavor":project.flavor.name,
                "period":project.period
            }
            for project in self.project
        ]
        return data

        

class Developer(Persona):
    def __init__(self, name, age, occupation,programming_languages):
        super().__init__(name, age, occupation)
        self.programming_languages = programming_languages

    def describe(self):
        super().describe()
        print("Persona Type: Developer")
        print(f"Programming Languages: {', '.join(self.programming_languages)}")
        print("")

class DataScientist(Persona):
    def __init__(self, name, age, occupation,tools):
        super().__init__(name, age, occupation)
        self.tools = tools

    def describe(self):
        super().describe()
        print("Persona Type: Data Scientist")
        print(f"Tools: {', '.join(self.tools)}")
        print("")




