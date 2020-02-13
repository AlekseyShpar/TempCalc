# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:21:51 2020

@author: 79652
"""

import math 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

z1=[] 
ta1=[]
td1=[]
tf=[]
'''
print ("Папаметры скважины:") #начало ввода данных пользователем
d10=float(input("Внутрненний диаметр малого НКТ: "))
d20=float(input("Внешний диаметр малого НКТ: "))
lt=float(input("Теплопроводность НКТ: "))
d30=float(input("Внутрненний диаметр большого НКТ: "))
d40=float(input("Внешний диаметр большого НКТ: "))
ltt=float(input("Теплопроводность НКТ: "))
d50=float(input("Внутрненний диаметр колонны: "))
d60=float(input("Внешний диаметр колонны: "))
lc=float(input("Теплопроводность стенки колонны: "))
dw0=float(input("Диаметр скважины: " ))

print ("Папаметры рабочей жидкости: ")
cm=float(input("Удельная теплоёмкость: " ))
rm=float(input("Плотность: " ))
lm=float(input("Теплопроводность: " ))
mu0=float(input("Динамическая вязкость: " ))
q0=float(input("Расход (объёмный): " ))

print ("Граничные значения:")
td0=float(input("Температура рабочей жидкости на поверхности h=0: "))
t0=float(input("Температура нейтрального слоя: "))
print ("Глубины:")
H=float(input("Спуска НКТ: "))
h=float(input("Шаг на графике: "))

print ("Параметры породы:")
lcem=float(input("Теплопроводность цемента: "))
lf=float(input("Теплопроводность породы: "))
cf=float(input("Теплоёмкость пород: "))
rf=float(input("Плотность пород: "))
g=float(input("Геотермический градиент: "))

print ("Продолжительность промывки")
t=float(input("Время промывки в часах: ")) #конец ввода данных пользователем
'''
print ("Папаметры скважины:") #начало ввода данных пользователем
d10=62
d20=73
lt=45.4
d30=126
d40=146
#ltt=float(input("Теплопроводность НКТ: "))
#d50=float(input("Внутрненний диаметр колонны: "))
#d60=float(input("Внешний диаметр колонны: "))
lc=45.4
dw0=216

print ("Папаметры рабочей жидкости: ")
cm=4200
rm=130
lm=0.4
mu0=30
q0=0.5

print ("Граничные значения:")
td0=70
t0=20
print ("Глубины:")
H=1500
h=10

print ("Параметры породы:")
lcem=0.73
lf=1.5
cf=2200
rf=2700
g=0.02

print ("Продолжительность промывки")
t=100



d1=float(d10/1000) #перевод величин в размерности, удобные для расчёта
d2=float(d20/1000)
d3=float(d30/1000)
d4=float(d40/1000)
#d5=float(d50/1000)
#d6=float(d60/1000)
dw=float(dw0/1000)
qv=float(q0/3600)
q=float(qv*rm)
mu=float(mu0/1000)

alf=float(lf/(cf*rf)) #влияние продолжительности промывки
tay=float(t*3600*alf/dw)
tt=float(math.log(math.exp(-0.28*tay)+(1.5-0.3719*math.exp(-tay))*tay**(1/2)))

vd=float(q/(3.14*rm*d1*d1/4)) #скорость потока в НКТ
va=float(q/(3.14*rm*(d3*d3/4 - d2*d2/4))) #скорость потока в затрубном пространстве

red=float(rm*vd*d1/mu) #число Рейнольдса в НКТ
rea=float(rm*va*(d3-d2)/mu) #число Рейнольдса в затрубном пространстве

pr=float(mu*cm/lm) #число Прандтля

if red>=4000: #выбор числа Нуссульта для потока в НКТ
    nud=float(0.021*(red**0.8)*pr**0.43)
elif red<2100:
    nud=4.36
else:
    nud=float(4.36+(0.021*(red**0.8)*(pr**0.43)-4.36))
    
if rea>=4000: #выбор числа Нуссульта для потока в затрубном пространстве
    nua=float(0.021*(red**0.8)*pr**0.43)
elif rea<2100:
    nua=4.36
else:
    nua=float(4.36+(0.021*(red**0.8)*(pr**0.43)-4.36))
    
#ha=float(6.28/(2*(d30-d20)/(d20*nua*lm)+(1/lc)*math.log(d40/d30)+(1/lcem)*math.log(dw0/d40)+(1/lt)*math.log(d40/d30)+(1/lx)*math.log(d50/d40)+(tt/lf))) #подсчёт коэффициентов теплообмена
ha=float(6.28/((2*(d3-d2)/(d2*nua*lm))+((math.log(d4/d3))/lc)+(math.log(dw/d4)/lcem)+tt/lf))
#ht=float(6.28/(2*(d3-d2)/(d2*nua)+2/(lm*nud)+(1/lt)*math.log(d2/d1)+2*(d3-d2)/(lm*nud*d2)))
ht=float(6.28/((2*(d3-d2)/(d2*nua*lm))+(2/(lm*nud))+((math.log(d2/d1))/lt)+(2*(d3-d2)/(d2*nud*lm))))
b=float(cm*g/ht)

l1=float(ha/(2*b*ht)+1/(2*b)*((ha/ht)**2+4*(ha/ht))**(1/2)) #подсчёт корней характеристического полинома
l2=float(ha/(2*b*ht)-1/(2*b)*((ha/ht)**2+4*(ha/ht))**(1/2))

c1=float(-(((td0+b*g-t0)*l2*math.exp(l2*H)+g)/(l1*math.exp(l1*H)-l2*math.exp(l2*H)))) #нахождение постоянных
c2=float(((td0+b*g-t0)*l1*math.exp(l1*H)+g)/(l1*math.exp(l1*H)-l2*math.exp(l2*H)))
z=0
while z<=H:
    td=float(c1*math.exp(l1*z)+c2*math.exp(l2*z)+t0+g*z-b*g) #подсчёт температур с заданным шагом
    ta=float(b*l1*c1*math.exp(l1*z)+b*l2*c2*math.exp(l2*z)+b*g+td)
    tf1=float(t0+g*z)
    print(z,td,ta) #вывод значений температур на соответствующих глубинах
    z+=h #перебор глубин с заданным шагом
    z1=z1+[z]
    ta1=ta1+[ta]
    td1=td1+[td]
    tf=tf+[tf1]
    
ttt=float(c1*math.exp(l1*H)+c2*math.exp(l2*H)+t0+g*H-b*g) #подсчёт температуры рабочей жидкости на глубине H
print("Температура на максимальной глубине спуска НКТ: ", ttt)
print ("ht", ht)
print ("ha", ha)
print ("l1", l1)
print ("l2", l2)
print ("c1", c1)
print ("c2", c2)
print ("B", b)

#fig=plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')

"""fig=plt.figure(figsize=(10,25)) #вывод графика зависимости температур от глубины
fig = plt.axes()
plt.plot(ta1,z1, label = 'Ta')
plt.plot(td1,z1, label = 'Td')
plt.plot(tf,z1, label = 'G')
plt.gca().invert_yaxis()
fig.yaxis.set_major_locator(ticker.MultipleLocator(50))
fig.xaxis.set_major_locator(ticker.MultipleLocator(5))
plt.grid(True) 
plt.ylabel('z')
plt.xlabel('T')
plt.legend()
fig = plt.gcf()
plt.show()  

fig.savefig("graf.png")"""

fig=plt.figure()
plt.plot(td1,z1, label = '$\ Td $')
plt.plot(ta1,z1, label = '$\ Ta $')
plt.plot(tf,z1, label = '$\ Tg $')
plt.gca().invert_yaxis()
plt.grid(True)
plt.ylabel('Z')
plt.xlabel('T')
plt.legend()
plt.show() 
