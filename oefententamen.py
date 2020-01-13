import uncertainties as uc 
import uncertainties.umath as um
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

raw = []
header = []
with open('tentamen.txt','r') as f:
    for line in f:
        if line[0] != "#":
            raw.append(line.replace("\n","").split('\t'))
        else:
            header.append(line)
data = pd.DataFrame(raw,columns = ['','',''])
print("# Oussama Benchikhi 6930263")
for line in header:
    print(line.strip())
print(data)

datamatrix = np.genfromtxt("tentamen.txt")
gemiddeldey = datamatrix.mean(0)

def pythagoras(lijst):
    return np.sqrt(np.sum(lijst**2))

v0 = []
for i in datamatrix:
    v0.append(pythagoras(i))

print(np.round(gemiddeldey, 2), "de gemiddelde snelheden in m/s")
print(np.round(v0,2), "de gemiddelde beginsnelheden in m/s")

np.random.seed(20010723)
delta_v0 = np.random.normal(0, 2, size=np.shape(v0))
#print(delta_v0)
#print("delta_v0 =", delta_v0)

V0New = v0+delta_v0
print(np.round(V0New,2))









