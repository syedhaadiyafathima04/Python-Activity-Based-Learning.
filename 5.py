appliances = ["Fan", "AC", "Light"]
usage = [[2, 3, 2, 4, 3, 2, 3],[8, 9, 7, 10, 8, 9, 11],[2, 2, 3, 2, 2, 3, 2]]
for day in range(7) :
    total = 0
    for appliance in range(3) :
        total = total + usage[appliance] [day]
    print("Day", day + 1, "total:", total)
    if total > 15:
        print("High usage day")
for i in range(3) :
    total = 0
    for j in range(7) :
        total = total + usage[i][j]
    print(appliances[i], "weekly total:", total)