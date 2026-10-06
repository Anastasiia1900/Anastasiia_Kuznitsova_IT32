grades_text = "95, 88, 100, 99, 100"

grades = [int(grade) for grade in grades_text.split(", ")]
print("Grades:", grades)

average = sum(grades) / len(grades)
print(f"Average grade: {average:.2f}")
print("Highest grade:", max(grades))
print("Lowest grade:", min(grades))
print("Grades:", " | ".join(map(str, grades)))

subjects_text = (
    "IT Law, Web Resource Development, Programming, "
    "Ukrainian Language, Operating Systems and Computer Networks Administration"
)

subjects = subjects_text.split(", ")

print("\nTable:")
print(f"{'No.':<5}{'Subject':<65}{'Grade':<8}")

for number, (subject, grade) in enumerate(zip(subjects, grades), start=1):
    print(f"{number:<5}{subject:<65}{grade:<8}")

longest_subject = max(subjects, key=len)
print("\nLongest subject:", longest_subject)
print("Number of characters:", len(longest_subject))