name = "Anastasiia"
surname = "Kuznitsova"
group = "IT-32"
grades = [9, 10, 10, 11, 9, 11, 10, 9, 11, 11]

print("Grades:", grades)
print("Number of grades:", len(grades))
print("Sum:", sum(grades))
print("Best grade:", max(grades))
print("Worst grade:", min(grades))
print("Average:", round(sum(grades) / len(grades), 2))

sorted_grades = sorted(grades, reverse=True)
print("Sorted from best to worst:", sorted_grades)
print("Original grades:", grades)

print("Three best grades:", sorted(grades, reverse=True)[:3])
print("Three worst grades:", sorted(grades)[:3])

worst_grade = min(grades)
print("Position of the worst grade:", grades.index(worst_grade) + 1)

average = sum(grades) / len(grades)
higher_than_average = [grade for grade in grades if grade > average]
print("Grades higher than average:", higher_than_average)
print("Number higher than average:", len(higher_than_average))

print("Has 12:", 12 in grades)
print("Has 1:", 1 in grades)

grades.append(len(surname) % 12 + 1)
print("After adding grade to the end:", grades)

grades.insert(0, 12)
print("After inserting 12 at the beginning:", grades)

grades.remove(min(grades))
print("After removing the worst grade:", grades)

removed_grade = grades.pop()
print("Removed last grade:", removed_grade)
print("After removing the last grade:", grades)

print("Number of 12s:", grades.count(12))

result = grades.sort()
print("Return value of sort():", result)
print("Grades after sort:", grades)