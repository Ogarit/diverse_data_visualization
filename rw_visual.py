import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Cria um random walk
rw = RandomWalk()
rw.fill_walk()

# Plota os pontos no passeio
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')

plt.show()
