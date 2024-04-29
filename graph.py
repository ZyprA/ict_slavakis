import math
import matplotlib.pyplot as plt

def Tn(n,t):
    result = 1
    for i in range(n):
        k = i + 1
        result += 2/(1+16*k*k)*math.cos(2*k*t) + 8*k/(1+16*k*k)*math.sin(2*k*t) # omega = 2
    result = result * 0.504
    return result

tmax = math.pi
dif = 0.01
t = 0
xl1 = []
xl2 = []
xl3 = []
xl4 = []
xl5 = []
tl = []

while (t <= tmax):
    tl.append(t)
    x1 = math.exp(-t/2)
    xl1.append(x1)
    x2 = Tn(1,t)
    xl2.append(x2)
    x3 = Tn(5,t)
    xl3.append(x3)
    x4 = Tn(10,t)
    xl4.append(x4)
    x5 = Tn(20,t)
    xl5.append(x5)
    t += dif


plt.plot(tl, xl2, label="T1")
plt.plot(tl, xl3, label="T5")
plt.plot(tl, xl4, label="T10")
plt.plot(tl, xl5, label="T20")
plt.plot(tl, xl1, label="x(t)")
plt.legend()
plt.savefig("figure.png", dpi=300) 