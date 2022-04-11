number_of_shells = int(input())
content = []

for i in range(number_of_shells):
    content.append(input())
print(content)
numbers_of_permutasions = int(input())

for i in range(numbers_of_permutasions):
    new_number_of_shells = int(input())
    new_content = []
    for j in range(new_number_of_shells):
        new_content.append(content[j])
    for j in range(new_number_of_shells):
        permutation = int(input())
        new_content[permutation - 1] = content[j]
    content = new_content

for i in content:
    print(content)