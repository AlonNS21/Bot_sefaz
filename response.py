# response.py

from database import encontrar_resposta, salvar_conversa
from faq import obter_resposta  # Importa a função para obter resposta do faq

# Função para processar a mensagem do usuário


def processar_mensagem(mensagem):
    # Primeiro tenta encontrar uma resposta no banco de dados
    resposta = encontrar_resposta(mensagem)

    if resposta:
        return resposta
    else:
        # Se não encontrar, tenta obter resposta do faq
        return obter_resposta(mensagem)

# Função para salvar a conversa


def registrar_conversa(usuario, bot):
    salvar_conversa(usuario, bot)
