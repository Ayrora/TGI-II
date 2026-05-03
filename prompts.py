def prompt_extracao(curriculo):
    return f"""
Extraia os dados do currículo e retorne JSON válido.

Formato:

{{
  "nome": "",
  "anos_experiencia": 0,
  "skills": [],
  "educacao": []
}}

Currículo:
{curriculo}
"""


def prompt_avaliacao(vaga, curriculo_json):
    return f"""
Você é um avaliador de currículos.

Dê notas de 0 a 10.

Retorne SOMENTE JSON:

{{
  "nota_final": 0,
  "skills": 0,
  "experiencia": 0,
  "senioridade": 0,
  "educacao": 0,
  "justificativa": ""
}}

Vaga:
{vaga}

Candidato:
{curriculo_json}
"""