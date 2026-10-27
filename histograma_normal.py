
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent

# Parâmetros da distribuição
media = 50
desvio_padrao = 10

# Gera dados simulados
gerador = np.random.default_rng(42)

dados = gerador.normal(
    loc=media,
    scale=desvio_padrao,
    size=800
)

# Calcula a curva normal
x = np.linspace(
    media - 4 * desvio_padrao,
    media + 4 * desvio_padrao,
    500
)

y = (
    1 / (desvio_padrao * np.sqrt(2 * np.pi))
) * np.exp(
    -0.5 * ((x - media) / desvio_padrao) ** 2
)

# Desenha os dois gráficos juntos
fig, ax = plt.subplots(figsize=(9, 5.2))

ax.hist(
    dados,
    bins=22,
    density=True,
    alpha=0.65,
    edgecolor="white",
    label="Histograma"
)

ax.plot(
    x,
    y,
    linewidth=2.5,
    label="Curva normal teórica"
)

ax.set_title("Histograma e distribuição normal")
ax.set_xlabel("Valor")
ax.set_ylabel("Densidade")
ax.legend()
ax.grid(alpha=0.25)

fig.tight_layout()

# Salva a imagem combinada
destino = (
    BASE / "static" / "graficos" /
    "histograma_normal.png"
)

fig.savefig(destino, dpi=150)

plt.close(fig)

print("Gráfico combinado gerado com sucesso!")
