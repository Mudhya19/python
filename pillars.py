# Pillars
# https: // www.codewars.com/kata/5bb0c58f484fcd170700063d/train/python

# Create a function that takes in three parameters:
# 1. A list of numbers
# 2. A number representing the number of pillars
# 3. A number representing the number of spaces

'''test.describe("Basic Tests")
test.assert_equals(pillars(1, 10, 10) , 0)
test.assert_equals(pillars(2, 20, 25) , 2000)
test.assert_equals(pillars(11, 15, 30) , 15270)'''


def pillars(num_pill, dist, width):
    sum = 0
    if num_pill == 0:
        return 0
    elif num_pill == 1:
        return dist*100
    else:
        sum = ((num_pill - 1)*dist*100) + (width*(num_pill-2))
    return sum
