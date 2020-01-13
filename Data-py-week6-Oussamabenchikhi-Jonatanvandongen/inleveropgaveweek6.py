#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 20:55:30 2019

@author: Oussama Benchikhi en Jonatan van Dongen
"""

#welkom bij dit script. In ons script gaan we de fourierreeks bekijken

#zoals gewoonlijk beginnen we met het importeren 
import numpy as np
import matplotlib.pyplot as plt

##########
#Hier beginnen we met het definieren van de fourierfunctie
def fourierfunctie(A,j,f0,t,phi=0,t0=0):
    return np.sin(j*2*np.pi*f0*(t-t0)+ phi)*A 
    

#in deze loop maken we de reeks voor verschillende n termen
def fourierreeks(Aj,f0j,t):
    waarde = 0
    for j in range(len(Aj)):
        waarde += fourierfunctie(Aj[j],j,f0j[j],t)
    return waarde

##########
#Hier definieren we de Zaagtand, driehoek en de sinus functies 
def Z(t):
   return f0*t-np.floor(f0*t) - 0.5

def S(t):
    return np.sin(2*np.pi*f0*t)

def D(t):
    return 4*np.abs(f0*t + 0.25 - np.floor(f0*t + 0.75)) - 1


#We plotten hier nu alle drie in een figuur 
t = np.linspace(0,1,100000)

plt.figure()
#f0 zetten we hier op 2
f0 = 2
plt.plot(t,D(t), label='D(t)')
plt.plot(t,S(t), label='S(t)')
plt.plot(t,Z(t), label='Z(t)')
plt.legend(loc="upper right", title='F0 = 2')

plt.ylabel("") #Het zijn allemaal dimensieloze functies en dus heb je geen grootheid of eenheid op de y as
plt.xlabel("$t$")
plt.savefig("alledrie.pdf")
plt.show()

#voor het gemak houden we nu f0 = 1 aan
f0 = 1 

#We beginnen met het benaderen van de zaagtand functie hier
#We definieren hier voor elke n de functie die hoort bij de zaagtand functie.

def N(n):
    if n == 0:
        return 0
    elif n >= 1:
        return -1/(n*np.pi)

#Nu beginnen we met het plotten van verschillende benaderingen bij verschillende n's
plt.figure()
x = 5 #dit is de "n" en hoevaak we dus reeksen 
dx = 1

#we maken een lijst voor alle y waardes die de functie geeft bij de gegeven n waardes
nlist = [i*dx for i in range(x)]
ylistZ5 = [N(n) for n in nlist]
f0lijst = [f0 for i in range(x)] #hier maken we een lijst van eenen die even lang is als de gekozen aantal termen

#Nu plotten we de fourierreeks tegen de tijd
plt.plot(t,fourierreeks(ylistZ5, f0lijst, t), label='n=5')

#Hier doen we hetzelfde voor het aantal termen 25 en 50
x = 25
dx = 1

nlist = [i*dx for i in range(x)]
ylistZ25 = [N(n) for n in nlist]
f0lijst = [f0 for i in range(x)]

plt.plot(t,fourierreeks(ylistZ25, f0lijst, t), label='n=25')

x = 50
dx = 1

nlist = [i*dx for i in range(x)]
ylistZ50 = [N(n) for n in nlist]
f0lijst = [f0 for i in range(x)]

plt.plot(t,fourierreeks(ylistZ50, f0lijst, t), label='n=50')

#Hier plotten we ook even de orginele functie zodat je mooi het orgineel tegen de benaderingen ziet
plt.plot(t,Z(t), label='orgineel')
plt.legend(loc="upper left")
plt.savefig("BenaderingZaag.pdf")

plt.ylabel("") 
plt.xlabel("$t$")
plt.savefig("Bendaering Z(t).pdf")
plt.show()


#Nu beginnen we met het benaderen van de coeficient voor de driehoek functie

def Dn(n):
    if n % 2 == 0: 
        return 0
    else:
        return ((8/(np.pi)**2)*((-1)**((n-1)/2)))/n**2
    
#Nu plotten we de benaderingen, dit doen we precies hetzelfde als bij de zaagtand functie
#Hier kiezen we voor N, 5,7 en 50

plt.figure()
x1 = 5
dx1 = 1

nlist = [i*dx1 for i in range(x1)]
ylistD5 = [Dn(n) for n in nlist]
f0lijst1 = [f0 for i in range(x1)]

plt.plot(t,fourierreeks(ylistD5, f0lijst1, t), label='n=5')

x1 = 25
dx1 = 1

nlist = [i*dx1 for i in range(x1)]
ylistD25 = [Dn(n) for n in nlist]
f0lijst1 = [f0 for i in range(x1)]

plt.plot(t,fourierreeks(ylistD25, f0lijst1, t), label='n=25')

x1 = 50
dx1 = 1

nlist = [i*dx1 for i in range(x1)]
ylistD50 = [Dn(n) for n in nlist]
f0lijst1 = [f0 for i in range(x1)]

plt.plot(t,fourierreeks(ylistD50, f0lijst1, t), label='n=50')

plt.plot(t,D(t), label='orgineel')
plt.savefig("BenaderingDriehoek.pdf")
plt.legend(loc="upper right")

plt.ylabel("") 
plt.xlabel("$t$")
plt.savefig("benadering D(t).pdf")
plt.show()

#Nu beginnen we met de kwadratische verschillen. 

plt.figure() 
#We doen dit door de verschillende fourierreeksen - de orginele functies te doen en dat te kwadrateren
errorZ5 = ((fourierreeks(ylistZ5, f0lijst, t)) - Z(t))**2
plt.plot(t, errorZ5, label='Verschil voor n=5') 

errorZ25 = ((fourierreeks(ylistZ25, f0lijst, t)) - Z(t))**2
plt.plot(t, errorZ25, label='Verschil voor n=25')

errorZ50 = ((fourierreeks(ylistZ50, f0lijst, t)) - Z(t))**2
plt.plot(t, errorZ50, label='Verschil voor n=50')
plt.legend(loc='best')

plt.ylabel("Kwadratisch verschil")
plt.xlabel("$t$")
plt.savefig("Kwadritsch veschilZ.pdf")
plt.show() #We gebruiken plt.figure() en plt.show() om alles in 1 figuur te krijgen


#Hier doen we weer precies het zelfde voor de kwadratische verschillen voor de driehoeksfunctie
plt.figure()
errorD5 = ((fourierreeks(ylistD5, f0lijst, t)) - D(t))**2
plt.plot(t, errorD5, label='Verschil voor n=5')

errorD25 = ((fourierreeks(ylistD25, f0lijst, t)) - D(t))**2
plt.plot(t, errorD25, label='Verschil voor n=25')

errorD50 = ((fourierreeks(ylistD50, f0lijst, t)) - D(t))**2
plt.plot(t, errorD50, label='Verschil voor n=50')
plt.legend(loc='best')

plt.ylabel("Kwadratisch verschil")
plt.xlabel("$t$")
plt.savefig("Kwadratisch verschilD.pdf")
plt.show()
#Nu gaan we het gemiddelde kwadratische verschil tegen het aantal termen, n, plotten
plt.figure()

#we beginnen met een lijst maken van de gemiddelde kwadratische afwijkingen voor zowel D als Z
GemD = [np.mean(errorD5), np.mean(errorD25), np.mean(errorD50)]
nD = [5, 25, 50]

GemZ = [np.mean(errorZ5), np.mean(errorZ25), np.mean(errorZ50)]
nZ = [5, 25, 50]

plt.plot(nD, GemD, label='D')
plt.plot(nZ, GemZ, label='Z')

#we nemen als y-schaal de logaritmische schaal
plt.yscale("log")
plt.ylabel("Gemiddelde kwadratische verschil")
plt.xlabel("Aantal termen n")
plt.legend(loc='best')
plt.savefig("gemiddeld kwadratische verschil.pdf")
plt.show()

#Nu printen we even de waarde voor de totale gemiddelde afwijking
#dus we nemen al onze gemeten afwijkingen en nemen daar het gemiddelde van
print("Totaal gemiddelde afwijking voor de driehoeksgolf = ",(np.mean(errorD5) + np.mean(errorD25) + np.mean(errorD50))/3)
print("Totaal gemiddelde afwijking voor de zaagtandgolf =", (np.mean(errorZ5) + np.mean(errorZ25) + np.mean(errorZ50))/3)



