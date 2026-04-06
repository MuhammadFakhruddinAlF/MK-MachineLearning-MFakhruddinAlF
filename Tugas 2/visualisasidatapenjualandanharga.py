import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#%
#create and show random data
penjualan = np.random.rand(100) * 100
harga = np.array([16000, 18000, 27000, 34000, 50000, 60000, 68000, 65000, 81000, 85000])

print("Data Penjualan:", penjualan)
print("Data Harga:", harga)
