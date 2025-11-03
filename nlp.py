import spacy
import unicodedata
nlp = spacy.load("es_core_news_sm")
def normalizar(texto: str) -> str:
    texto = texto.lower()
    texto = "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) !="Mn")
    return texto

def procesar_texto(texto: str) -> set:
    texto = normalizar(texto)
    doc = nlp(texto)
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return set(tokens)