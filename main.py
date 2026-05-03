from llm import LLM
from prompts import prompt_extracao, prompt_avaliacao
from embeddings import calcular_similaridade
from data import vaga, curriculos

llm = LLM()

def processar_curriculo(texto):
    prompt = prompt_extracao(texto)
    return llm.generate(prompt)

def avaliar(curriculo_texto, curriculo_json):
    prompt = prompt_avaliacao(vaga, curriculo_json)
    avaliacao = llm.generate(prompt)

    similaridade = calcular_similaridade(curriculo_texto, vaga)

    nota_llm = avaliacao.get("nota_final", 0)

    nota_final = (nota_llm * 0.7) + (similaridade * 10 * 0.3)

    return {
        "nota_llm": nota_llm,
        "similaridade": round(similaridade, 3),
        "nota_final": round(nota_final, 2),
        "justificativa": avaliacao.get("justificativa", "")
    }

def main():
    resultados = []

    for i, curriculo in enumerate(curriculos):
        print(f"\n===== Candidato {i+1} =====\n")

        try:
            curriculo_json = processar_curriculo(curriculo)
            resultado = avaliar(curriculo, curriculo_json)

            print(resultado)
            resultados.append(resultado)

        except Exception as e:
            print("Erro:", e)

    print("\n===== RANKING =====\n")

    ranking = sorted(resultados, key=lambda x: x["nota_final"], reverse=True)

    for i, r in enumerate(ranking):
        print(f"{i+1}º lugar → Nota {r['nota_final']}")

if __name__ == "__main__":
    main()