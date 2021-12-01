import requests
from bs4 import BeautifulSoup




class Book:
    def __init__(self,title, unit_price):
        self.title = title
        self.unit_price = unit_price


class Category:
    def __init__(self, url,title,pages):
        self.title = title
        self.url = url
        self.pages = pages

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

    def all_pagination(self):
        """
        return all pages
        """
        listUrlCategories = []
        x = 0
        w = 0


        for i in self.pages:
            w = w + 1
            p = "page-" + str(x + 1) + ".html"
            url4 = self.pages[w - 1].replace("index.html", p)
            page = requests.get(url4)
            soup = BeautifulSoup(page.content, 'html.parser')
            status = page.status_code
            if status == 200:
                f = soup.find('li', {'class': 'current'})
                a = str(f)
                b = a[60:61]
                c = int(b)
                for i in range(c):
                    p = "page-" + str(i + 1) + ".html"
                    url4 = self.pages[w - 1].replace("index.html", p)
                    listUrlCategories.append(url4)
            else:
                listUrlCategories.append(self.pages[w - 1])
        return listUrlCategories


if __name__ == "__main__":
    book_1 = Book("Le seigneur des anneaux", 20)
    print(book_1.unit_price)

    urls = Category.get_categories_urls()
    print('urls:\n',"\n".join(urls))

    fantasy_category = Category("https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html","Fantasy","listUrlCategorie")

    fantasy_category_books_urls = fantasy_category.get_books_url()
    print('fantasy_category_books_urls:\n',"\n". join(fantasy_category_books_urls))

    Allpages = fantasy_category.all_pagination()
    print('url all pages:\n', "\n".join(Allpages))

