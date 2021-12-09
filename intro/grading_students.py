def grading_studnets(grades):
    for i in range(len(grades)):
        r = grades[i] % 5
        if grades[i] >= 38 and r > 2:
            grades[i] = grades[i] + (5 - r)
    return grades
grades = [73,38,52,33,88]
print(grading_studnets(grades))