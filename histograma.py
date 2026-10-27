
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Localização da pasta do projeto
BASE = Path(__file__).resolve().parent

# Geração dos dados simulados
gerador = np.random.default_rng(42)
dados = gerador.normal(
    loc=50,
    scale=10,
    size=500
)

# Construção do histograma
fig, ax = plt.subplots(figsize=(9, 5.2))

ax.hist(
    dados,
    bins=18,
    edgecolor="white"
)

ax.set_title("Histograma de dados simulados")
ax.set_xlabel("Valor")
ax.set_ylabel("Frequência")
ax.grid(axis="y", alpha=0.25)

fig.tight_layout()

# Salva o gráfico para a página web
destino = BASE / "static" / "graficos" / "histograma.png"
fig.savefig(destino, dpi=150)

plt.close(fig)

print("Histograma gerado com sucesso!")
