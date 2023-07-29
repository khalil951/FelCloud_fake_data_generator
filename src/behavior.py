from .flavor import SmallFlavor , MediumFlavor , LargeFlavor , XXLFlavor
from random import randint
from datetime import date , timedelta

class Behavior:
    def __init__(self, flavor , start_date , end_date):
        self.flavor = flavor
        self.start_date = start_date
        self.end_date = end_date
        

    def describe(self):
        print(f"start_date: {self.start_date}")
        print(f"end_date: {self.end_date}")
        self.flavor.describe()

class PersonaBehavior(Behavior):
    def __init__(self):
        start_date = date(2022 , 1 , 1)
        end_date = date(2025 , 12 , 30)
        random_flavor = randint(0,3)
        flavors = [SmallFlavor(), MediumFlavor(), LargeFlavor(), XXLFlavor()]
        super().__init__(flavors[random_flavor] , start_date , end_date)

    def describe(self):
        super().describe()

# Creating instance
persona_behavior = PersonaBehavior()







      