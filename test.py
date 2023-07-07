import random
from builtins import print

tst = []

for i in range(10):
    tst.append((random.randint(0,9), random.randint(0,9)))
#tst.append(tst[random.randint(0,9)])

#for link_ind in range(len(tst)):
print(tst[-1] in tst[0:-1])
#print(tst)
