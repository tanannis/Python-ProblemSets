from cs50 import get_float  # cs50 library from Harvard University

while True:
    change = get_float("Change owed: ")

    if change <= 0:
        change = get_float("Change owed: ")
    if change > 0:
        break

cents = round(change * 100)

quarters = 25
dimes = 10
nickles = 5
pennies = 1

coins = 0

while cents >= 25:
    cents -= 25
    coins += 1
# print(f"used quarters: {change}")

while cents >= 10:
    cents -= 10
    coins += 1

while cents >= 5:
    cents -= 5
    coins += 1

while cents >= 1:
    cents -= 1
    coins += 1

print(f"used pennies: {change}")
print(f"total coins: {coins}")
