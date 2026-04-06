import pandas as pd
import matplotlib.pyplot as plt

# read data  [cite: 187, 202]
data = pd.read_csv("tips.csv")

# count the percentage
percentage = data['sex'].value_counts(normalize=True) * 100

#Bar Chart
percentage.plot(kind='bar', color=['blue', 'pink'])
plt.title("Sebaran Jenis Kelamin (Persentase)")
plt.xlabel("Jenis Kelamin")
plt.ylabel("Persentase (%)")
plt.xticks(rotation=0)
plt.show()