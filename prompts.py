def prompt_extracao(curriculo):

    return f"""
Você é um sistema de extração de currículos.

Extraia as informações do currículo
e retorne SOMENTE JSON válido.

NÃO explique nada.
NÃO escreva texto adicional.
NÃO use markdown.

Formato obrigatório:

{{
  "nome": "",
  "anos_experiencia": 0,
  "skills": [],
  "educacao": []
}}

Regras:
- skills deve ser lista
- educacao deve ser lista
- anos_experiencia deve ser número inteiro

Currículo:
{curriculo}
"""


def prompt_avaliacao(vaga, curriculo_json):

    return f"""
Você é um recrutador técnico especialista.

Avalie o candidato comparando
com a vaga.

Retorne SOMENTE JSON válido.

Formato obrigatório:

{{
  "nota_final": 0,
  "skills": 0,
  "experiencia": 0,
  "senioridade": 0,
  "educacao": 0,
  "justificativa": ""
}}

Regras:
- notas entre 0 e 10
- justificativa curta
- não escreva fora do JSON

Vaga:
{vaga}

Candidato:
{curriculo_json}
"""
