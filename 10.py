records = [
    "2026-CSE-101",
    "2026-ECE-205",
    "26-CSE-103",
    "2026-EEE-110",
    "2026-CSE-7",
]
for record in records:
    parts = record.split("-")
    valid = True
    if len(parts) != 3:
        valid = False
    else:
        year = parts[0]
        branch = parts[1]
        number = parts[2]
        if len(year) != 4 or not year.isdigit():
            valid = False
        if branch != "CSE" and branch != "ECE":
            valid = False
        if len(number) != 3 or not number.isdigit():
            valid = False
    if valid:
        print(record, "is valid")
    else:
        print(record, "is invalid")