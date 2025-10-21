import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200)

# Define o título do gráfico e os exios do rótulo
ax.set_title("Números quadrados", fontsize=14)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Quadrado dos Valores", fontsize=14)

# Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize=14)

plt.show()
