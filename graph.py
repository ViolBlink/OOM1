import numpy as np
import matplotlib.pyplot as plt

f = open('Config.txt')

Arr = f.read()
Arr = Arr.split("\n")

N = int(Arr[0].split(" ")[2])

J = int(Arr[1].split(" ")[2])

T = int(Arr[2].split(" ")[2])

f.close()

f = open('Data.txt')

Lattis = np.zeros((J + 1, N + 1))
Arr = []

for x in f:
    Arr.append(float(x))

i = 0

for j in range(N + 1):
    for q in range(J + 1):
        Lattis[q][j] = Arr[i]
        i = i + 1

X = np.linspace(0, -1, N + 1)
Y = np.linspace(0, T, J + 1)

gx, gt = np.meshgrid(X, Y)

fig1 = plt.figure(figsize=(10, 10))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.plot_surface(gx, gt, Lattis,
                cmap='viridis', edgecolor='none')
ax1.set_title('Численное решение')

fig2 = plt.figure(figsize=(10, 10))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_wireframe(gx, gt, Lattis, rstride=10,cstride=10)
ax2.set_title('Численное решение')

plt.xlabel('x')
plt.ylabel('t')
plt.show()