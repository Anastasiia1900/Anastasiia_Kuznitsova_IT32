def create_subjects():
    return [
        ("OperatingSystems", 3, 9),
        ("Programming", 3, 10),
        ("UkrainianLanguage", 1, 10),
        ("Databases", 3, 11),
        ("ITLaw", 2, 9),
        ("WebDevelopment", 3, 11),
        ("ForeignLanguage", 2, 10),
        ("Mathematics", 2, 9)
    ]


def print_table(subjects):
    print("Anastasiia Kuznitsova, IT-32")
    print("#  Subject                  Pairs  Grade")

    for number, (title, pairs, grade) in enumerate(subjects, 1):
        print(f"{number:<3}{title:<25}{pairs:<7}{grade}")


def total_pairs(subjects):
    return sum(subject[1] for subject in subjects)


def subject_with_most_pairs(subjects):
    return max(subjects, key=lambda subject: subject[1])


def subject_with_lowest_grade(subjects):
    return min(subjects, key=lambda subject: subject[2])


def print_lists_and_average(subjects):
    titles = [subject[0] for subject in subjects]
    grades = [subject[2] for subject in subjects]
    average = sum(grades) / len(grades)

    print("Titles:", titles)
    print("Grades:", grades)
    print("Average:", round(average, 2))


def print_high_grades(subjects):
    titles = [
        subject[0]
        for subject in subjects
        if subject[2] >= 10
    ]

    print("Grade 10+:", titles)


def print_histograms(subjects):
    for title, pairs, grade in subjects:
        print(f"{title}: {'#' * grade}")


def retake_subject(subjects):
    weakest = subject_with_lowest_grade(subjects)
    old_grade = weakest[2]
    new_grade = min(old_grade + 2, 12)
    updated_subjects = []

    for title, pairs, grade in subjects:
        if title == weakest[0]:
            updated_subjects.append((title, pairs, new_grade))
        else:
            updated_subjects.append((title, pairs, grade))

    print(f"Retake: {weakest[0]} {old_grade} -> {new_grade}")
    print("Subjects:", updated_subjects)


def main():
    subjects = create_subjects()
    print_table(subjects)
    print("Pairs per week:", total_pairs(subjects))

    most_pairs = subject_with_most_pairs(subjects)
    print(f"Most pairs: {most_pairs[0]} ({most_pairs[1]})")

    weakest = subject_with_lowest_grade(subjects)
    print(f"Weakest subject: {weakest[0]} ({weakest[2]})")

    print_lists_and_average(subjects)
    print_high_grades(subjects)
    print_histograms(subjects)
    retake_subject(subjects)

main()