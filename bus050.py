import requests
from bs4 import BeautifulSoup

def get_horario_050():
    r = requests.get('https://www.montecarmelo.mg.gov.br/transporte-publico')

    if (r.status_code == 200):
        soup = BeautifulSoup(r.content, 'html.parser')
        horarios = soup.find('div', class_='row information_line linha50')
        itens_horarios = horarios.find_all('div', class_='row')

        pontos = []
        for item in itens_horarios:
            linhas = str(item.text).split(sep="\n")
            for linha in linhas:
                pontos.append(linha)
                
        horas = []
        for ponto in pontos:
            if("Campus Novo" in ponto):
                hora = str(ponto).split(" » ")
                horas.append(hora[0])
        
        return horas
    
    else:
        print(f"Erro ao acessar o site: Status {r.status_code}")
        return None
get_horario_050()