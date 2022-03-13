from gnews import GNews

google_news = GNews()
json_resp = google_news.get_news('Pakistan')
article = google_news.get_full_article(
    json_resp[0]['url'])  # newspaper3k instance, you can access newspaper3k all attributes in article


print(article.text)
