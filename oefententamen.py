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
print("")
for line in header:
    print(line.strip())
print(data)
print("hey")

