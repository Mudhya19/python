import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 3, 7, 3, 9, 7, 11])

nama = ('C', 'C#', 'C++', 'Django', 'Javascript',
        'PHP', 'React.js', 'Java', 'Ruby', 'Python')
nilai = [3, 8, 1, 10, 3, 7, 3, 9, 7, 11]
plt.bar(nama, nilai, alpha=0.5)
plt.xticks(nama)
plt.ylabel("Penjualan")
plt.xlabel("Merek")
plt.title("Diagram")
plt.plot(ypoints, marker='o')
plt.show()
