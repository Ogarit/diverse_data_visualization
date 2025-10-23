import matplotlib.pyplot as plt
from random_walk import RandomWalk
import gui_dimensions as gd


def keep_running():
    """Verifica se continuará com outra caminhada."""
    option = input("Fazer outra caminhada? (s/n): ")
    if option.lower() == 'n':
        return False
    elif option.lower() != 's':
        print('Selecione uma opção válida!')
        return keep_running()
    else:
        return True


dimensions = gd.get_gui_size()
dpi = gd.get_dpi()

# Continua criando passeios novos desde que o programa esteja ativo
while True:
    # Cria um random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plota os pontos no passeio
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(dimensions['x'], dimensions['y']), dpi=dpi)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, color='blue', linewidth=1)
    ax.set_aspect('equal')

    ax.scatter(0, 0, c='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    # Remove os eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    if not keep_running():
        break
