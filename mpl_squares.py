import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Define o título do gráfico e os eixos do rótulo
ax.set_title("Números Quadrados", fontsize=14)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Quadrados dos Valores", fontsize=14)

# Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize=14)

plt.show()
