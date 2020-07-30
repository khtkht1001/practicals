import random
print(random.randint(5, 20))  # line1
print(random.randrange(3, 10, 2))  # line2
print(random.uniform(2.5, 5.5))  # line3
"""
1)random number between 5 and 20 (including 5 and 20)
smallest number=5, largest number=20

2)random number in a range of numbers between 3 and 10 with the interval of 2 [3,5,7,9]
smallest number=3, largest number=9
line 2 couldn't have produced a 4

3)random number between 2.5 and 5.5 (including both integer and float)
"""
print(random.randint(1, 100))
