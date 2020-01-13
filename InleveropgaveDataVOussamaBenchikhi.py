#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:55:30 2020

@author: Oussama Benchikhi en Jonatan van Dongen
"""


#Importeer het ODR pakket (ODR = Orthogonal Distance Regression)
import scipy.odr as odr
import numpy as np
import matplotlib.pyplot as plt

#De data set 
t = np.array([0.25,0.75,1.25,2.5,3.0,3.75,4.5,5.5,7.0,8.5])
d = np.array([1.43,2.06,2.09,2.66,3.31,3.52,3.79,4.12,4.35,4.95])
sig_d = np.array([0.20,0.20,0.20,0.20,0.20,0.20,0.20,0.20,0.20,0.20])

#We beginnen met het plotten van de meetdata
f,ax = plt.subplots(1)
ax.errorbar(t,d,xerr=0.0,yerr=sig_d,fmt='k.', label='Meetset')

#We beginnen met een gokje voor de waardes A en B
A_start=2.6 
B_start=1.5

#We definieren een functie die het model bevat, een wortelfunctie in dit geval
#B is een vector met parameters, in dit geval twee (A = B[0], B = B[1])
#x is de array met x-waarden

def f(B, x):
    return (B[0] + B[1]*x)**0.5

#We definieren het model om te gebruiken in odr
odr_model = odr.Model(f)

## (3) Definieer een RealData object
## Een RealData-object vraagt om de onzekerheden in beide richtingen. 
odr_data  = odr.RealData(t,d,sy=sig_d)

## (4) Maak een ODR object met data, model en startwaarden
odr_obj   = odr.ODR(odr_data,odr_model,beta0=[A_start,B_start])

#Omdat de onzekerheid in de x-richting gelijk is aan nul in ons geval, moeten we 
#een kleinste kwadraat aanpassing instellen met het volgend regeltje
odr_obj.set_job(fit_type=2)

#hier voeren we de fit uit
odr_res   = odr_obj.run()

#de beste schatters voor de parameters
par_best = odr_res.beta
#dit zijn de externe onzekerheden
par_sig_ext = odr_res.sd_beta

#De interne covariantiematrix
par_cov = odr_res.cov_beta 
print(" De (INTERNE!) covariantiematrix  = \n", par_cov)

#De chi-kwadraat en de gereduceerde chi-kwadraat van deze aanpassing
chi2 = odr_res.sum_square
print("\n Chi-squared         = ", chi2)
chi2red = odr_res.res_var
print(" Reduced chi-squared = ", chi2red, "\n")

#Een compacte weergave van de belangrijkste resultaten als output
odr_res.pprint()

# Hier plotten we ter controle de aanpassing met de dataset
xplot = np.linspace(0,10,1000)

ax.plot(xplot,(par_best[0] + par_best[1]*xplot)**0.5, '-r', label='Aangepaste set')
#Hier zorgen we ervoor dat we ook de onzekerheden van het model plotten
ax.fill_between(xplot,f(par_best-par_sig_ext,xplot),f(par_best+par_sig_ext,xplot), label='Error in het model')
ax.set_xlim(0) #dit zorgt ervoor dat het plotje begint bij x = 0

#as-labels
plt.xlabel("Tijd in uren")
plt.ylabel("Dikte in cm")

#legenda
plt.legend(loc='upper left')
plt.savefig("Plotss.pdf")
plt.show()

