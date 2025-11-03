import gradio as gr
from bot import buscar_respuesta

def responder(mensaje, historial):
    respuesta = buscar_respuesta(mensaje)
    historial.append([mensaje, respuesta])
    return "", historial

with gr.Blocks() as demo:
    gr.Markdown("## Chatbot SoftDev")
    chatbot = gr.Chatbot(
        label="Historial de conversación",
        value = [["","Hola, soy el chatbot de SoftDev. ¿En qué puedo ayudarle?"]]
    )

    msg = gr.Textbox(placeholder="Escribe tu mensaje aquí...")
    clear = gr.Button("Limpiar historial")

    msg.submit(responder, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: [], None, chatbot)

if __name__ == "__main__":
    demo.launch()