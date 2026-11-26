
text = input("Введiть суму: ")
text = text.replace(",", ".")
cents = round(float(text) * 100)

nominals = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

banknotes = 0
coins = 0
lines = []

for n in nominals:
    count = cents // n # скільки разів n поміщається в суму
    cents %= n # що залишилось
    if count > 0:
        if n >= 500:
            banknotes += count
        else:
            coins += count
        value = n / 100
        if value == int(value):
            value = int(value)
        lines.append(f"{count} x {value}")

print("Кількість банкнот:", banknotes)
print("Кількість монет:", coins)
print("Склад суми:")
for line in lines:
    print(line)