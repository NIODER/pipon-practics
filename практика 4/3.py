import math
import random

accuracy = int(input("Count of points: "))
count_points_in_circle = 0
for i in range(accuracy):
    x0 = 0
    y0 = 0
    x = random.random()
    y = random.random()
    if (math.pow((x - x0), 2) + math.pow((y - y0), 2)) <= 1:
        count_points_in_circle += 1

print((4*count_points_in_circle)/accuracy)
