import requests
from bs4 import BeautifulSoup




class Book:
    def __init__(self, title, unit_price):
        self.title = title
        self.unit_price = unit_price


class Category:
    def __init__(self, url, title):
        self.url = url
        self.title = title

    @classmethod
    def get_categories_urls(cls):
        url = 'https://books.toscrape.com/index.html'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        f = soup.find('aside', {'class': 'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')
        list_url_categorie = []
        compteur_j = 0
        i = 1
        for u in range(2, len(f) + 1):
            i = i + 1
            compteur_j = compteur_j + 1
            format_text = f[compteur_j].text.replace("\n", "")
            b = format_text.strip()
            v = b.lower()
            t = str(v)
            nbr_espace = v.count(" ")
            if nbr_espace > 0:
                c = t.replace(" ", "-")
                url0 = "https://books.toscrape.com/catalogue/category/books/" + str(c) + "_" + str(i) + "/index.html"
                list_url_categorie.append(url0)
            else:
                url1 = "https://books.toscrape.com/catalogue/category/books/" + str(t) + "_" + str(i) + "/index.html"
                list_url_categorie.append(url1)
        return list_url_categorie

    def get_books_url(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll('div', {'class': 'image_container'})
        book_urls = []
        for link in links:
            a = link.find('a')
            href = a['href']
            book_urls.append(href.replace('../../../', 'https://books.toscrape.com/catalogue/'))
        return book_urls


if __name__ == "__main__":
    book_1 = Book("Le seigneur des anneaux", 20)
    print(book_1.unit_price)

    urls = Category.get_categories_urls()
    print('urls:', urls)

    fantasy_category = Category("https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html", "Fantasy")
    fantasy_category_books_urls = fantasy_category.get_books_url()
    print("fantasy_category_books_urls:", fantasy_category_books_urls)