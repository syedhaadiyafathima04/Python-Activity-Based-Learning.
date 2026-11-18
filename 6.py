teams = ["A", "B", "C", "D"]
results = [["D", "W", "L"], ["D", "W", "W"], ["L", "L", "W"], ["W", "L", "L"]]
points = [0, 0, 0, 0]
for i in range(4):
    for result in results[i]:
        if result == "W":
            points[i] = points[i] + 3
        elif result == "D":
            points[i] = points[i] + 1
for i in range(4):
    for j in range(i + 1, 4):
        if points[j] > points[i]:
            points[i], points[j] = points[j], points[i]
            teams[i], teams[j] = teams[j], teams[i]
print("Ranking:")
for i in range(4):
    print(i + 1, teams[i], points[i])