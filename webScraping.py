import requests
from bs4 import BeautifulSoup
from model import Model_Mensagem

def return_dado():
    resposta = requests.get('http://www.prefe.ufu.br/concessoes/cantina-da-tia-lu')

    if resposta.status_code == 200:
        # Verifica a resposta HTML
        print("Resposta recebida com sucesso!")
        soup = BeautifulSoup(resposta.content, 'html.parser')
        
        # Imprime o HTML da página para análise
        #print(soup.prettify())  # Veja como está estruturada a página
        valor = soup.find('div', class_='node')
        
        dados_menu= {
            "menuNav": "Web Scraping tia lu",
            "link": valor.text,
        }
        valor = soup.find_all('div', class_='field-label')
        #valor1 = valor.split('</div>')
        print(type(valor))
        for v in valor: 
            print(f'------------------\n{v.text} \n--------------')
        valor1 = soup.find_all('div', class_='field-items')
        #valor1 = valor.split('</div>')
        print(type(valor1))
        i = 0 
        label =[]
        items = []
        for v in range(4,len(valor1)):
            if v == 11 or v == 12 or v == 17 or v == 18 or v ==19:
                continue
            print(f'------------------\n{valor1[v].text} \n--------------')
            label.append(valor[i].text)
            items.append(valor1[v].text)
            i += 1
        tialu= {
                "menuNav": label,
                "link": items,
        }
        for i in range(len(tialu['link'])):
            print(f'{tialu["link"][i]}---------------\n\n\n\n\n\nn\n')
        #return dados_menu
        return tialu
    else:
        print(f"Erro ao acessar o site: Status {resposta.status_code}")
        return None
    

return_dado();