import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Define o título do gráfico e os eixos do rótulo
ax.set_title("Números Quadrados", fontsize=14)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Quadrados dos Valores", fontsize=14)

# Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize=14)

plt.show()
