# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-
# import webdriver
from __future__ import unicode_literals
from distutils.command.config import LANG_EXT
from selenium.webdriver.support.select import Select
from exception.lancar_excecao import lancamento_excecao
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By


def inserir_IE(driver, IE):
    driver.find_element(By.XPATH, '//*[@id="txtCae"]').send_keys(IE)


def clicar_botao_procurar_empresa(driver):
    driver.find_element(By.CLASS_NAME, 'nc-search').click()


def seleciona_empresa(driver, IE):
    lancamento_excecao(inserir_IE, driver, IE)
    lancamento_excecao(clicar_botao_procurar_empresa, driver)


def menu_toggle(driver):
    driver.find_element(By.XPATH, '//*[@id="menu-toggle"]').click()


def mudar_barra_lateral(driver):
    for _ in range(10):
        try:
            elemento = driver.find_element(By.ID, 'wrapper')
            break
        except ElementNotInteractableException as e:
            print('Retry in 1 second', e)
            time.sleep(1)

    if elemento.get_attribute("class") != 'toggled':
        lancamento_excecao(menu_toggle, driver)


def seleciona_menu(driver):
    lancamento_excecao(mudar_barra_lateral, driver)


def seleciona_menu_contratados_1(driver):
    driver.find_element(By.XPATH,
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[3]/div/span[3]').click()


def seleciona_menu_contratados_2(driver):
    driver.find_element(By.XPATH,
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[2]/div/span[3]').click()


def seleciona_servicos_contratados(driver, IE, empresa):
    if empresa[6] == 'I':
        lancamento_excecao(seleciona_menu_contratados_1, driver)

    else:
        lancamento_excecao(seleciona_menu_contratados_2, driver)


# consulta_de_notas_tomadas

def consulta_menu_1(driver):
    driver.find_element(By.XPATH,
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[3]/ul/li[4]/div/a').click()


def consulta_menu_2(driver):
    driver.find_element(By.XPATH,
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[3]/ul/li[6]/div/a').click()


def consulta_menu_3(driver):
    driver.find_element(By.XPATH,
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[2]/ul/li[6]/div/a').click()


def consulta_de_notas_tomadas(driver, simples, empresa):
    if not simples and empresa[6] == 'I':

        lancamento_excecao(consulta_menu_1, driver)

    elif simples and empresa[6] == 'I':

        lancamento_excecao(consulta_menu_2, driver)
    else:

        lancamento_excecao(consulta_menu_3, driver)


# mudar_frame
def switch_frame(driver):
    frame = driver.find_element(By.XPATH,
        '//*[@id="iframe"]')

    driver.switch_to.frame(frame)


def mudar_frame(driver):
    lancamento_excecao(switch_frame, driver)

# mudar_para_relatorio


def switch_relatorio(driver):
    frame = driver.find_element(By.XPATH,
        '//*[@id="viewer"]')
    driver.switch_to.frame(frame)


def mudar_para_relatorio(driver):
    lancamento_excecao(switch_relatorio, driver)


def mudar_frame_principal_except(driver):
    driver.switch_to.default_content()


def mudar_frame_principal(driver):
    lancamento_excecao(mudar_frame_principal_except, driver)


# selecionar_serie_nota
def clicar_na_serie_nota(driver):
    select = Select(driver.find_element(By.ID, 'ddlSerie'))
    select.select_by_value('22')


def selecionar_serie_nota(driver):
    lancamento_excecao(clicar_na_serie_nota, driver)

# selecionar_filtros_adicionais


def clicar_filtros_adicionais(driver):
    driver.find_element(By.ID, "imbArrow").click()


def selecionar_filtros_adicionais(driver):
    lancamento_excecao(clicar_filtros_adicionais, driver)

# selecionar_data_inicial


def inserir_data_inicial(driver, dt_inicial):
    driver.find_element(By.XPATH,
        '//*[@id="txtDtEmissaoIni"]').send_keys(dt_inicial)


def selecionar_data_inicial(driver, dt_inicial):
    lancamento_excecao(inserir_data_inicial, driver, dt_inicial)
# selecionar_data_final


def inserir_data_final(driver, dt_final):
    driver.find_element(By.XPATH,
        '//*[@id="txtDtEmissaoFim"]').send_keys(dt_final)


def selecionar_data_final(driver, dt_final):
    lancamento_excecao(inserir_data_final, driver, dt_final)

# buscar_notas


def clicar_buscar_notas(driver):
    driver.find_element(By.XPATH,
        '//*[@id="btnBuscarNotas"]/span').click()


def buscar_notas(driver):
    lancamento_excecao(clicar_buscar_notas, driver)


# exportar_notas_xml
def clicar_exportar_xmls(driver):
    driver.find_element(By.ID,
        "dgDocumentos__ctl2_btnExpTodos").click()


def exportar_notas_xml(driver):
    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    if len(rows) > 2:
        lista_notas = list(rows)
        print(
            f' linha 1 {lista_notas[1].find_elements(By.TAG_NAME, "td")[0].text}')
        print(
            f' ultima linha {lista_notas[-2].find_elements(By.TAG_NAME,"td")[0].text}')
        lancamento_excecao(clicar_exportar_xmls, driver)


# trocar empresa


def clica_entrar_empresa(driver):
    driver.find_element(By.XPATH,
        '//*[@id="lblNomeEmpresa"]').click()


def trocar_empresa(driver):
    lancamento_excecao(clica_entrar_empresa, driver)


def percorrer_menus_servicos_contratados_xml(driver, IE, dt_inicial,
                                             dt_final, simples,
                                             empresa):
    seleciona_empresa(driver, IE)
    time.sleep(0.5)
    seleciona_menu(driver)
    seleciona_servicos_contratados(driver, IE, empresa)
    consulta_de_notas_tomadas(driver, simples, empresa)
    mudar_frame(driver)
    selecionar_serie_nota(driver)
    selecionar_filtros_adicionais(driver)
    selecionar_data_inicial(driver, dt_inicial)
    selecionar_data_final(driver, dt_final)
    buscar_notas(driver)
    exportar_notas_xml(driver)


def empresa_do_simples(empresa):
    if empresa[5] == 'N':
        return False
    else:
        return True


def exportar_empresas_xml(dt_inicial, dt_final, driver, dic_empresas):
    for empresa in dic_empresas.values():
        Identificador = empresa[4]
        simples = empresa_do_simples(empresa)

        percorrer_menus_servicos_contratados_xml(driver, Identificador,
                                                 dt_inicial,
                                                 dt_final, simples,
                                                 empresa)

        # gerar segunda empresa em diante
        mudar_frame_principal(driver)
        trocar_empresa(driver)
    time.sleep(10)
    driver.close()
    driver.quit()
