schedule = {
    "Mon": ["Operating Systems and Computer Networks Administration", "Programming", "Ukrainian Language"],
    "Tue": ["Databases in Information Systems", "Programming", "IT Law"],
    "Wed": ["Web Resource Development", "Foreign Language", "Web Resource Development"],
    "Thu": ["Operating Systems and Computer Networks Administration", "Programming", "Web Resource Development", "Physical Culture"],
    "Fri": ["IT Law", "Foreign Language", "Databases in Information Systems"]
}

for day, subjects in schedule.items():
    print(f"day: {day};")
    print(f"number of subjects: {len(subjects)};")
    print(f"subjects: {', '.join(subjects)}")

total = sum(len(subjects) for subjects in schedule.values())
print(f"total: {total}")

max_day = max(schedule, key=lambda day: len(schedule[day]))
print(max_day)

all_subjects = set()

all_subjects = set(subject for subjects in schedule.values() for subject in subjects)
print(all_subjects)
print(len(all_subjects))

monday = set(schedule["Mon"])
wednesday = set(schedule["Wed"])

print(f"There are some on both Monday and Wednesday:", monday & wednesday)
print(f"It is in Monday, but not in Wednesday:", monday - wednesday)

def count_subjects(schedule):
    result = {}
    for subjects in schedule.values():
        for subject in subjects:
            result[subject] = result.get(subject, 0) + 1
    return result

subject_counts = count_subjects(schedule)

for number, (subject, count) in enumerate(
    sorted(subject_counts.items(), key=lambda x: x[1], reverse=True),
    start=1
):
    print(f"{number}. {subject} — {count}")