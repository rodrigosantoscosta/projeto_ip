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
        
        print(f"Erro na requisição da API: {e}")
        
        return None


def exibir_menu():
    print('**** MENU DA CACHAÇARIA DO SEU ZÉ *****')
    print('--------------------------------------')
    print('1 - Selecionar numero de conselhos\n2 - Exibir conselhos\n4 - Salvar conselhos num arquivo de texto\n5 - Traduzir os conselhos do ingles para o portugues')
    print('--------------------------------------')
if __name__ == "__main__":
    print(tome_um_conselho())
    conselhos = []
    texto = 'Hello World!'
    print(traduzir(texto))
    exibir_menu()