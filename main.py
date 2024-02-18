from utils.util import make_soup, get_soup, main_
import pandas as pd


filename = "data/html_text.txt"
url = 'https://books.toscrape.com'


if __name__ == '__main__':
    list_ = main_(filename, url='https://books.toscrape.com')
    df = pd.DataFrame(list_)
    df.to_csv("data/results.csv", index=False)
