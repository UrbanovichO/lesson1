# try:
#     print("start program")
#     print(hell)
# except:
#     print("You have an error")


# res = 0
# def division(a,b):
#
#     try:
#         res = a/b
#     except:
#         try:
#             a = int(a)
#             b = int(b)
#             res = a/b
#         except ZeroDivisionError:
#             res = 0
#         except ValueError:
#             res = ("Enter number")
#     print(res)
# while res == 0:
#     division(input("a = "),input("b = "))

# x = 15
# try:
#     print(x)
# except:
#     print("Something went wrong")
# else:
#     print("Else program do")
# finally:
#     print("The program has completed its work")

def checker(var1):
    if type(var1)!= str:
        raise TypeError(f"Sorry, we can`t wark with {type(var1)}, we need class str")
    else:
        return var1
fir = "10"
checker(fir)
