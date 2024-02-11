import requests
from twilio.rest import Client
import html

url = 'https://www.alphavantage.co/query'
alpha_vantage_api = "Enter Your API Key Token Here"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": alpha_vantage_api
}

stock_response = requests.get(url=url, params=parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# --------------------
data_dict = stock_data.get("Time Series (Daily)")
daily_stock_list = [value for (key, value) in data_dict.items()]

print(daily_stock_list)

yesterday_close = daily_stock_list[0]["4. close"]
day_before_yesterday_close = daily_stock_list[1]["4. close"]

close_percent = (float(yesterday_close) / float(day_before_yesterday_close) - 1) * 100

# ------------ getting news
if close_percent >= 1:
    print("Getting News")

    # fetching the news data
    COMPANY_NAME = "Tesla Inc"
    url = ('https://newsapi.org/v2/everything?'
           'q="Tesla Inc"&'
           'from=2024-02-10&'
           'sortBy=popularity&'
           'apiKey=Enter Your API Key Token Here')

    news_response = requests.get(url)
    news_response.raise_for_status()
    news_data = news_response.json()

    articles = news_data.get('articles')

    for article in articles:
        article_source = article['source']['name']
        article_author = article.get("author")
        article_title = article.get("title")
        article_description = article.get("description")

        formatted_message = html.unescape(f"\nARTICLE SOURCE: {article_source}\n\n"
                                          f"AUTHORED BY: {article_author}\n\n"
                                          f"TITLE: {article_title}\n\n"
                                          f"DESCRIPTION: {article_description}")

        # using twillo to send our message
        account_sid = "Enter Your Twillo account_sid Here"
        auth_token = "Enter Your Twillo auth_token Here"

        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"{formatted_message}",
            from_='+19252414618',
            to='+2348105662218'
        )

        print(message.status)
else:
    print("No news")
