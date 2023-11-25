allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

apples = 0             
names = list(allGuests.keys())   

for name in names:
    if 'apples' in allGuests[name].keys():
        apples += int(allGuests[name]['apples'])
    else:
        pass    
print(apples)

# make it into a function now
def total_items(item):
    total = 0
    for name in names:
        if item in allGuests[name].keys():
            total += int(allGuests[name][item])
        else:
            pass
    return print(f'Total {item} at the picnic were {total}.')        

total_items('apples')
total_items('apple pies')
