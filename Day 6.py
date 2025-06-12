students_scores = [10, 10, 9, 9, 3, 5, 4, 5, 7, 1]

max_score = students_scores[0]

for score in students_scores:
    if score > max_score:
        max_score = score

print("The highest score is:", max_score)
