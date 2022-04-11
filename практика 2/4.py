white_list_length = int(input())
request_list_length = int(input())
white_list = []
request_list = []

for i in range(white_list_length):
    white_list.append(input())
for i in range(request_list_length):
    request_list.append(input())

for word in request_list:
    for word1 in white_list:
        if word == word1:
            print(word)