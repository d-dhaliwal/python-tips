myCat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

print(myCat['size'])

# Mutability of dictionaries

new_dict = myCat

if id(new_dict) == id(myCat):
    print("Both dictionaries have the same id.")  

new_dict['age'] = 5
print(myCat)
"""
    Althugh we added the key-value pair to new_dict, 
    myCat also got the same key-value pair.
"""

print(f'My cat has {myCat["color"]} fur.')

# Dictionaries vs. Lists

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']

print(spam == bacon)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}

print(eggs == ham)

