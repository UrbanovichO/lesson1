import random
l = []
for i in range(0,10):
    l.append(random.randint(1,10))
it = iter(l)
a = [(1+next(it)*5) for i in range(10)]
print(a)