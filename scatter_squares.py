import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=10)

# Define o título do gráfico e os exios do rótulo
ax.set_title("Números quadrados", fontsize=14)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Quadrado dos Valores", fontsize=14)

# Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize=14)

# Define o intervalo para cada eixo
ax.axis([0, 1_000, 0, 1_100_000])

plt.show()
