def read_grade(prompt: str) -> int:
    """Reads a valid grade from 0 to 100."""
    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Error: digits only")
            continue

        grade = int(value)

        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue
        return grade


def to_letter(grade: int) -> str:
    """Converts a numeric grade to an ECTS letter."""
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 74:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades: list[int]) -> float:
    """Returns the arithmetic mean of grades."""
    return sum(grades) / len(grades)


def count_above(grades: list[int], limit: float) -> int:
    """Counts grades greater than the given limit."""
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name: str, group: str, grades: list[int]) -> None:
    """Prints a report about the student's grades."""
    avg = average(grades)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print(f"Grades: {' '.join(map(str, grades))}")
    print(f"Average: {avg:.2f} -> {to_letter(round(avg))}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {count_above(grades, avg)}")


def main() -> None:
    """Runs the main program."""
    name = "Anastasiia Kuznitsova"
    group = "IT-32"
    grades = []
    n = len("Anastasiia")

    print(f"{name}, {group}")

    for i in range(n):
        grade = read_grade(f"Grade {i + 1} (0-100): ")
        grades.append(grade)

    print_report(name, group, grades)

main()