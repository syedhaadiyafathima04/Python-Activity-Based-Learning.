n = int(input("Enter an odd size: "))

if n <= 0 or n % 2 == 0 or n > 9:
    print("Invalid size")
else:
    mid = n // 2
    for i in range(mid + 1):
        spaces = mid - i
        if i == 0:
            print(" " * spaces + "*")
        else:
            inside = 2 * i - 1
            print(" " * spaces + "*" + " " * inside + "*")
    for i in range(mid - 1, -1, -1):
        spaces = mid - i
        if i == 0:
            print(" " * spaces + "*")
        else:
            inside = 2 * i - 1
            print(" " * spaces + "*" + " " * inside + "*")