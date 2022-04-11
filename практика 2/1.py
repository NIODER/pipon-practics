books_in_library = int(input())
summertime_reading_books = int(input())
library = []
summertime_plan = []

for i in range(books_in_library):
    library.append(input())
print("-" * 10)
for i in range(summertime_reading_books):
    summertime_plan.append(input())

find = False
for book1 in summertime_plan:
    for book in library:
        if book == book1:
            find = True
            break
        else:
            find = False
    if find:
        print("YES")
    else:
        print("NO")
