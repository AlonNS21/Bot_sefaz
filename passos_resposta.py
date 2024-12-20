# passos_resposta.py
# Comandos para Passos a passos.

# Boleto BRB
def resposta_boleto_brb():
    # Aqui você define a resposta específica para ativar o credor
    pdf_link = "https://drive.google.com/file/d/103FRmhcU3sHDcsiOJMOGp4RkneuNwm36/view?usp=drive_link"
    resposta = (
        "Boleto de deposito judical BRB.\n\n>"
        
        "lique no link abaixo para fazer boleto de deposto judical do BRB.\n\n"
        
        "Obs.: Esse rotina teve a ultima atualização em 2022.\n\n>"
        
        f"Clique [aqui]({pdf_link}) para ver um exemplo em PDF."
    )
    return resposta

# Pagamento Detran
def resposta_pagamento_detran():
    # Aqui você define a resposta específica para ativar o credor
    pdf_link = "https://drive.google.com/file/d/1oA2FFm-fkcViOrh4auifaEu69rA0VJiS/view?usp=drive_link"
    resposta = (
        "Rotina de pagamento Deran.<b>"
        "Clique no link abaixo para vizualizar a rotina de pagamento restituição detran.\n\n"
        
        "Obs.: Esse rotina teve a ultima atualização em 2022.\n\n"

        f"Clique [aqui]({pdf_link}) para ver um exemplo em PDF."
    )
    return resposta

# Rotina Deposito Judicial.
def resposta_rotina_deposito_judicial():
    # Aqui você define a resposta específica para ativar o credor
    pdf_link = "https://drive.google.com/file/d/1oA2FFm-fkcViOrh4auifaEu69rA0VJiS/view?usp=drive_link"
    resposta = (
        "Passo a passo deposito judical.<b>"
        "Para saber como é a rotina para preparar o pagamento do processo de deposto judical, segue o link abaixo.<b><b>"
        
        "Obs.: Esse rotina teve a ultima atualização em 2022.<b><b>"

        f"Clique [aqui]({pdf_link}) para ver um exemplo em PDF."
    )
    return resposta


def resposta_incluir_nex():
    
    resposta = (    
    """ 
    Incluir NEX: Passo a Passo
    
    Passo 1: Acesse o SEI.
    Passo 2: Escolha uma restituição (ICMS, IPVA, ITD, TAXAS).
    Passo 3: Vá em "Anotações".
    Passo 4: Copie o número da NOB.
    Passo 5: Acesse o Fiplan.
    Passo 6: Vá em "Consultar NEX".
    Passo 7: Insira o exercício (2024).
    Passo 8: Insira o número da NOB.
    Passo 9: Clique em "Consultar".
    Passo 10: Selecione o resultado.
    Passo 11: Se a NEX já estiver efetivada ou não, copie a informação.
    Passo 12: Gere o PDF.
    Passo 13: Envie para o Carlos e anote o número do Fiplan.
    Passo 14: Volte ao SEI.
    Passo 15: Vá em "Incluir Documentos".
    Passo 16: Selecione "Externo".
    Passo 17: Escolha "Nota de Ordem Extra Orçamentária".
    Passo 18: Marque como "Nato-Digital".
    Passo 19: Insira a data (atual).
    Passo 20: Caso necessário, selecione "Público Restrito".
    Passo 21: Inclua o documento.
    Passo 22: Para o Carlos, selecione a opção do número do Fiplan, que estará em "Download" (seta para baixo) ⬇️.
    Passo 23: Clique em "Abrir" após a seleção.
    Passo 24: Siga para o próximo processo.
    """
    )
    return resposta








