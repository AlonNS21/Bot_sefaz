# receita_reposta.py
def resposta_receita_integrada():
    # Aqui você define a resposta específica para ativar o credor
    
    resposta = (
        "Receita integrada\n\n"
        "Começa após o pagamento do DAE efetuado pelo contribuinte, o SIGAT recebe essas informações e as trata em seu banco de dados.\n"
        "Em seguida passa por três processo Arrecadação, Repasse, classificada, e Regularização da RSS.\n\n"

        "Arrecadação:\n"
        "Durante a noite, o FIPLAN consome as informações dos DAE’s usando o banco de dados do SIGAT, gerando assim os DAE’s tributários e em seguida os DAE’s orçamentários que são divididos pela a receia, registrando assim a AVR (Aviso de credito).\n\n"

        "OBS: A limitação é de: 45.000 unidades/dia em 3 lotes, 15.000 em cada lote.\n\n"

        "Repasse:\n" 
        "Depois de 2 dias o FIPLAN registra os DAC a partir dos repasses informado no SIGAT.\n\n"

        "Classificada:\n"
        "Gerou a RSS?\n\n"
        "Se sim, irá registrar a RSS, por convênio, que será visualizada em dois dias (D+2), pois o DAC é processado na madrugada.\n"
        "Se não, os documentos não casados ficam na Vala.\n\n"
        "Os documentos na vala serão precisos fazer a Regularização da RSS manual, depois da regularização manual se o DAC for igual a AVR registrará a RSS, caso contrário voltará para a vala, esperando novos registro DAC (Repasses).\n\n"

        "Regularização da RSS:\n\n"
        "A RSS é regularizada automaticamente pelo FIPLAN, mas caso haja algum pendencia terá que fazer a regularização manualmente.\n\n"
        "Regularizar a RSS manualmente no FIPLAN, depois emitir e analisar Relatório FIP 712A (Relatório Financeiro).\n"
        
        "A análise do resultado do relatório FIP712A para não haver pendencias tem que está AVR=DAC=RSS, isto é, AVR-DAC e DAC-RSS zerados!\n\n"
        "Analise do resultado do relatório FIP712A, RSS não gerada (AVR≠DAC), impacta na apuração diária do FUNCEP, pagamento de DAE por outro órgão.\n\n"
    )
    return resposta

def resposta_avr_maior_dac():
    # Aqui você define a resposta específica para ativar o credor
    
    resposta = (
        
    "AVR maior que DAC, com um valor positivo, significa que na coluna AVR-DAC exsite mais AVR do que DAC.\n\n"
    
    "Caso a AVR esteja maior que o DAC isso geralmente tem a ver com o parcelamento.<br>"
    "OBS.: Pois o banco faz o repasse no último dia do mês, GEARC faz controle em planilha Excel e em seguida a GEARC envia a planilha de controle para DEPAT e para o BANCO.\n\n"
    
    "A diferença devida ao parcelamento, processo de repasse das receitas em função do parcelamento, acompanhar durante o mês se o valor será repassado pelo banco no final do mês.\n"
    "OBS 2.: O parcelamento é inicialmente enviado para uma conta especifica, com o controle da GEARC o banco faz as contas especificas de arrecadação.\n\n"
    
    "Caso a diferença não é devido ao parcelamento, informar a GEARC para verificar o problema, em seguida só aguardar a GEARC resolver o problema.\n"
    "OBS 3.: situações: Banco não enviar ou SIGAT não liberar repasse, problemas na integração, etc. O problema será resolvido."
         
    )
    return resposta

def reposta_avr_menor_dac():
    # Aqui você define a resposta específica para ativar o credor
    
    resposta = (
    
    "AVR menor que o DAC, signfica que que na coluna AVR-DAC o valor estará negativo, tendo mais DAC que AVR.\n\n"
    
   "Quando a AVR está menor que o DAC isso pode a ver inúmeros problemas, vou explicar;\n\n"
   " 1 - DAEs não processados, o sistema não conseguiu processá-los por algum motivo, podendo assim forçar um processamento, no caso processá-los manualmente.\n"
    "2 - Credor não cadastrado, os credores são as pessoas que pagaram o DAE, e assim terá que cadastra-los no banco de dados do FIPLAN, para assim o problema desaparecer, esse procedimento é feito pela COEFI.\n"
    "3 - Natureza da Receita não cadastrada (NR), para solucionar, basta Solicitar a GERAC o cadastro da Natureza da Receita assim a GERAC aciona a SEPLAN para realizar o cadastro. Em caso de apenas parametrização da Natureza da Receita no FIPLAN, a GERAC resolve.\n"
    "4 - Código de tributo não cadastrado, terá que solicitar a GERAC castro do código do tributo, a GERAC aciona a SAT/DARC para realizar o cadastro.\n"
    "5 – Outros casos: Informar para GERAC verificar o problema, que pode ser pendencia de processamento de arrecadação no SIGAT ou na PRODEB, envio no arquivo pelo banco, etc.\n"
    "Cadastro de credor realizado, Natureza da receita cadastrada ou apenas parametrizada, código do tributo cadastrada pela DARC ou pedir para GERAC verificar se a problema no processamento da arrecadação no SIGAT ou PRODEB.\n"
    "Aguardar o sistema processar AVR/DAC na rotina automática.\n"
    "6 - DAEs represados Solicitar a GDSAF carga extra de obtenção e processamento de DAE.\n"
    "OBS.: Esse processo acontece durante o dia.\n\n"
    
    "A SEFAZ/ DEPAT solicita abrir o ticket para a PRODEB realizar   processamento, caso processamento finalizado, informar a SAFAZ/ DEPAT.\n\n" 
    "O processamento é finalizado após 17h aguardar o sistema processar AVR/DAC na rotina automática, processamento finalizado até início da tarde.\n\n"
    "Depois é só processar o DAE manualmente, processar AVR manualmente e Processar Regularização de RSS manualmente.<br>" 
    "AVR processada?  RSS regularizada (até a data analisada).\n"
    "AVR não processada? Aguardar o sistema processar AVR/DAC na rotina automática, no dia seguinte emitir o relatório FIP712A (Financeiro), verificar se AVR=DAC=RSS.\n\n"
    "Caso a AVR esteja menor que o DAC, reportar problema para GERAC/GEARC/GDSAF e aguardar retorno dos setores responsáveis.\n"
    "OBS: Problema na integração, doc de arrecadação não apropriado pelo SIGAT, receita sem código cadastrado.\n\n"  
    "Problema resolvido!"

    )
    return resposta


def resposta_fechamento_receita_integrada():
    # Aqui você define a resposta específica para ativar o credor
    resposta = (
    
    "Emitir relatório FIP712(contábil)\n\n>"
    
    "No final do mês conforme se o valor do parcelamento foi repassado, emitir relatório FIP712A (Financeiro) do mês. Para confirmar se AVR=DAC=RSS no mês, indicando que a RSS foi regularizada com sucesso e que não à pendencia no mês.\n" 
    "Emitir relatório FIP712 (Contábil), caso a RSS não gerada dando indicio que a AVR está diferente do DAC (AVR≠DAC), é possível efetuar a correção dentro do mês.<br>" 
    "Emitir relatório FIP712(contábil)\n\n"
    "AVR=DAC=RSS, RSS regularizada no automaticamente do mês pelo FIPLAN (Contábil)\n"
    "-FIM!\n\n"
    
    "RSS não gerada (AVR=DAC≠RSS), emitir relatório consulta AVR c/ indicativo de RSS – Não.\n"
    "OBS: Verificar se há AVR/DAC sem RSS de mês anterior.\n\n" 
    "Regularizar RSS nas datas de arrecadação correspondente às AVR do relatório.\n"
    "Emitir novamente do FIP712A (contábil).\n"
    "OBS: O mês pode ser fechado com diferença no relatório em caso de algum problema não resolvido.\n\n" 
    "Mapear as diferenças encontradas para ajuste/correções no mês seguinte.\n"
    "RSS regularizada no fechamento do mês no FIPLAN.\n"
    "-FIM!"

    )
    return resposta

def reposta_avr():
    # Aqui você define a resposta específica para ativar o credor
    
    resposta = (
    
    "AVR é um aviso de Cerdito, faz parte da arrecadação.\n\n"
    
    "Ainda sera incluido mais informações."
    )
    return resposta


def resposta_dac():
    # Aqui você define a resposta específica para ativar o credor
    resposta = (
    
    "DAC é o documento de aviso de credtito, faz parte dp repasse.\n\n"
    
    "Ainda sera incluido mais informações."

        
    )
    return resposta

def resposta_rss():
    # Aqui você define a resposta específica para ativar o credor
    resposta = (
    
    "Sem informções no momento."
    
    )
    return resposta

def resposta_avr_dac_rss():
    # Aqui você define a resposta específica para ativar o credor
    resposta = (
    
    "Se AVR-DAC e DAC-RSS estivem zeradas(0), significa que não a pendência para ser resolvidas."
    
    )
    return resposta


def resposta_dac_rss_negativa():
    # Aqui você define a resposta específica para ativar o credor
    resposta = (
    
    "Sempre vai ser um valor positivo indicando que a AVR-DAC esta com pendências, assim pendendo esse valor, ou zerado indicando que não tem pendências.\n\n"
    
    "O DAC-RSS não deve acontecer nunca!\n"
    "A RSS é o prduto do AVR e do DAC, se DAC-RSS é negativo, está dizendo que ele vai gerar a RSS sem ter DAC, um fato praticamente impossivel."
     
    )
    return resposta


def resposta_avr_zerada():
    # Aqui você define a resposta específica para ativar o credor
    
    resposta = (
    
    "AVR zerada indica que não holve arrecadação.\n\n"
    
    "Outro suposto indicativo:\n"
    "Se for do convenio 0001 (ICMS) pode ser por causa do SIMPLES NACIONAL.\n"
    "Aparentimente é normal, pois a informação so chega 2 dias depois.\n"

    )
    return resposta


def resposta_dac_zerada():
    # Aqui você define a resposta específica para ativar o credor
    
    resposta = (
    
    "Se o DAC estiver zerado, significa que Moreno não lançou o repasse, ou pode ser que o FIPLAN não conseguiu processar.\n"
    "Dai tem que avaliar se seria algum problema na integração.\n\n"
    
    "Assim como o DAC não ter AVR, também pode ser por problema de integração.\n\n"
    
    "Tem que acompanhar e avaliar!"
    
    )
    return resposta


def resposta_rss_zerada():
    # Aqui você define a resposta específica para ativar o credor
    resposta = (
    
    "RSS zerada(0), significa que não holve o 'Casamento' da AVR e DAC ou DAC e AVR.\n\n"
    
    "Outro suposto indicativo:\n"
    "Se for do convenio 0001 (ICMS) pode ser por causa do SIMPLES NACIONAL.\n"
    "Aparentimente é normal, pois a informação so chega 2 dias depois.\n"

    )
    return resposta