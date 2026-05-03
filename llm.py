import requests
import json
import re

class LLM:
    def __init__(self, model="mistral"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": "Responda sempre em JSON válido, sem texto fora do JSON.",
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        if response.status_code != 200:
            raise Exception(f"Erro no Ollama: {response.text}")

        texto = response.json()["response"]

        texto_limpo = self._extrair_json(texto)

        try:
            return json.loads(texto_limpo)
        except Exception as e:
            print("⚠️ Erro ao parsear JSON:")
            print(texto)
            return {
                "nota_final": 0,
                "erro": True,
                "raw": texto
            }

    def _extrair_json(self, texto):
        match = re.search(r"\{.*\}", texto, re.DOTALL)
        if match:
            return match.group(0)
        return texto