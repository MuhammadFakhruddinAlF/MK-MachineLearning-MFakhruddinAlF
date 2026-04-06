import pandas as pd
import matplotlib.pyplot as plt

# read data  [cite: 187, 202]
data = pd.read_csv("tips.csv")

# count the number of tips given by each gender
counts = data['sex'].value_counts()

# pie chart
plt.figure(figsize=(6, 6))
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightpink'])
plt.title("Persentase Pemberi Tips Berdasarkan Jenis Kelamin")
plt.show()