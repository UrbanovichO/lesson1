import logging
x = 5
y = 8
z = 9
print(f"x = {x} y = {y} z = {z}")
print("x = {x} y = {y} z = {z}".format(x=x,y=y,z=z))
logging.basicConfig(level=logging.DEBUG, filename="logs.log",filemode="w",format="We have next logging massege:%(asctime)s%(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
logging.debug("debug")
logging.info("info")
# f = open("lesson9.log","w+")
# array.append(logging.critical("critical"))
# s = ""
# s += str(array)+"\t"
# print(array)
# f.write(s)