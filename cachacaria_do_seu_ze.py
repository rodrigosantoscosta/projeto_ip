import loguru
import requests
from deep_translator import GoogleTranslator
from loguru import logger

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
            
            return (response.json()['slip']['advice'])
        
        else:
            print("Erro ao tentar gerar conselho.")
            
            return None
    except Exception as e:
        
        logger.exception(f"Erro na requisição da API: {e}")
        
        return None
    
def salva_conselhos(arquivo, conselhos):
    with open(arquivo, 'a') as a:
        for conselho in conselhos:  
            a.write(conselho)
        
def exibir_menu():
    
    print('--------------------------------------')
    print('**** MENU DA CACHAÇARIA DO SEU ZÉ *****')
    print('1 - Selecionar numero de conselhos')
    print('2 - Exibir conselhos')
    print('3 - Salvar conselhos num arquivo de texto')
    print('4 - Traduzir os conselhos do ingles para o portugues')
    print('0 - Sair do programa')
    print('--------------------------------------')
    
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
            
            case 0:
                status = 0
    
    print('Obrigado por visitar a Cachaçaria do seu Zé!')
