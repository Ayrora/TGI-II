from llm import LLM
from prompts import prompt_extracao, prompt_avaliacao
from embeddings import calcular_similaridade
from data import vaga, curriculos

llm = LLM()


def processar_curriculo(texto):

    prompt = prompt_extracao(texto)

    return llm.generate(prompt)


def avaliar(curriculo_texto, curriculo_json):

    prompt = prompt_avaliacao(
        vaga,
        curriculo_json
    )

    avaliacao = llm.generate(prompt)

    similaridade = calcular_similaridade(
        curriculo_texto,
        vaga
    )

    nota_llm = avaliacao.get(
        "nota_final",
        0
    )

    nota_final = (
        nota_llm
    )

    return {

        # =========================
        # DADOS DO CANDIDATO
        # =========================

        "nome": curriculo_json.get(
            "nome",
            "Nome não encontrado"
        ),

        "anos_experiencia": curriculo_json.get(
            "anos_experiencia",
            0
        ),

        "skills_extraidas": curriculo_json.get(
            "skills",
            []
        ),

        "educacao": curriculo_json.get(
            "educacao",
            []
        ),

        # =========================
        # NOTAS
        # =========================

        "nota_llm": nota_llm,

        "similaridade": round(
            similaridade,
            3
        ),

        "nota_final": round(
            nota_final,
            2
        ),

        # =========================
        # JUSTIFICATIVA
        # =========================

        "justificativa": avaliacao.get(
            "justificativa",
            ""
        )
    }


def main():

    resultados = []

    for i, curriculo in enumerate(curriculos):

        print(f"\n===== Candidato {i+1} =====\n")

        try:

            # =========================
            # EXTRAÇÃO
            # =========================

            curriculo_json = processar_curriculo(
                curriculo
            )

            print("JSON EXTRAÍDO:")
            print(curriculo_json)

            # =========================
            # AVALIAÇÃO
            # =========================

            resultado = avaliar(
                curriculo,
                curriculo_json
            )

            print("\nRESULTADO:")
            print(resultado)

            resultados.append(resultado)

        except Exception as e:

            print("Erro:", e)

    # =========================
    # RANKING FINAL
    # =========================

    print("\n===== RANKING =====\n")

    ranking = sorted(
        resultados,
        key=lambda x: x["nota_final"],
        reverse=True
    )

    for i, r in enumerate(ranking):

        print(
            f"{i+1}º lugar → "
            f"{r['nome']} "
            f"(Nota {r['nota_final']})"
        )

        print(
            f"   Similaridade: "
            f"{r['similaridade']}"
        )

        print(
            f"   Nota LLM: "
            f"{r['nota_llm']}"
        )

        print(
            f"   Skills: "
            f"{', '.join(r['skills_extraidas'])}"
        )

        print(
            f"   Justificativa: "
            f"{r['justificativa']}"
        )

        print()


if __name__ == "__main__":
    main()
