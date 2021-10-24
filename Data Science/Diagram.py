import matplotlib.pyplot as plt
import numpy as np

nama = ('A', 'B', 'C', 'D', 'E')
nilai = [1, 2, 3, 4, 5]
plt.bar(nama, nilai, alpha=0.5)
plt.xticks(nama)
plt.ylabel("Penjualan")
plt.xlabel("Merek")
plt.title("Diagram")

plt.show()
