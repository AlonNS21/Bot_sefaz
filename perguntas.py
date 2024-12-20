def carregar_perguntas():
    """Retorna uma lista de perguntas associadas com suas funções de respostas"""
    # from respostas import resposta_nome, resposta_como_esta, resposta_capital_bahia, resposta_capital_franca, resposta_credor_pagamento_fatura
    # Receita
    from receita_reposta import resposta_receita_integrada, resposta_avr_maior_dac, reposta_avr_menor_dac, resposta_fechamento_receita_integrada, reposta_avr, resposta_dac, resposta_rss, resposta_avr_dac_rss, resposta_dac_rss_negativa, resposta_avr_zerada, resposta_dac_zerada, resposta_rss_zerada
    from receita_perguntas import pergunta_receita_integrada, pergunta_avr_maior_dac, pergunta_avr_menor_dac, pergunta_fechamento_receita_integrada, pergunta_avr, pergunta_dac, pergunta_rss, pergunta_avr_dac_rss, pergunta_dac_rss_negativa, pergunta_avr_zerada, pergunta_dac_zerada, pergunta_rss_zerada
    # E-mail
    from email_resposta import resposta_ativar_credor, resposta_concluir_processo_aj, resposta_credor_pagamento_fatura, reposta_pagamento_nao_efetivado, resposta_inativar_conta_bancaria, resposta_fale_consco_rest, resposta_reset_senha_rede, resposta_cadastro_agencia_bancaria
    from email_pergunta import pergunta_ativar_credor, pergunta_concluir_processo_aj, pergunta_credor_pagamento_fatura, pagamento_nao_efetivado, pergunta_inativar_conta_bancaria, pergunta_fale_consco_rest, pergunta_reset_senha_rede, pergunta_cadastro_agencia_bancaria
    # Comandos para bancos
    from coman_bancos_resposta import resposta_bb_pupanca, resposta_cef_pupanca
    from coman_bancos_pergunta import pergunta_bb_pupanca, pergunta_cef_pupanca
    # Passo a passo 
    from passos_resposta import resposta_boleto_brb, resposta_pagamento_detran, resposta_rotina_deposito_judicial, resposta_incluir_nex
    from passos_pergunta import pergunta_boleto_brb, pergunta_pagamento_detran, pergunta_rotina_deposito_judicial, pergunta_incluir_nex
    # Lista telefone / Ramal.
    from ramal_resposta import resposta_ramal_telefone
    from ramal_pergunta import pergunta_ramal_telefone
    # BRB
    from brb_resposta import resposta_dae_brb, resposta_deveolver_alvara, resposta_email_brb, resposta_rotina_brb
    from brb_pergunta import pergunta_dae_brb, pergunta_deveolver_alvara, pergunta_email_brb, pergunta_rotina_brb
    # Fiplan 
    from fiplan_resposta import resposta_credor, resposta_dr, resposta_nex, resposta_nob, resposta_noe, resposta_numero_credor, resposta_numero_documento, resposta_ped, resposta_sistema_fiplan, resposta_unidade_getora_executora
    from fiplan_pergunta import pergunta_credor, pergunta_dr, pergunta_nex, pergunta_nob, pergunta_noe, pergunta_numero_credor, pergunta_numero_documento, pergunta_ped, pergunta_sistema_fiplan, pergunta_unidade_getora_executora
    
    


    return [
        
        # Receita
        (pergunta_receita_integrada(), resposta_receita_integrada),
        (pergunta_avr_maior_dac(), resposta_avr_maior_dac),
        (pergunta_avr_menor_dac(), reposta_avr_menor_dac),
        (pergunta_fechamento_receita_integrada(), resposta_fechamento_receita_integrada),
        (pergunta_avr(), reposta_avr),
        (pergunta_dac(), resposta_dac),
        (pergunta_rss(), resposta_rss),
        (pergunta_avr_dac_rss(), resposta_avr_dac_rss),
        (pergunta_dac_rss_negativa(), resposta_dac_rss_negativa),
        (pergunta_avr_zerada(), resposta_avr_zerada),
        (pergunta_dac_zerada(), resposta_dac_zerada),
        (pergunta_rss_zerada(), resposta_rss_zerada),
        # E-mail
        (pergunta_ativar_credor(), resposta_ativar_credor),
        (pergunta_concluir_processo_aj(), resposta_concluir_processo_aj),
        (pergunta_credor_pagamento_fatura(), resposta_credor_pagamento_fatura),
        (pagamento_nao_efetivado(), reposta_pagamento_nao_efetivado),
        (pergunta_inativar_conta_bancaria(), resposta_inativar_conta_bancaria),
        (pergunta_fale_consco_rest(), resposta_fale_consco_rest),
        (pergunta_reset_senha_rede(), resposta_reset_senha_rede),
        (pergunta_cadastro_agencia_bancaria(), resposta_cadastro_agencia_bancaria),
        # Comandos para bancos
        (pergunta_bb_pupanca(), resposta_bb_pupanca),
        (pergunta_cef_pupanca(), resposta_cef_pupanca),
        # Passo a passo 
        (pergunta_boleto_brb(), resposta_boleto_brb),
        (pergunta_pagamento_detran(), resposta_pagamento_detran),
        (pergunta_rotina_deposito_judicial(), resposta_rotina_deposito_judicial),
        (pergunta_incluir_nex(), resposta_incluir_nex),
        
        # Lista telefone / Ramal.
        (pergunta_ramal_telefone(),resposta_ramal_telefone),
        # BRB
        (pergunta_deveolver_alvara(), resposta_deveolver_alvara),
        (pergunta_dae_brb(), resposta_dae_brb),
        (pergunta_rotina_brb(), resposta_rotina_brb),
        (pergunta_email_brb(), resposta_email_brb),
        # Fiplan
        (pergunta_credor(), resposta_credor),
        (pergunta_dr(), resposta_dr),
        (pergunta_nex(), resposta_nex),
        (pergunta_nob(), resposta_nob),
        (pergunta_noe(), resposta_noe),
        (pergunta_numero_documento(), resposta_numero_documento),
        (pergunta_ped(), resposta_ped),
        (pergunta_sistema_fiplan(), resposta_sistema_fiplan),
        (pergunta_unidade_getora_executora(), resposta_unidade_getora_executora),
        (pergunta_numero_credor(), resposta_numero_credor),
        # ((), ),
        # ((), ),
        # ((), ),
        # ((), ),
        # ((), ),
        # ((), ),
        # ((), ),
        
         # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        # ((),),
        
        
    
        # Nova pergunta associada à função de resposta
    ]
