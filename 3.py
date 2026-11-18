ids = [101, 102, 103, 102, 104, 105, 101]
amounts = [1200, 5000, 800, 6200, 1500, 700, 5500]

duplicates = []

for i in range(len(ids)):
    for j in range(i + 1, len(ids)):
        if ids[i] == ids[j] and ids[i] not in duplicates:
            duplicates.append(ids[i])

print("Duplicate transaction IDs:")

for x in duplicates:
    print(x)

print("Transactions above 5000:")

for i in range(len(amounts)):
    if amounts[i] > 5000:
        print(ids[i], amounts[i])