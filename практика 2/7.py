char = input()
text_array = input().lower().split(" ")

for word in text_array:
    if char in word:
        print(word)