import requests
from bs4 import BeautifulSoup
def return_dado():
    r = requests.get('https://proae.ufu.br/intercampi')

    if (r.status_code == 200):
        soup = BeautifulSoup(r.content, 'html.parser')
        horarios = soup.find('div', about='/conteudo/unidade-boa-vista-unidade-araras-0')
        saida = horarios.find_all('span', class_='date-display-single')

        horas = []
        for hora in saida:
            horas.append(str(hora.text))
            
        return horas
    
    else:
        print(f"Erro ao acessar o site: Status {r.status_code}")
        return None
return_dado()