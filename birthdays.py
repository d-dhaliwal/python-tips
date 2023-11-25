birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Please enter a name or type nothing to terminate.')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(f'{birthdays[name]} is the birthday for {name}.')
    else:
        print(f'I don\'t have birthday record available for {name}.')
        print('When is their birthday?')
        birthday = input()

        birthdays[name] = birthday
        print(f'Birthday database updated.')
