from collections import deque

queues = deque([1, 2, 3, 4, 5])

print("data sekarang: ", queues)

# menambahkan data antrian
queues.append(6)
print("data dimasukan: ", 6)
print("data sekarang: ", queues)

# mengeluarkan data antrian

out = queues.popleft()
print('data dikeluarkan: ', out)
print('data sekarang: ', queues)
