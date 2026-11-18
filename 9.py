names = ["Aisha", "Rahul", "Sara"]
marks = [[70, 65, 75], [35, 40, 30], [55, 60, 58]]
attendance = [85, 68, 72]
lab = [70, 35, 45]
for i in range(3):
    average = sum(marks[i]) / 3
    risk = 0
    if average < 40:
        risk = risk + 1
    if attendance[i] < 75:
        risk = risk + 1
    if lab[i] < 40:
        risk = risk + 1
    if risk >= 2:
        level = "High Risk"
    elif risk == 1:
        level = "Medium Risk"
    else:
        level = "Safe"
    print(names[i], ":", level)