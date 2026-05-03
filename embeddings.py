from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def calcular_similaridade(texto1, texto2):
    emb1 = model.encode(texto1)
    emb2 = model.encode(texto2)

    return util.cos_sim(emb1, emb2).item()