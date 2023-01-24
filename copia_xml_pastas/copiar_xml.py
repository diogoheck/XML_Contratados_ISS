import os
import shutil
from renomear.renomear_arquivos import renomear_arquivos
from copiar_rede_relatorios.copiar_rede import criar_nova_pasta, existe_essa_pasta
pasta = r'U:\ISS\xml_contratados'
# C:\XML
# Percorrer a pasta dos XMLs


def mover_arquivo(origem, destino):
    shutil.move(origem, destino)


def navegar_pastas_xml_contratados(dic_empresas):

    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            old = os.path.join(diretorio, arquivo)

            if len(old.split('\\')) == 4:
                registro = os.path.join(diretorio, arquivo).split('\\')[
                    3].split('_')
                IM = registro[0]
                # print(registro)
                Nota = int(registro[2])
                cod_unico = dic_empresas.get(IM)[2]
                empresa = dic_empresas.get(IM)[1]
                nome_arquivo = f'{IM} {str(Nota)}.xml'
                new = f'U:\\ISS\\xml_contratados\\{nome_arquivo}'
                renomear_arquivos(old, new)

                caminho = f'U:\\ISS\\xml_contratados\\{cod_unico}'
                destino_arquivo = f'{caminho}\\{nome_arquivo}'
                if not existe_essa_pasta(caminho):
                    criar_nova_pasta(caminho)
                mover_arquivo(new, destino_arquivo)


if __name__ == '__main__':
    navegar_pastas_xml_contratados()
