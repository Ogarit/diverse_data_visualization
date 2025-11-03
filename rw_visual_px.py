import plotly.express as px
from random_walk import RandomWalk


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


# Continua criando passeios novos desde que o programa esteja ativo
while True:
    # Cria um random walk
    rw = RandomWalk()
    rw.fill_walk(True)

    # Máximo de ponto
    total_points = range(rw.num_points)

    # Plota os pontos no passeio
    title = "Passeio aleatório em 3D"
    fig = px.scatter_3d(x=rw.x_values, y=rw.y_values, z=rw.z_values,
                        color=total_points, title=title)

    fig.show()

    if not keep_running():
        break
