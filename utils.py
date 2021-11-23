import requests
from bs4 import BeautifulSoup

class Book:
    def __init__(self, url , page , soup, f, ListUrlCategorie, compteur_j, i):
        self.url = url
        self.page = page
        self.soup = soup
        self.f = f
        self.ListUrlCategorie = ListUrlCategorie
        self.compteur_j = compteur_j
        self.i = i

    def get_categories_url(self):
        """
        Adress url of each pages category
        """

    for u in range(2, len(self.f) + 1):
        self.i = self.i + 1
        self.compteur_j = self.compteur_j + 1
        format_text = self.f[self.compteur_j].text.replace("\n", "")
        b = format_text.strip()
        v = b.lower()
        t = str(v)
        nbr_espace = v.count(" ")
        if nbr_espace > 0:
            c = t.replace(" ", "-")
            url0 = "https://books.toscrape.com/catalogue/category/books/" + str(c) + "_" + str(self.i) + "/index.html"
            self.listUrlCategorie.append(url0)
        else:
            url1 = "https://books.toscrape.com/catalogue/category/books/" + str(t) + "_" + str(self.i) + "/index.html"
            self.listUrlCategorie.append(url1)

category_urls = Book('https://books.toscrape.com/index.html', requests.get(url),
                     BeautifulSoup(page.content, 'html.parser',
                    soup.find('aside', {'class': 'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li'),
                    [], 0, 1))
category_urls = category_urls.get_categories_url()
print(category_urls)
