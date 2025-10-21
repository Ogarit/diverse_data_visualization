import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Define o título do gráfico e os exios do rótulo
ax.set_title("Números quadrados", fontsize=14)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Quadrado dos Valores", fontsize=14)

# Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize=14)

plt.show()
