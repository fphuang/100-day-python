from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"

response = requests.get(url=url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
article_tags = soup.find_all(name="a", class_="titlelink")
article_links = []
article_texts = []
for tag in article_tags:
    article_texts.append(tag.getText())
    article_links.append(tag.get('href'))

article_upvote_scores = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
print(article_texts)
print(article_links)
print(article_upvote_scores)

index = article_upvote_scores.index(max(article_upvote_scores))
print(article_texts[index])