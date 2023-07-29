# import sys
# sys.path.append('/Users/pc/Felcloud/src')

from src.persona import Persona
from db import inject_db
from faker import Faker
import pandas as pd
import uuid
import csv

# Creating Faker instance
fake = Faker()

personas  = [Persona(uuid.uuid4() , fake.name() , fake.random_int(min=25, max=60), fake.job()) for _ in range(1000)]
data = list()

for persona in personas:
    dict = persona.to_dict()
    data.extend(dict)

df = pd.DataFrame(data)
# Save the DataFrame to a CSV file
file_name = 'personas.csv'
#csv_file_path = os.path.join(os.getcwd(), file_name)
df.to_csv(file_name, index=False)
#inject into DB
inject_db(file_name ,csv)

