import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

penjualan = np.array([6, 5, 5, 4, 4, 3, 2, 2, 2, 1])
harga = np.array([16000, 18000, 27000, 34000, 50000, 68000, 65000, 81000, 85000, 90000])

plt.scatter(penjualan, harga)
plt.title("Scatter Plot Penjualan vs Harga")
plt.xlabel("Penjualan")
plt.ylabel("Harga")
plt.show()