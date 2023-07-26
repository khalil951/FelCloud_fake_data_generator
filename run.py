# import sys
# sys.path.append('/Users/pc/Felcloud/src')
import pandas as pd
from src.persona import Persona , Developer , DataScientist
from src.behavior import PersonaBehavior
from faker import Faker

# Creating Faker instance
fake = Faker()

# Creating instances  
persona1 = Persona(fake.name() , fake.random_int(min=20, max=65), fake.job())
persona1.describe()

# persona2 = Developer(fake.name(), fake.random_int(min=20, max=65) , "Software Engineer", ["Python", "Java"])
# persona2.describe()

# persona3 = DataScientist(fake.name(), fake.random_int(min=20, max=65), "Data Analyst", ["R", "Python", "SQL"])
# persona3.describe()


data  = [Persona(fake.name() , fake.random_int(min=20, max=65), fake.job()) for _ in range(1000)]