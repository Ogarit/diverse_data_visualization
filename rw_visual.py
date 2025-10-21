import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Continua criando passeios novos desde que o programa esteja ativo
while True:
    # Cria um random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plota os pontos no passeio
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.YlGnBu,
               s=15)
    ax.set_aspect('equal')

    ax.scatter(0, 0, c='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    plt.show()

    keep_running = input("Fazer outra caminhada? (s/n): ")
    if keep_running.lower() == 'n':
        break
