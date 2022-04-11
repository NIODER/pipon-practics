columns = int(input())
lines = int(input())

for line in range(1, lines + 1):
    for column in range(1, columns + 1):
        print(column / line, " ", end="")
    print()