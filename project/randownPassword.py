import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
simbol = "+=-*%/$#@"

length = 16
all = (upper + lower + number + simbol)
password = "".join((random.sample(all, length)))
print(password)
