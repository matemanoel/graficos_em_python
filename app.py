
from flask import Flask, render_template, send_file, jsonify
from pathlib import Path
import subprocess
import sys

app = Flask(__name__)

BASE = Path(__file__).resolve().parent

# Programas Python que serão executados
SCRIPTS = {
    "histograma": BASE / "histograma.py",
    "normal": BASE / "distribuicao_normal.py",
    "combinado": BASE / "histograma_normal.py"
}

# Imagens produzidas pelos programas
IMAGENS = {
    "histograma": BASE / "static/graficos/histograma.png",
    "normal": BASE / "static/graficos/distribuicao_normal.png",
    "combinado": BASE / "static/graficos/histograma_normal.png"
}


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/grafico/<tipo>")
def gerar_grafico(tipo):
    if tipo not in SCRIPTS:
        return jsonify({
            "erro": "Tipo de gráfico inválido."
        }), 404

    try:
        resultado = subprocess.run(
            [sys.executable, str(SCRIPTS[tipo])],
            cwd=str(BASE),
            capture_output=True,
            text=True,
            timeout=30
        )

        if resultado.returncode != 0:
            return jsonify({
                "erro": "Erro ao executar o programa Python.",
                "detalhes": resultado.stderr[-1200:]
            }), 500

        imagem = IMAGENS[tipo]

        if not imagem.exists():
            return jsonify({
                "erro": "A imagem do gráfico não foi criada."
            }), 500

        return send_file(
            imagem,
            mimetype="image/png",
            max_age=0
        )

    except subprocess.TimeoutExpired:
        return jsonify({
            "erro": "Tempo limite excedido ao gerar o gráfico."
        }), 504


if __name__ == "__main__":
    app.run(debug=True)
