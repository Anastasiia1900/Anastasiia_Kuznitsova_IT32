print('Anastasiia Kuznitsova IT-32')

def print_card():
    print('Name: Anastasiia Kuznitsova')
    print('Group: IT-32')
    print('Birth year: 2009')

print("--- no parameters, call 1 ---")
print_card()

print("--- no parameters, call 2 ---")
print_card()

print("--- no parameters, call 3 ---")
print_card()

def print_card_ards(name, surname, group='IT-32', year=2009):
    print(f"{name} {surname}, {group}, {year}")

print('--- positional arguments ---')
print_card_ards('Anastasiia', 'Kuznitsova', 'IT-32', 2009)

print('--- keyword arguments ---')
print_card_ards(
    name = 'Anastasiia',
    surname = 'Kuznitsova',
    group = 'IT-32',
    year = 2009
)

print('--- mixed arguments ---')
print_card_ards('Anastasiia', 'Kuznitsova', group='IT-32', year=2009)

print('--- default group ---')
print_card_ards('Anastasiia', 'Kuznitsova', year=2009)