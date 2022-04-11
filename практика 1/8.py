count = int(input())
list = []

for i in range(count):
    list.append(input())

for string in list:
    if "кот" in string.lower():
        print("МЯУ")
        break
