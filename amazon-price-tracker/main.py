from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://www.amazon.com/dp/B00X9JNWGS/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
headers = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4707.0 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()

content = response.text
print(content)

soup = BeautifulSoup(content, "html.parser")
price_span = soup.find(name="span", class_="a-size-medium a-color-price priceBlockSalePriceString")
price_text = price_span.getText()
price_fryer = price_text.split("$")[1]
price_fryer = float(price_fryer)
print(price_fryer)

