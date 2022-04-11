table = []
rows = int(input())

for i in range(rows):
    line = input()
    splitted_line = line.split(",")
    table.append(splitted_line)

count = int(input())
coordinates_list = []

for i in range(count):
    coordinates_list.append(input())

for coordinates in coordinates_list:
    x = int(coordinates.split(",")[0])
    y = int(coordinates.split(",")[1])
    print(table[x][y])