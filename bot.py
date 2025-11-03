from respuestas import FAQ
from utils import jaccard

def buscar_respuesta(pregunta: str) -> str:
   mejor_score = 0.0
   mejor_respuesta = "Lo siento, no tengo respuesta para eso."
   for faq, resp in FAQ:
    score = jaccard(pregunta, faq)
     
    if score > mejor_score:  
       mejor_score = score
       mejor_respuesta = resp
   return mejor_respuesta