# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:45:06 2020

@author: 79652
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:40:33 2020

@author: 79652
"""
import numpy as np
import matplotlib.pyplot as plt

Td0=70
Ta0=35
T0=20
H=1500
ht=2.2304408272582124
ha=3.635241970705732
z0=0
h=0.1
g=0.02
B=37.66071665001653

Td=[]
Ta=[]
Tg=[]
Z=[]
tg=T0
#z=np.linspace(0,1500,150)
#z=np.arange(z0,H+h,h)
N=H/h
i=0
while i<N:
    i+=1
    k11=h*(Ta0-Td0)/B
    k21=h*ha*((tg-Ta0)-(Ta0-Td0))/(B*ht)
    k12=h*((Ta0+k11/2)-(Td0+k21/2))/B
    k22=h*ha*((tg-(Ta0+k21/2))-((Ta0+k21/2)-(Td0+k11/2)))/(B*ht)
    k13=h*((Ta0+k12/2)-(Td0+k22/2))/B
    k23=h*ha*((tg-(Ta0+k22/2))-((Ta0+k22/2)-(Td0+k12/2)))/(B*ht)
    k14=h*((Ta0+k13)-(Td0+k23))/B
    k24=h*ha*((tg-(Ta0+k23))-((Ta0+k23)-(Td0+k13)))/(B*ht)
    
    t1=Td0+(k11+2*k12+2*k13+k14)/6
    t2=Ta0+(k21+2*k22+2*k23+k24)/6
    
    Td0=t1
    Ta0=t2
    z0=z0+h
    tg=tg+g*h
    
    Z=Z+[i*h]
    Td=Td+[t1]
    Ta=Ta+[t2]
    Tg=Tg+[tg]

"""Td=[70]+Td
Ta=[35]+Ta
Tg=[20]+Tg
Z=[0]+Z"""

fig=plt.figure()
plt.plot(Td,Z, label = '$\ Td $')
plt.plot(Ta,Z, label = '$\ Ta $')
plt.plot(Tg,Z, label = '$\ Tg $')
plt.gca().invert_yaxis()
plt.grid(True)
plt.ylabel('Z')
plt.xlabel('T')
plt.legend()
plt.show() 







