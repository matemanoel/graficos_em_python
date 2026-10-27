
const nomes = {
    histograma: "Histograma",
    normal: "Distribuição normal",
    combinado: "Histograma + distribuição normal"
};

const resultado = document.getElementById("resultado");
const titulo = document.getElementById("titulo-grafico");
const mensagem = document.getElementById("mensagem");
const imagem = document.getElementById("grafico-gerado");

document.querySelectorAll("[data-grafico]").forEach((cartao) => {

    cartao.addEventListener("click", async () => {

        const tipo = cartao.dataset.grafico;

        resultado.hidden = false;
        titulo.textContent = nomes[tipo];
        mensagem.textContent = "Executando o programa Python...";
        imagem.hidden = true;
        imagem.removeAttribute("src");

        resultado.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });

        try {
            const resposta = await fetch(
                `/grafico/${tipo}?t=${Date.now()}`
            );

            if (!resposta.ok) {
                let detalhe = "Erro ao gerar o gráfico.";

                try {
                    const erro = await resposta.json();

                    if (erro.erro) {
                        detalhe = erro.erro;

                        if (erro.detalhes) {
                            detalhe += " " + erro.detalhes;
                        }
                    }
                } catch (e) {}

                throw new Error(detalhe);
            }

            const blob = await resposta.blob();

            imagem.src = URL.createObjectURL(blob);
            imagem.alt = "Resultado: " + nomes[tipo];
            imagem.hidden = false;

            mensagem.textContent = "Gráfico gerado com sucesso!";

        } catch (erro) {

            mensagem.textContent =
                erro.message ||
                "Não foi possível conectar ao servidor Python.";
        }
    });
});

document.getElementById("fechar").addEventListener("click", () => {
    resultado.hidden = true;
});
