from urllib.request import Request, urlopen
from selenium import webdriver
from bs4 import BeautifulSoup


def get_GST():
    req = Request('https://www.binance.com/ru/price/gst', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req).read(), 'html.parser')
    div = soup.find_all('div', class_='css-12ujz79')
    price = float(div[0].text[2:])
    # print(f'{price}$ - GST')
    return price


def get_GMT():
    req = Request('https://www.binance.com/ru/price/green-metaverse-token', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req).read(), 'html.parser')
    div = soup.find_all('div', class_='css-12ujz79')
    price = float(div[0].text[2:])
    # print(f'{price}$ - GMT')
    return price


def get_SOL():
    req = Request('https://www.binance.com/ru/price/solana', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req).read(), 'html.parser')
    div = soup.find_all('div', class_='css-12ujz79')
    price = float(div[0].text[2:])
    # print(f'{price}$ - SOL')
    return price


def get_shoe_min_price():
    driver = webdriver.Edge()
    driver.get("https://magiceden.io/marketplace/stepn")
    elem = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div/div[3]/div[1]/div/span').text
    price_in_sol = float(elem[:-1])
    # print(f'{price_in_sol} - SOL')
    # print(f'{price_in_sol * get_SOL()} $')
    return price_in_sol

    
# get_GST()
# get_GMT()
# get_SOL()
# get_shoe_min_price()
