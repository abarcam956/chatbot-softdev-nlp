from nlp import procesar_texto
def jaccard(a: str, b: str) -> float:
   """Similitud de Jaccard entre dos frases."""
   A, B = procesar_texto(a), procesar_texto(b)
   if not A or not B:
     return 0.0
   return len(A & B) / len(A | B)