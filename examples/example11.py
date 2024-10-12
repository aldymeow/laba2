def my_generate(start=0, stop=11, step=2):
    number = start
    while number <= stop:
        yield number
        number += step
        
ranger = my_generate(1,11)

for value in ranger:
    print(value)