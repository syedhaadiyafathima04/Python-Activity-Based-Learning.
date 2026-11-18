days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
prepared = [100, 120, 110, 90]
served = [92, 100, 105, 75]
for i in range(4):
    waste = prepared[i] - served[i]
    percentage = (waste / prepared[i]) * 100
    print(days[i], "waste:", waste, "meals")
    print("Waste percentage:", round(percentage, 2), "%")
    if percentage > 10:
        print("High waste")