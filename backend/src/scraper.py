import requests
from bs4 import BeautifulSoup


def g1_scraper(url):
    titulo_class = 'content-head__title'
    texto_class = 'content-text__container'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
 
    titulo = soup.find('h1', class_=titulo_class).text
    texto = soup.find_all('p', class_=texto_class)


    texto_completo = ''

    for i in texto:
        texto = i.text
        texto_completo += texto
        texto_completo += '\n'

    return (titulo, texto_completo)

if __name__ == "__main__":
    url = "https://g1.globo.com/economia/noticia/2024/07/17/taxad-entenda-as-criticas-ao-ministro-da-fazenda.ghtml"
    titulo, texto = g1_scraper(url)
    print(titulo)
    print(texto)