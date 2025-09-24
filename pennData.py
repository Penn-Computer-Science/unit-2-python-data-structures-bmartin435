import pandas as pd
import random

fNames = ["Eliana", "Mike", "Big Dog", "Felicia", "Amelia", "Kayla", "Jake", "June", "Alex", "Stephen", "Jackson"]
lNames = ["McDonald", "Dover", "Williams", "Moore", "Jordan", "Marsh", "Dingle", "Moriah", "Clark", ]
years = ["Freshman", "Sophomore", "Junior", "Senior", "Super Senior"]
pathways = [" Early College", "Agriculture", "Engineering", "Computer Science", "Business", "Marketing", "Theater"]
names = []

for i in range(20):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.0), 2) for _ in names],
    "Credits Completed": [random.randint(0, 60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names],
}

pennData = pd.DataFrame(data)

print(pennData)