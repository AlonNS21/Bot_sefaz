# respostas.py

def resposta_nome():
    return "Meu nome é ChatBot!"

def resposta_como_esta():
    return "Estou funcionando perfeitamente, obrigado por perguntar!"

def resposta_capital_bahia():
    return "A capital da Bahia é Salvador."

def resposta_capital_franca():
    return "A capital da França é Paris."

def resposta_credor_pagamento_fatura():
    pdf_link = "https://drive.google.com/file/d/1yTdpQGjR5--2M_yC3PDal2829CgsoEre/view?usp=drive_link"
    resposta = (
        "Para incluir credor como conta ou pagamento fatura, é necessário enviar um e-mail para a Gerência de Análises e Operações Contabéis (GERAC): gerac@sefaz.ba.gov.br.<br><br>"
        f"Você pode acessar o {pdf_link}"
    )
    return resposta
