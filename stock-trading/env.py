stock = {
    "url": "https://www.alphavantage.co/query",
    "params": {
        "function": "TIME_SERIES_DAILY",
        "outputsize": "compact",
        "datatype": "json",
        "symbol": "TSLA",
        "apikey": "99BXJROZJSXSL6LQ",
    }
}

twilio = {
    "phone_number": "+14785004220",
    "account_sid": "AC57f9802cc13704fea73fde8397750a27",
    "auth_token": "0e794481d85c3c755c611092ba6fbc98"
}

newsapi = {
    "url": "https://newsapi.org/v2/everything",
    "params" : {
        "q": "tesla",
        "from": "2021-12-22",
        "sortBy": "publishedAt",
        "apiKey": "11ae3b2c73fa41c2b0ba66d7eaa7c2ae"
    }
}