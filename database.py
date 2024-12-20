# database.py

import sqlite3  # Importa a biblioteca sqlite3 para interagir com o banco de dados SQLite

# Função para conectar ao banco de dados SQLite
def conectar_bd():
    return sqlite3.connect('chatbot.db')  # Retorna uma conexão com o banco de dados chamado 'chatbot.db'

# Função para criar a tabela de conversas no banco de dados, se ainda não existir
def criar_tabela():
    conn = conectar_bd()  # Conecta ao banco de dados
    cursor = conn.cursor()  # Cria um cursor, que é um objeto utilizado para executar comandos SQL
    # Executa um comando SQL para criar a tabela 'conversas' se ela não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS conversas 
                      (usuario TEXT, bot TEXT)''')  # A tabela tem duas colunas: 'usuario' e 'bot', ambas de tipo TEXT
    conn.commit()  # Salva (confirma) as mudanças no banco de dados
    conn.close()  # Fecha a conexão com o banco de dados

# Função para salvar uma conversa (pergunta do usuário e resposta do bot) no banco de dados
def salvar_conversa(usuario, bot):
    conn = conectar_bd()  # Conecta ao banco de dados
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    # Executa um comando SQL para inserir os dados de uma conversa na tabela 'conversas'
    cursor.execute("INSERT INTO conversas (usuario, bot) VALUES (?, ?)", (usuario, bot))  # Insere os valores da conversa (usuario, bot) no banco
    conn.commit()  # Salva (confirma) a inserção dos dados no banco de dados
    conn.close()  # Fecha a conexão com o banco de dados

# Função para encontrar uma resposta do bot baseada no input do usuário
def encontrar_resposta(usuario_input):
    conn = conectar_bd()  # Conecta ao banco de dados
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    # Executa um comando SQL para buscar a resposta do bot onde a entrada do usuário corresponde a 'usuario' na tabela
    cursor.execute("SELECT bot FROM conversas WHERE usuario = ?", (usuario_input,))  # Busca a resposta do bot para a entrada do usuário
    resposta = cursor.fetchone()  # Obtém a primeira linha do resultado da consulta
    conn.close()  # Fecha a conexão com o banco de dados
    return resposta[0] if resposta else None  # Retorna a resposta do bot (primeira coluna), ou None se não houver resposta

# # database.py
# import psycopg2  # Importa a biblioteca psycopg2 para interagir com o banco de dados PostgreSQL

# # Função para conectar ao banco de dados PostgreSQL
# def conectar_bd():
#     # Conecta ao banco de dados com os parâmetros necessários (substitua pelos seus valores)
#     return psycopg2.connect(
#         host="localhost",     # Endereço do servidor do banco de dados
#         database="chatbot",   # Nome do banco de dados
#         user="seu_usuario",   # Seu usuário do banco de dados
#         password="sua_senha"  # Sua senha do banco de dados
#     )

# # Função para criar a tabela de conversas no banco de dados, se ainda não existir
# def criar_tabela():
#     conn = conectar_bd()  # Conecta ao banco de dados
#     cursor = conn.cursor()  # Cria um cursor, que é um objeto utilizado para executar comandos SQL
#     # Executa um comando SQL para criar a tabela 'conversas' se ela não existir
#     cursor.execute('''CREATE TABLE IF NOT EXISTS conversas 
#                       (usuario TEXT, bot TEXT)''')  # A tabela tem duas colunas: 'usuario' e 'bot', ambas de tipo TEXT
#     conn.commit()  # Salva (confirma) as mudanças no banco de dados
#     conn.close()  # Fecha a conexão com o banco de dados

# # Função para salvar uma conversa (pergunta do usuário e resposta do bot) no banco de dados
# def salvar_conversa(usuario, bot):
#     conn = conectar_bd()  # Conecta ao banco de dados
#     cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
#     # Executa um comando SQL para inserir os dados de uma conversa na tabela 'conversas'
#     cursor.execute("INSERT INTO conversas (usuario, bot) VALUES (%s, %s)", (usuario, bot))  # Insere os valores da conversa (usuario, bot) no banco
#     conn.commit()  # Salva (confirma) a inserção dos dados no banco de dados
#     conn.close()  # Fecha a conexão com o banco de dados

# # Função para encontrar uma resposta do bot baseada no input do usuário
# def encontrar_resposta(usuario_input):
#     conn = conectar_bd()  # Conecta ao banco de dados
#     cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
#     # Executa um comando SQL para buscar a resposta do bot onde a entrada do usuário corresponde a 'usuario' na tabela
#     cursor.execute("SELECT bot FROM conversas WHERE usuario = %s", (usuario_input,))  # Busca a resposta do bot para a entrada do usuário
#     resposta = cursor.fetchone()  # Obtém a primeira linha do resultado da consulta
#     conn.close()  # Fecha a conexão com o banco de dados
#     return resposta[0] if resposta else None  # Retorna a resposta do bot (primeira coluna), ou None se não houver resposta
