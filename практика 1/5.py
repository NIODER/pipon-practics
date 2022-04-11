sum = 0
count = 0

while True:
    number = float(input())
    if number > -300:
        sum = sum + number
        count = count + 1
    else:
        break

print(sum / count)