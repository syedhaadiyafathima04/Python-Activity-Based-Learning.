subjects = ["Python", "Maths", "English"]

old_marks = [55, 70, 65]
new_marks = [68, 62, 35]

for i in range(3):
    change = new_marks[i] - old_marks[i]
    
    if change > 0:
        print(subjects[i], "improved by", change)
    elif change < 0:
        print(subjects[i], "decreased by", -change)
    else:
        print(subjects[i], "no change")

print("Weak subjects:")

for i in range(3):
    if new_marks[i] < 40:
        print(subjects[i])