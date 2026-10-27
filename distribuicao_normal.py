
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent

# Parâmetros da distribuição normal
media = 50
desvio_padrao = 10

# Valores do eixo X
x = np.linspace(
    media - 4 * desvio_padrao,
    media + 4 * desvio_padrao,
    500
)

# Densidade de probabilidade da distribuição normal
y = (
    1 / (desvio_padrao * np.sqrt(2 * np.pi))
) * np.exp(
    -0.5 * ((x - media) / desvio_padrao) ** 2
)

# Construção do gráfico
fig, ax = plt.subplots(figsize=(9, 5.2))

ax.plot(x, y, linewidth=2.5)
ax.fill_between(x, y, alpha=0.2)

ax.set_title("Distribuição normal")
ax.set_xlabel("Valor")
ax.set_ylabel("Densidade de probabilidade")
ax.grid(alpha=0.25)

fig.tight_layout()

# Salva a imagem
destino = (
    BASE / "static" / "graficos" /
    "distribuicao_normal.png"
)

fig.savefig(destino, dpi=150)

plt.close(fig)

print("Distribuição normal gerada com sucesso!")
