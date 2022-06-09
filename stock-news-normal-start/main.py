import requests
import twilio


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=HX3IBCZAZ22MJDXW")
response.raise_for_status()
data = response.json()
data_2 = [value for (key, value) in data.items()]
print(data_2)


data_2 = float(data['Time Series (Daily)']['2022-05-25']['4. close'])
print(data_2)

difference = abs(data_1 - data_2)
print(difference)


change = difference/ data_2
print(change)

if change > .05:
    print("great newsss")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


response_news = requests.get(url="https://newsapi.org/v2/everything?q=tesla&from=2022-04-30&sortBy=publishedAt&apiKey=8b4995564b61465697202f1c7d5d573e")
response_news.raise_for_status()
data_news = response_news.json()



articles = (data_news['articles'][4:7])
print(articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 



article_list = []
for article in articles:
    article_list.append(article['title'])
    article_list.append(article['description'])

print(article_list)

account_sid ="ACf2ee3320ca14b2a20063a53f0e375839"
authen_token = "51b50f17964e85499752942edcf50fe6"
client = twilio.Client(account_sid, authen_token)

message = client.messages.create(
    body=f"{article_list}",
    from_="+17745003472",
    to="+18182670211"
)




"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

