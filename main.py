# main.py

from perguntas import carregar_perguntas

def obter_resposta(pergunta_usuario):
    # Carrega as perguntas e respostas
    perguntas_respostas = carregar_perguntas()

    # Verifica se a pergunta do usuário tem correspondência
    for pergunta, resposta_func in perguntas_respostas:
        if pergunta_usuario.lower() == pergunta.lower():  # Ignora maiúsculas/minúsculas
            return resposta_func()  # Executa a função de resposta correspondente

    return "Desculpe, não entendi sua pergunta."

# Teste com a nova pergunta
pergunta = "como incluir credor no pagamento fatura"
resposta = obter_resposta(pergunta)
print(resposta)
