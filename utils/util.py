import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def save_soup(filename: str, soup: BeautifulSoup) -> None:
    with open(filename, 'w') as f:
        f.write(str(soup))

def retreive_soup(filename: str) -> BeautifulSoup:
    with open(filename, 'r') as f:
        html = f.read()
        soup = BeautifulSoup(html.text, 'html.parser')
        return soup

def get_soup(filename, url) -> BeautifulSoup:
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup


def make_soup(filename, url='no') -> None:
    if url =='no':
        soup = retreive_soup(filename)
    else:
         soup = get_soup(filename, url)
    return soup


def main_(filename: str, url: str) -> list:
    results = []
    
    for page in tqdm(range(1, 51)):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        soup = make_soup(filename, url)
        
        books = soup.select('article')
        
        for book in books:
            result = {
                'title': book.select_one('a img')['alt'],
                'price': book.select_one('p.price_color').text[2:],
            }
            results.append(result)
            # print(result)
    return results



if __name__ == '__main__':
    print('wrong file run')   