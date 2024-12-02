import loguru
import requests
from deep_translator import GoogleTranslator
from loguru import logger
import os 
import time

# # Use any translator you like, in this example GoogleTranslator
# translated = GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig

def traduzir(texto):
    try:
        traducao = GoogleTranslator(source='auto', target='portuguese').translate(texto)
        return traducao
    
    except Exception as error:
        logger.exception(f'Erro ao traduzir: {error}')

def tome_um_conselho():
    try:
        response = requests.get('https://api.adviceslip.com/advice')
        if response.status_code == 200:
            id = response.json()['slip']['id']
            conselho = response.json()['slip']['advice']
            return (f'{id} - {conselho}')
        
        else:
            logger.error("Erro ao tentar gerar conselho.")
            
            return None
    except Exception as e:
        
        logger.exception(f"Erro na requisição da API: {e}")
        
        return None
    
def salva_conselhos(arquivo, conselhos):
    try:
        with open(arquivo, 'a', encoding='UTF-8') as a:
            for conselho in conselhos:
                a.writelines(conselho + '\n')
        logger.info(f"Conselhos salvos no'{arquivo}'")
    except Exception as e:
        logger.error(f"Erro ao salvar conselhos no arquivo '{arquivo}': {e}")

def lembrar_conselhos(arquivo):
    print('Estou lembrando da sabedoria dos anciões anglófonos')
    if os.path.exists(arquivo):
        with open (arquivo,'r') as file:
            arquivo_existe = file.read()
            arquivo_existe = arquivo_existe.splitlines()
        
        return arquivo_existe
    else:
        return('Ei Zé o arquivo não existe, por favor salvar alguma mensagem no texto!')
        
def exibir_menu():
    
    print('---------------------------------------')
    print('**** MENU DA CACHAÇARIA DO SEU ZÉ *****')
    print('1 - Selecionar numero de conselhos')
    print('2 - Exibir conselhos')
    print('3 - Salvar conselhos num arquivo de texto')
    print('4 - Traduzir os conselhos do ingles para o portugues')
    print('5 - Traduzir os conselhos salvos')
    print('0 - Sair do programa')
    print('----------------------------------------')
    
if __name__ == "__main__":
    # print(tome_um_conselho())
    conselhos = []
    # texto = 'Hello World!'
    # print(traduzir(texto))
    # exibir_menu()
    arquivo_conselhos ='conselhos.txt'
    status = -1

    while status != 0:
        exibir_menu()
        status = int(input('Digite a opção desejada: '))
       
        match status:
            case 1:
                try:
                    numero_de_conselhos = int(input('Quantos conselhos você vai querer?: '))
        
                    for i in range(numero_de_conselhos):
                        conselhos.append(tome_um_conselho())

                except Exception as e:
                    logger.exception(f"Erro! Tente novamente um valor válido: {e}")

            case 2:
                print('Lista de conselhos:\n')
                for conselho in conselhos:
                    print(conselho)

            case 4:
                traduzidos = []
                
                for i in range(len(conselhos)):
                    texto = conselhos[i]
                    traduzidos.append(traduzir(texto))
                print('Conselhos traduzidos:\n')
                for traduzido in traduzidos:
                    print(traduzido)
            case 3:
                salva_conselhos(arquivo_conselhos, conselhos)        
            case 5:
                sabedoria_adquidira = lembrar_conselhos(arquivo_conselhos)
                for i in range(len(sabedoria_adquidira)):
                    print(traduzir(sabedoria_adquidira[i]))
                
            case 0:
                status = 0
            case _:
                logger.error("Opção inválida. Escolha uma opção do menu!")        
    
    print('Obrigado por visitar a Cachaçaria do seu Zé!')