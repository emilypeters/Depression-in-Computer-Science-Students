import pandas as pd
import matplotlib.pyplot as plt
from numpy import size

df = pd.read_csv(location_of_file)

depressed_female = (df[(df.DepressionStatus == "Yes") & (df.Gender == "Female")])
depressed_female_count = size(depressed_female)

total_minus_depressed = (df[(df.DepressionStatus != "Yes") & (df.Gender == "Female")])
total_minus_depressed_count = size(total_minus_depressed)

data = [depressed_female_count, total_minus_depressed_count]
labels = ['depressed female', 'undepressed female']

plt.pie(data, None, labels)
plt.title("Female Students in Computer Science")

plt.show()


