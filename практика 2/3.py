chain = list(input())
counts = []

count = 0
for i in range(len(chain)):
    if chain[i] == "р":
        count = 0
        continue
    try:
        next_one = chain[i] == chain[i + 1]
    except Exception:
        next_one = False
    try:
        previous = chain[i] == chain[i - 1]
    except Exception:
        previous = False
    if next_one or previous:
        count = count + 1
    counts.append(count)

print(max(counts))
