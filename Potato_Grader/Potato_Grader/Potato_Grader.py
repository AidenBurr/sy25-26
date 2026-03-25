"""Potato Grader"""

weight = float(input("Enter Potato Weight in Grams: "))

if weight < 100:
    grade ="small"

elif weight >= 100 and weight < 200:
    grade = "medium"

else:
    grade = "large" 

print(f"This is a {grade} potato.")

"""Blemish Counter"""

Blemish_Counts = []

for i in range(5):
    count = int(input(f"Enter blemishes for potato {i+1}: "))
    Blemish_Counts.append(count)

total = sum(Blemish_Counts)

average = total / len(Blemish_Counts)

print(f"Total Blemishes: {total}")

print(f"Average Blemishes: {average}")

"""Quality Control Filter"""

All_Potatoes = [0,2,5,1,0,8,3,0]

Perfect_Potatoes = []

for p in All_Potatoes:
    if p == 0:
        Perfect_Potatoes.append(p)

Num_Total = len(All_Potatoes)

Num_Perfect = len(Perfect_Potatoes)

Percentage = (Num_Perfect / Num_Total) * 100

print(f"Batch Quality: {Percentage}% Perfect Potatoes")