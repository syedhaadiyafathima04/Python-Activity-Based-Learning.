products = ["Rice", "Milk", "Oil", "Sugar"]
old_price = [50, 30, 120, 45]
new_price = [55, 32, 145, 42]
for i in range(4):
    change = ((new_price[i] - old_price[i]) / old_price[i]) * 100
    print(products[i], "change:", round(change, 2), "%")
    if abs(change) > 10:
        print("Large price change")