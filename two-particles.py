from time import sleep
import numpy as np

def force(r_1, r_2, k=1e-4, eq=1):
    extension = r_2 - r_1
    return -k * (extension - eq)

def step(v, x_2, F, a_1, dt):
    v = v + F * dt / 2
    x_2 = x_2 * v * dt
    F = force(x_2, a_1)
    v = v + F * dt / 2
    return v, x_2, F, a_1


n = 2
r = np.zeros(shape=(n, 3))
r[0][0] = 2
v = np.zeros(shape=(n, 3))
F = np.zeros(shape=(n, 3))

v = 0
a_1 = np.array([0.00000000, 0.00000000]).reshape(-1, 1)
x_2 = np.array([0.00000000, 20.000000000]).reshape(-1, 1)
F = force(a_1, x_2)
t = 0
dt = 1e-5

with open("two-particles.xyz", "w+") as output:
    print("pos:", x_2)
    # print("velocity", float(v))
    print("Force", F)


    print(2, file=output)
    print(f"time={t}", file=output)
    print(f"O {float(x_2[0])} {float(x_2[1])} 0.0", file=output)
    print(f"O {float(a_1[0])} {float(a_1[1])} 0.0", file=output)

    for _ in range(100):
        print("pos:", x_2)
        # print("velocity", float(v))
        print("Force", F)
        v, x_2, F, a_1 = step(v, x_2, F, a_1, dt)
        t += dt

        print(2, file=output)
        print(f"time={t}", file=output)
        print(f"O {float(x_2[0])} {float(x_2[1])} 0.0", file=output)
        print(f"O {a_1[0]} {a_1[1]} 0.0", file=output)
        