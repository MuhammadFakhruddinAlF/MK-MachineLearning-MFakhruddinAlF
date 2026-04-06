import pandas as pd
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv("tips.csv")

# adding title and labels
plt.title("Scatter Plot")
plt.xlabel('Day')
plt.ylabel('Tip')

# create scatter plot
plt.scatter(data['day'], data['tip'])
plt.show()