# dictionary = A changeable, unordered collection of uniques key:value pairs
#               Fast due to hashing,allow us to acces a value quickly

capitals = {'USA':'Washinhton DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'USA':'Las Vegas'})
capitals.pop('China') #usuwa tylko wybrany element
#capitals.clear() usuwa wszystko

print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Germany':'Berlin'})

for key,value in capitals.items():
    print(key,value)
