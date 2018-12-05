import math as mt
import sympy as sp


def Dw(t,o,pi,net):


    return (o-t)/(mt.cosh(net)**2)*pi*4.3

say=0
maxx=0
maxy=0
w1=0.025
w2=0.015
w3=0.12
b=list()
ak=0
z='0'
zon=True




lines = list()
while True:
  s =input()
  if s:
    lines.append(s.split(","))
    b=s.split(',')
    if float(b[0])>maxx:
        maxx=float(b[0])
    if float(b[1])>maxy:
        maxy=float(b[1])

  else:
    break;


for i in lines:
  if len(i)==3:

    if float(i[0]) != 0 and float(i[1]) != 0  and float(i[2]) != 0:

        net1 = w1 * float(i[0])//maxx  + w2 * float(i[1])//maxy  + (1 * w3)
        f_net = mt.tanh(net1)

        w1 = w1 - Dw(float(i[2]), f_net, float(i[0])//maxx , net1)  # True , çıktı , p1        #back propagation
        w2 = w2 - Dw(float(i[2]), f_net, float(i[1])//maxy , net1)  # True , çıktı , p2        #back propagation
        w3 = w3 - Dw(float(i[2]), f_net, 1, net1)

  if len(i)==2:

         net2 = w1 * float(i[0])//maxx  + w2 * float(i[1])/maxy + (1 * w3)
         sonuc = mt.tanh(net2)
         if round(sonuc) == 1:
             print("+1")
         if round(sonuc) ==-1:
             print("-1")
