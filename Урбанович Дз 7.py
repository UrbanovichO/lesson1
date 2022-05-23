result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

#data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
data = {10: 2, 2: 5, 18: 0 , 8 : 4}
data[0] = 15
data[123] = 4
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except TypeError:
        print("TypeError")
    except ValueError:
        ValueError("ValueError")
    except ZeroDivisionError:
        ZeroDivisionError("ZeroDivisionError")
print(result)