# import random
# myList = [random.randint(-10,10) for i in range(10)]
# print(myList)
# it = iter(myList)
#
# for i in myList:
#     print(next(it)+2)
#
# class Counter:
#     def __init__(self,maxNum):
#         self.i = 0
#         self.maxNumber = maxNum
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.maxNumber:
#             raise StopIteration
#         return self.i
# count = Counter(5)
p = range(0,5)
it = iter(p)
a = [(1+next(it)*5) for i in range(5)]
print(a)
# for elem in count:
#     print(elem)
# import random
#
# l = []
# for i in range(0,10):
#     l.append(random.randint(-10,10))
# print(l)
# a = [random.randint(-10,10)//3 for i in range(10)]
# print(a)