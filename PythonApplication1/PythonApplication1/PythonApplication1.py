rider_scores = [10, 8, 9, 7, 6]

for i in range(4):
    if rider_scores[i+1] >= 8:
        rider_scores = i + 20
final_sum = sum(rider_scores)
print(final_sum)
