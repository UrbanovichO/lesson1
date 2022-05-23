import random
l = []
for i in range(25):
    l.append(random.randint(1,100))
it = iter(l)
a = [(1+next(it)*random.randint(1,10)) for i in range(25)]
print(a)