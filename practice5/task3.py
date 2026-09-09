print('Anastasiia Kuznitsova IT-32')

def get_initials(name: str, surname:str) -> str:
    return f'{name[0]}. {surname[0]}.'
def get_initials(name: str, surname: str) -> str:
    return f"{name[0]}.{surname[0]}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    count = 0

    for char in text.lower():
        if char == letter.lower():
            count += 1

    return count


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


def reverse_text(text: str) -> str:
    result = ""

    for char in text:
        result = char + result

    return result


name = "Anastasiia"
surname = "Kuznitsova"
group = "IT-32"

print(f"{name} {surname}, {group}")
print(f"Initials: {get_initials(name, surname)}")

c = len(surname)
vowels = count_vowels(surname)
consonants = c - vowels

print(f"Letters in surname: {c}")
print(f"Vowels: {vowels}, consonants: {consonants}")

for letter in "aeiou":
    print(f"{letter}: {count_letters(surname, letter=letter)}")

print(f"Default letter 'a': {count_letters(surname)}")

print(f"Reversed surname: {reverse_text(surname)}")

print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")
