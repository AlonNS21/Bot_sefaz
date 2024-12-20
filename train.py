# train.py

from database import salvar_conversa  # Importa a função salvar_conversa do módulo database

# Função para adicionar uma conversa ao banco de dados
def adicionar_conversa(usuario_input, bot_response):
    # Chama a função salvar_conversa passando o input do usuário e a resposta do bot como parâmetros
    salvar_conversa(usuario_input, bot_response)
