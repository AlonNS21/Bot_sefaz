# fiplan_resposta.py
def resposta_sistema_fiplan():
    resposta = ( 
            
    "Fiplan significa Sistema Integrado de Planejamento, o sistema tem foco na área de Contabilidade e Finanças do Estado da Bahia.\n\n"
    
    "Fiplan é um sistema compartilhado entre as Secretarias da Fazenda (Sefaz) e do Planejamento (Seplan), cujo objetivo é o aperfeiçoamento dos registros dos processos de planejamento, contabilidade, execução orçamentária, financeira e patrimonial da Administração Pública do Estado da Bahia.\n\n"
    
    "O Fiplan integra em uma única ferramenta, via web, os sistemas antes utilizados para gerir o planejamento, a execução orçamentária e a prestação de contas do Estado da Bahia, contribuindo para a melhoria da qualidade da informação nestas áreas de atuação governamental."
     
    )
    return resposta
    
def resposta_credor():
    resposta = (
    "São considerados credores as pessoas físicas ou jurídicas que constam nos documentos orçamentários e financeiros como favorecidos de obrigações contraídas pelas unidades gestoras."
    )
    return resposta
    
    
def resposta_numero_credor():
    resposta = (
    
    "Para cada credor incluído é gerado automaticamente pelo sistema o código que o identifique. Esse código é formado por 10 dígitos, sendo um sequencial por exercício.\n\n"
    
    """
    Exercício: 2024.
    Sequecial: 00035
    DV: -1 \n\n
    
    Formando assim o numero do credor: 2024.00035-1
    """
    )
    return resposta
    
    
def resposta_ped():
    resposta = (
        
    "Descrição do Pedido de Empenho - PED<b><b>"
    
    "Pedido de Empenho da Despesa é o estágio que precede o Empenho da Despesa – EMP. A UG deverá certificar se da existência de saldo suficiente na dotação específica, uma vez que é condição indispensável para sua inclusão.<b><b>"
    
    "Cancelamento da Autorização do PED<b><b>"
    
    "O servidor com perfil de ordenador de despesas para a Unidade Gestora Executora poderá realizar o cancelamento da autorização do PED.<b><b>"
    
    "Após o cancelamento da autorização do PED, o documento gerado voltará para a situação de Não Autorizado e poderá ser alterado ou estornado.<b><b>"
    
    )
    return resposta
    
def resposta_nob():
    resposta = (
       
    "A NOB é o instrumento que figura a transferência de recursos financeiros do Estado para a conta do credor, comprovando a quitação de uma obrigação.\n\n"  
        
    "Descrição\n\n"
    
    "A Nota de Ordem Bancária é o último estágio do processo de execução da despesa e caracteriza-se pela emissão do documento Nota de Ordem Bancária – NOB.\n\n"
    
    "A NOB é o instrumento que efetua a transferência de recursos financeiros do Estado para a conta do credor, comprovando a quitação de uma obrigação.\n\n"
    
    "Condições.\n\n"
    
    "- Pagamento Liberado por meio da Funcionalidade LIB.\n\n"
    
    "- Para liquidações cuja forma de recebimento do credor ou consignatárias tenha sido definida como pagamento por fatura, esta já deverá estar detalhada.\n\n"
    
    "Funcionalidades.\n\n"
    
    "Incluir - Consultar - Autorizar Estorno - Estornar - Emitir NOB Geradas.\n\n"
    
    "Estorno da NOB.\n\n"
    
    "Não há estorno parcial de NOB. O estorno, quando possível, será realizado pelo valor total.\n\n"
    "Só será permitido estorno de NOB nas seguintes situações:.<b>"
    "- NOB com situação igual a Normal e que não foi transmitida ou NOB de regularização."
    

    )
    return resposta
    

def resposta_noe():
    # Aqui você define a resposta específica para ativar o credor
    pdf_link = ""
    resposta = (
        
     "A NOE é uma funcionalidade do Fiplan que permite o pagamento extraorçamentário. A NOE funciona para o pagamento extraorçamentário de forma análoga à liquidação para os pagamentos orçamentários.<b><b>"
        
    "Descrição<b><b>"
    
    "É a funcionalidade por meio da qual o pagamento extraorçamentário se inicia. A função da NOE no Fiplan é registrar as informações relativas aos dados bancários de recebimento do credor.<b><b>"
    
    "A Solicitação de Pagamento Extraorçamentário – NOE é uma funcionalidade do Fiplan que permite o pagamento de dispêndios extraorçamentários. A NOE funciona para o pagamento extraorçamentário de forma análoga à liquidação. A NOE não gera lançamentos contábeis, estes só serão realizados na geração da NEX.<b><b>"
    
    "Condições.<b><b>"
    
    "Para NOE cuja forma de recebimento do credor ou consignatárias tenha sido definida como pagamento por fatura, esta já deverá estar detalhada.<b><b>"
       
    "Funcionalidades.<b><b>"
    
    "Incluir - Alterar - Consultar - Cancelar -Detalhar fatura/Código de Barra<b><b>"
    
    "Dados.<b><b>"
    
    "As contas bancárias de origem de recurso serão disponibilizadas no sistema em função da fonte de recurso selecionada.<b><b>"
    "Depois de incluídas as NOE, essas precisam ser liberadas na funcionalidade Liberação de Pagamentos – LIB. As solicitações podem ser alteradas mesmo depois de liberadas. Somente as NOE liberadas são exibidas para a geração de NEX.<b><b>"
    "Só poderá ser alterada a data do vencimento da NOE dentro do exercício financeiro.<b><b>"
    
    "Existem vários tipos de pagamento extraorçamentário:<b><b>"
    
    
    """
    Registro/Devolução de Depósito Recebido;
    Concessão/Devolução de Depósito Concedido;
    Aporte ao Fundeb; 
    Registro/Devolução de Depósito de Leilão; 
    Pagamento de Restos a Pagar; 
    Contribuições Fiscais e Sociais a Recuperar; 
    Registro Patrimonial de Receita de Convênio; 
    Pagamento Centralizado da Folha; 
    Valores a Pagar por NEX.<b><b>
    """
    
    "Conforme o tipo de pagamento extraorçamentário selecionado, o sistema habilita o(s) fato(s) extraorçamentário(os). Tem-se por exemplo:<b><b>"
    "1 - Para o tipo de pagamento extraorçamentáio Pagamento de Restos a Pagar, o sistema habilita os fatos extraorçamentários Restos a Pagar Processados e Restos a Pagar não Processados Liquidados;<b>"
    
    "2 - Para o tipo de pagamento extraorçamentáio Pagamento Centralizado da Folha, o sistema habilita o fato extraorçamentário Pagamentos da Folha - Centralização no Tesouro.<b><b>"
    
    "A NOE pode ser eletrônica ou de regularização.<b><b>"
    
    "Para a NOE com indicativo de Documento de Regularização igual a NÃO, o Fiplan definirá o indicativo de transmissão como sendo Documento eletrônico. Para a NOE com indicativo de Documento de Regularização igual a SIM, o Fiplan definirá o indicativo de transmissão como sendo Documento de Regularização.<b><b>"
    
    "Outro indicativo que o Fiplan verifica é o de transmissão do pagamento sinalizado na NOE. Caso o indicativo seja Documento Eletrônico, a NEX assumirá o status de Pagamento não transmitido, para posterior transmissão eletrônica. Caso na NOE esteja indicado como documento de regularização, o Fiplan manterá o indicativo de situação da transmissão eletrônica em branco, pois os referidos indicativos de transmissão tratam de pagamentos que não devem ser transmitidos eletronicamente.<b><b>"
    
    "As NOE podem apresentar as seguintes situações no sistema: NOE Normal, NOE cancelada e NOE cancelada por NEX.<b><b>"
    
    "As consignações serão possíveis para os pagamentos extraorçamentários cujo tipo de fato extraorçamentário possua indicativo de consignação. Quando é selecionado um fato extraorçamentário que possua indicativo de consignação, o sistema permite adição das consignatárias."
    
    
        # f"Clique [aqui]({pdf_link}) para ver como fazer o canselamento \ desaltorizção da PED."
    )
    return resposta
    
    

def resposta_nex():
    # Aqui você define a resposta específica para ativar o credor
    resposta = (

    "A NEX tem a finalidade de incluir o pagamento extraorçamentário que foi solicitado por meio da NOE, para posterior geração de ordem bancária. Efetivamente os pagamentos extraorçamentários serão concretizados na confirmação da NEX.\n\n"

    "Descrição\n\n"
    
    "Esta funcionalidade destina-se à emissão das Notas de Ordem Bancária Extraorçamentárias – NEX utilizadas para pagamento extraorçamentário. A NEX é o instrumento que figura a transferência de recursos para a conta do credor. Nesta funcionalidade haverá lançamentos contábeis.\n\n"
    
    "Condições.\n\n"
    
    "Para a geração da NEX, é necessário que exista disponibilidade de recurso financeiro na Unidade Gestora e na fonte de recurso escolhida (DR). A disponibilidade é concretizada por meio de Autorização de Repasse da Receita – ARR.\n\n"
    
    "Só poderá ser realizada NEX das NOE geradas quando as solicitações estiverem liberadas por meio da funcionalidade Liberar Pagamento – LIB.\n\n"
       
    "Funcionalidades.\n\n"
    
    "Incluir - Consultar - Estornar - Autorizar estorno - Emitir NEX geradas\n\n"
    
    "Dados.\n\n"
    
    "A data de pagamento da NEX corresponde à data de vencimento da NOE. É gerada uma NEX para o principal da NOE, líquido do credor, e uma NEX para cada consignatária. Na geração da NEX não é verificado se existe pendência com inadimplência, caso o credor seja contribuinte do Estado.\n\n"
    
    "Quando se tratar de devolução de depósito, deve haver a concessão de depósito por meio de Registro da Receita Extraorçamentária - RDE. Será gerada uma NEX para o principal da NOE, líquido do credor, e uma NEX para cada consignatária, quando houver.\n\n"
    
    "Transmissão de Pagamento\n\n"
    
    "A situação da transmissão do pagamento pode ser visualizada por meio de relatórios, nos quais consulta-se pagamentos transmitidos e inconsistências, pagamentos retornados pelo banco, pagamentos transmitidos sem retorno.\n\n"
    
    
    "Para tratar as situações em que a NEX não tenha sido transmitida e o pagamento não tenha sido efetivado, consultar a Orientação Técnica 056/2016."    
    
    )
    return resposta
    

def resposta_numero_documento():
    # Aqui você define a resposta específica para ativar o credor
    
    resposta = (
        
    "Descrição<b><b>"
    
    "Em geral, cada transação quando executada gera um número de documento, o qual é composto dos itens a seguir:\n\n"
    
    """
    UO: 12345
    UG: 1234
    Execício: 19
    N° Documento: 1234567
    DV: - 1
    \n
    Exemplo: 13101 0001 19 0000001 - 1
    \n\n"""
    "Obs: O item “número do documento” é um sequencial por transação."
 
    
        # f"Clique [aqui]({pdf_link}) para ver como fazer o canselamento \ desaltorizção da PED."
    )
    return resposta
    
    

def resposta_unidade_getora_executora():
    # Aqui você define a resposta específica para ativar o credor
    pdf_link = ""
    resposta = (
        
    "Descrição\n\n"
    
    "Unidade Gestora Executora (UG 0001 a 9999)\n\n"
   
    "Unidade em que é realizada a execução da despesa. Toda unidade orçamentária terá sua UG Centralizadora (UG 0000) e a UG Executora 0001 que a representa."
 
    
    )
    return resposta


# Obs.: Problema ao chamar a função 
def resposta_dr():
    # Aqui você define a resposta específica para ativar o credor, não sabe o motivo.
    resposta = (
        
    "Destinação de Recursos – DR\n\n"
    
    "é o processo pelo qual os recursos públicos são correlacionados a uma aplicação desde a previsão da receita até a efetiva utilização dos recursos, com o objetivo de identificar as fontes de financiamento dos gastos públicos.\n\n"

    
    "O controle das disponibilidades financeiras por DR será feito desde a elaboração do orçamento até a sua execução, incluindo o ingresso, o comprometimento e a saída dos recursos orçamentários.\n\n"
    
    "Art. 8º [...] Parágrafo único. Os recursos legalmente vinculados a finalidade específica serão utilizados exclusivamente para atender ao objeto de sua vinculação, ainda que em exercício diverso daquele em que ocorrer o ingresso.” “Art. 50. Além de obedecer às demais normas de contabilidade pública, a escrituração das contas públicas observará as seguintes: I – a disponibilidade de caixa constará de registro próprio, de modo que os recursos vinculados a órgão, fundo ou despesa obrigatória fiquem identificados e escriturados de forma individualizada;\n\n"
    
    "Composição da Destinação de Recursos:\n\n"
       
    "1º Dígito = Identificador de Uso (IDUSO): utilizado para indicar se os recursos se destinam à contrapartida. Por meio do IDUSO, serão identificados, dentre os recursos destinados a contrapartida, quais serão destinados à contrapartida de convênios, operações de crédito e outras contrapartidas.\n\n"
    
    "2º Dígito = Grupo: segrega os recursos em originários do Tesouro e Outras Fontes, identificando o exercício em que foram arrecadados (corrente ou anterior). Identifica também os recursos condicionados, ou seja, aqueles incluídos na previsão da receita orçamentária, mas que dependem de legislação ou outra condição para integralização dos recursos. Quando confirmadas tais proposições, os recursos são remanejados para as destinações correspondentes e só então poderão ser executados por meio da receita e da despesa.\n\n"
    
    "3º e 4º Dígito = Especificação: individualiza a destinação, sendo a parte mais significativa da classificação. No Fiplan, o Grupo e Especificação serão cadastrados na tabela de Fonte de Recurso.\n\n>"
    
    "5º ao 10º Dígito = Detalhamento: representa o maior nível de particularização da destinação de recursos. No Fiplan, o detalhamento será cadastrado na tabela de Subfonte. A subfonte será utilizada, na 1ª fase do Fiplan, para controlar os convênios recebidos/captados e operações de crédito, sendo gerada uma subfonte para cada convênio e operação de crédito."    
    
        # f"Clique [aqui]({pdf_link}) para ver como fazer o canselamento \ desaltorizção da PED."
    )

    return resposta