# -*- coding: cp1252 -*-
from login import acesso_issnet as acesso
from banco_dados import dicionario_empresas as de
from exportacao_issnet import export_issnet as ISS
from extrair import extrair_XML as arq_xml
from renomear import renomear_arquivos as rename
from copiar_rede_relatorios import copiar_rede as copiar_rede
from copia_xml_pastas.copiar_xml import navegar_pastas_xml_contratados as copiar_xmls_pastas
import os



if __name__ == '__main__':

    with open('R:\Compartilhado\Fiscal\lista_clientes_iss\senha.txt', 'r') as arquivo:
        credenciais = arquivo.readlines()
    
    CPF = credenciais[0].replace('\n', '')
    SENHAS = credenciais[1].replace('\n', '').split()
    SENHAS = [int(senha) for senha in SENHAS]

    dt_inicial = '01/12/2022'
    dt_final = '31/12/2022'
    data_lista = dt_inicial.split('/')
    competencia = data_lista[1] + data_lista[2]
    # print(competencia)
    planilha = de.planilha()
    dic_empresas = de.criar_dicionario_empresas(planilha)

    driver = acesso.criar_conexao(CPF, SENHAS)

    ISS.exportar_empresas_xml(dt_inicial, dt_final, driver, dic_empresas)

    # arq_xml.extrair_arquivos()

    # arq_xml.remover_arquivos_zip()

    # copiar_xmls_pastas(dic_empresas)

    print('gerado com sucesso!!!\o/\o/')

    os.system('pause')
