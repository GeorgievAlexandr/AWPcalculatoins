import matplotlib.pyplot as plt
pM = 3.33 #масса пороха
pv = (pM / 30) * 4988.7
m = 0.01 #масса пули
length = 1 #длина ствола
nowX = 0.05 #начальная позиция
v = 0 #начальная скорость
s = 0.01**2 * 3.1415
iterations = 300000
x = []
y = []
for t in range(0,1000):
    if nowX < length:
        a = pv/(nowX*m)
        p = pv/(nowX*s)
        nowX += v/iterations + a/(2*iterations**2)
        v += a/iterations
        x.append(nowX) #время
        y.append(p/1000000)#то что хочешь построить
        print("t", t /iterations, "nowX", nowX, "V", v, "a", a, "p", p)
plt.plot(x, y)
plt.xlabel("Координата, м")
plt.ylabel("Давление, Мпа")
plt.show()