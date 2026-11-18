marks = [[80, 70, 60], [75, 85, 65], [90, 60, 55]]
subjects = ["Python", "Maths", "English"]
for i in range(len(marks)):
    total = 0
    for j in range(len(marks[i])):
        total = total + marks[i][j]
    average = total / len(marks[i])
    print("Student", i + 1, "Total:", total, "Average:", average)
lowest_average = 101
lowest_subject = ""
for j in range(3):
    total = 0
    for i in range(3):
        total = total + marks[i][j]
    average = total / 3
    if average < lowest_average:
        lowest_average = average
        lowest_subject = subjects[j]
print("Lowest average subject:", lowest_subject)