import env
import requests
from newsapi import NewsApiClient
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_price_change_ratio():
    #TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
    response = requests.get(env.stock["url"], params=env.stock["params"])
    response.raise_for_status()
    daily_data = [value["4. close"] for (key, value) in response.json()["Time Series (Daily)"].items()]
    price_today = float(daily_data[0])

    #TODO 2. - Get the day before yesterday's closing stock price
    price_yesterday = float(daily_data[1])

    #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
    price_change = abs(price_today - price_yesterday)

    #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
    change_ratio = (price_change / price_yesterday) * 100


    #TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    print(f"price change: {price_change}, ratio: {change_ratio}")
    # if change_ratio > 5:
    #     print("Get News")
    # else:
    #     print("Nothing exciting")

    return change_ratio

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# Init
def get_news():
    client = NewsApiClient(api_key='11ae3b2c73fa41c2b0ba66d7eaa7c2ae')

    # # /v2/top-headlines
    # top_headlines = client.get_top_headlines(q='bitcoin',
    #                                           sources='bbc-news,the-verge',
    #                                           category='business',
    #                                           language='en',
    #                                           country='us')

    # /v2/top-headlines/sources
    # sources = client.get_sources()

    # /v2/everything
    all_articles = client.get_everything(q="tesla",
                                          sources='bbc-news,the-verge,twitter,cnn',
                                          domains='bbc.co.uk,techcrunch.com,cnn.com,twitter.com',
                                          from_param='2021-12-22',
                                          # to='2021-12-23',
                                          sort_by='publishedAt')

    return all_articles


all_articles = get_news()['articles'][:3]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
print(all_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
headline_list = [item['title'] for item in all_articles]
brief_list = [item['description'] for item in all_articles]
change_ratio = get_price_change_ratio()


#TODO 9. - Send each article as a separate message via Twilio. 
account_sid = env.twilio['account_sid']
auth_token = env.twilio['auth_token']
client = Client(account_sid, auth_token)

for n in range(1):
    icon = "🔺" if change_ratio > 5 else "🔻"
    headline = f"Headline: {headline_list[n]} (TSLA)?"
    brief = brief_list[n]
    body = f"{icon}\n{headline}\n{brief}"
    message = client.messages.create(
                         body=body,
                         from_=env.twilio['phone_number'],
                         to='+12165517819'
                     )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

