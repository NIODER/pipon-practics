a = [1, 2, 3]


def from_string_to_list(string, container):
    for number in string.split(" "):
        container.append(int(number))


from_string_to_list("1 2 3 4", a)
print(*a)

