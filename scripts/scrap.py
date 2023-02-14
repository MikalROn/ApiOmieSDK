from requests import get
from bs4 import BeautifulSoup


def pega_links_api():
    def retquest_devpageomie() -> BeautifulSoup:
        try:
            r = get('https://developer.omie.com.br/service-list/')
            r.raise_for_status()
            return BeautifulSoup(r.text, features="html.parser")
        except:
            raise Exception('Erro na requisição')
    suop = retquest_devpageomie().find('div', {'class': 'service-list'})
    return {
        item.get_text().strip(): item.get("href")
        for item in suop.find_all('a')
    }

