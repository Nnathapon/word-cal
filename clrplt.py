import matplotlib.pyplot as p
import numpy as np

with open("clr.txt", "r") as f:
    clrlist = f.readlines()
intval = np.zeros((1, 3))


def s3(s):
    return np.array([eval("0x" + x) for x in (s[:2], s[2:4], s[4:])])


for i in clrlist:
    if "," in i:
        q = i.split(",")
        print(q)
        intval = np.vstack((intval, [s3(q[0])], [s3(q[1])]))
    else:
        intval = np.vstack((intval, [s3(i)]))
print(intval)
print(intval.mean(axis=0), intval.ar)
