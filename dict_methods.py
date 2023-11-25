spam = {'color' : 'red',
        'age' : 42}

for v in spam.values():
    print(v)

for k, v in spam.items():
    print(f'{k} --- {v}')

for i in spam.items():
    print(i)        

print(list(spam.keys()))

# The get() Method

picnicItems = {'apples' : 5,
               'cups' : 2}

print(f"I am bringing {picnicItems.get('apples',0)} apples to the picnic.")
print(f"I am bringing {picnicItems.get('cupcakes',0)} cupcakes to the picnic.")
