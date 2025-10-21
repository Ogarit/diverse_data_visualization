import matplotlib.pyplot as plt

x_values = range(1, 5_001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
_, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=10)

# Título do gráfico e dos rótulos
ax.set_title("Números Cúbicos", fontsize=14)
ax.set_xlabel("Valores", fontsize=14)
ax.set_ylabel("Cubo dos Valores", fontsize=14)

# Tamanho das marcações de escala
ax.tick_params(labelsize=14)
ax.axis([0, 5_000, 0, 125_000_000_000])

plt.show()
