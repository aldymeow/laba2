def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}

bro_cat = cat('Barsik', 'Grey', 2)
print(bro_cat)

my_cat = cat(color = 'white', age = 1, name = 'Alf')
print(my_cat)