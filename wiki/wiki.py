import requests
from bs4 import BeautifulSoup


def get_html():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    get_page = requests.get(url).text
    return get_page


def get_subcategories():
    page = get_html()
    soup = BeautifulSoup(page, "lxml")
    subcategories = []
    letters = soup.find("div", class_="toccolours plainlinks center").find("span").find_all("a")
    for letter in letters:
        subcategories.append(letter.text)
    return subcategories


def get_data(page):
    animals = []
    expression = True
    while expression:
        soup = BeautifulSoup(page, "lxml")
        names = soup.find("div", class_="mw-category-group").find_all("a")
        for name in names:
            print(name.text)
            animals.append(name.text)
            if name.text == "Ящурки":
                expression = False
        if not expression:
            break
        links = soup.find("div", id="mw-pages").find_all_next("a")
        for a in links:
            if a.text == "Следующая страница":
                url = "https://ru.wikipedia.org/" + a.get("href")
                page = requests.get(url).text
    return animals


def result():
    animals = get_data(get_html())
    letters = get_subcategories()

    result = {}
    for letter in letters:
        count = 0
        for name in animals:
            if name.startswith(letter):
                count += 1
                result[letter] = count
    return result


for k, v in result().items():
    print(k, ":", v)
