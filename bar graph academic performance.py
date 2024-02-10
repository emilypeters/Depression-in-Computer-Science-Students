import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(location_of_file)

depressed_female = (df[(df.DepressionStatus == "Yes") & (df.Gender == "Female")])
academic_performance = depressed_female["AcademicPerformance"]

below_average = academic_performance.value_counts()["Below average"]
average = academic_performance.value_counts()["Average"]
good = academic_performance.value_counts()["Good"]

labels = ["Below Average", "Average", "Good"]
scale = [below_average, average, good]

plt.bar(labels, scale)
plt.title("Academic Performance of Depressed Female Computer Science Students")
plt.show()
