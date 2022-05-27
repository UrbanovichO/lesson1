import random
import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.log",filemode="w",format="We have next logging massege:%(asctime)s%(levelname)s - %(message)s")
a1 = random.randint(1,10)
r =range(0,10)
it = iter(r)
l = [a1+5*(next(it)) / random.randint(-5, 5) for i in r]
it = iter(l)
try:
    print(l)
except:
    logging.error("Division Zero")