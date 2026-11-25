
appliances = ["Fan", "Light", "AC"]
days = 7

consumption = []

for i in range(3):
    row = []

    print("\nEnter daily consumption for", appliances[i])

    for j in range(days):
        units = float(input("Day " + str(j + 1) + ": "))
        row.append(units)

    consumption.append(row)

print("\n----- ELECTRICITY REPORT -----")

for i in range(3):
    total = 0

    for j in range(days):
        total = total + consumption[i][j]

    print(appliances[i], "weekly consumption:", total, "units")

print("\n----- DAILY CONSUMPTION -----")

for j in range(days):
    total = 0

    for i in range(3):
        total = total + consumption[i][j]

    print("Day", j + 1, ":", total, "units")
