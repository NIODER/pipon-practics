word = list(input())
index = int(input())
try:
    print(word[index - 1])
except Exception as e:
    print("ОШИБКА")