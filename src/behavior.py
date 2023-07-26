from .flavor import SmallFlavor , MediumFlavor , LargeFlavor , XXLFlavor
from random import randint
from datetime import datetime, timedelta

class Behavior:
    def __init__(self, period, flavor):
        self.period = period
        self.flavor = flavor

    def describe(self):
        print(f"Period of Usage: {self.period}")
        self.flavor.describe()
#start date = janvier 2022 -> decembre 2025
#end period

class PersonaBehavior(Behavior):
    def __init__(self):
        min_period = 1*24*7  #number of hours in 1week
        max_period = 52*24*7 #number of hours in 1year
        random_period = randint(min_period, max_period)
        start_date = datetime.now()
        period = start_date + timedelta(hours=random_period)
        random_flavor = randint(0,3)
        flavors = [SmallFlavor(), MediumFlavor(), LargeFlavor(), XXLFlavor()]
        super().__init__(period, flavors[random_flavor])

    def describe(self):
        print(f"period : {self.period}")
        self.flavor.describe()

# Creating instances of Behavior classes
persona_behavior = PersonaBehavior()
persona_behavior.describe()






      