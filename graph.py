import numpy as np
import matplotlib.pyplot as plt

f = open('Config.txt')

Arr = f.read()
Arr = Arr.split("\n")

N = int(Arr[0].split(" ")[2])

J = int(Arr[1].split(" ")[2])

T = int(Arr[2].split(" ")[2])

AN = int(Arr[4].split(" ")[2])

AJ = int(Arr[5].split(" ")[2])

f.close()

""" Аналитический счет """

# Создаем макет для графика

fig = plt.figure(figsize=(8, 8)) # Для характеристик
fig1 = plt.figure(figsize=(8, 8)) # Для 3Д граффика

ax = fig.add_subplot(111) # Сетка для характеристик
ax1 = fig1.add_subplot(111, projection='3d') # Сетка для 3Д

fig2 = plt.figure(figsize=(10, 10))
ax2 = fig2.add_subplot(111, projection='3d')

ax1.set_title('Аналитическое решение')
ax1.set_ylabel('Время t')
ax1.set_xlabel('Координата x')
ax1.set_zlabel('U(x,t)')

for i in range(AN):
    # Текущая точка 
    x0 = -float(i/AN)
    # Точки по x 
    x = np.linspace(-1, 0, AN)

    # Создаем характеристку
    t = (x0 - x)/(2 - (4/np.pi) * np.arctan(x0 + 2))

    if(x0 == 0):
        ax.plot(x, t, 'b', linewidth=2)

    ax.plot(x, t, linewidth=0.5)

    # Задаем значение по характеристике
    u = 2 - (4/np.pi) * np.arctan(x0 + 2)
    # Рисуем
    ax1.plot(x, t, u,'red',linewidth=0.5)
    ax2.plot(x, t, u,'red',linewidth=0.5)

for i in range(AJ):
    # Текущая точка 
    t0 = float(i/AJ)
    # Точки по x 
    x = np.linspace(-1, 0, AN)

    # Создаем характеристку
    t = t0 - x*np.exp(t0)/(2 - (4/np.pi) * np.arctan(2))

    ax.plot(x, t, linewidth=0.5)

    # Задаем значение по характеристике
    u = (2 - (4/np.pi) * np.arctan(2)) * np.exp(-t0)
    # Рисуем
    ax1.plot(x, t, u,'green',linewidth=0.5)
    ax2.plot(x, t, u,'red',linewidth=0.5)

ax.grid(True)

""" Конец аналитического счета """

""" Численый счет """

f = open('Data.txt')

Lattis = np.zeros((J + 1, N + 1))
Arr = []

for x in f:
    Arr.append(float(x))

count = 0

for j in range(N + 1):
    for q in range(J + 1):
        Lattis[q][j] = Arr[count]
        count = count + 1

X = np.linspace(0, -1, N + 1)
Y = np.linspace(0, T, J + 1)

gx, gt = np.meshgrid(X, Y)

ax2.plot_wireframe(gx, gt, Lattis, rstride=10,cstride=10)
ax2.set_title('Численное и аналитическое решение')
ax2.set_ylabel('Время t')
ax2.set_xlabel('Координата x')
ax2.set_zlabel('U(x,t)')

fig3 = plt.figure(figsize=(10, 10))
ax3 = fig3.add_subplot(111, projection='3d')
ax3.plot_wireframe(gx, gt, Lattis, rstride=10,cstride=10)
ax3.set_title('Численное решение')
ax3.set_ylabel('Время t')
ax3.set_xlabel('Координата x')
ax3.set_zlabel('U(x,t)')

plt.show()