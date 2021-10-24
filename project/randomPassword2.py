import random

upper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = ("abcdefghijklmnopqrstuvwxyz")
number = ("0123456789")
symbol = ("@#$%&*?")

pw = input(str("Password Code: "))


def passwordRandom(password):
    if password in str(pw):
        all = (upper + lower + number + symbol)
        length = 16
        password = "".join(random.sample(all, length))
        print(password != pw, "Successfully Password")
    else:
        all = (upper + lower)
        length = 16
        password = "".join(random.sample(all, length))
        print(password, "Not Valid password")


passwordRandom(pw)
