crate = [
    {"weight": 120, "blemishes": 0, "is_rotten": False},
    {"weight": 90,  "blemishes": 2, "is_rotten": False},
    {"weight": 250, "blemishes": 0, "is_rotten": False},
    {"weight": 150, "blemishes": 1, "is_rotten": True},   # Rotten!
    {"weight": 80,  "blemishes": 0, "is_rotten": False},
]

# Initialize counts
small_count = 0
med_count = 0
large_count = 0
rotten_count = 0
premium_count = 0


for potato in crate:

    
    if potato["is_rotten"]:
        rotten_count += 1
        continue  

    
    if potato["blemishes"] == 0:
        premium_count += 1

    if potato["weight"] < 100:
        small_count += 1
    elif potato["weight"] <= 200:
        med_count += 1
    else:
        large_count += 1

print("Summary:")
print("Small potatoes:", small_count)
print("Medium potatoes:", med_count)
print("Large potatoes:", large_count)
print("Rotten potatoes:", rotten_count)
print("Premium potatoes:", premium_count)
