import matplotlib.pyplot as plt
from die import Die

# Cria um D6
die = Die()

# Realiza alguns testes e armazena os resultados em uma lista
results = [die.roll() for _ in range(1_000_000)]

# Analisa os resultados
poss_results = range(1, die.num_sides+1)
frequencies = [results.count(value) for value in poss_results]

# Visualiza os resultados
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(poss_results, frequencies)

ax.set_title("Resultados da Rolagem de um D6 1.000.000 Vezes")
ax.set_xlabel("Resultado")
ax.set_ylabel("Frequência do Resultado")

plt.show()
