from gnews import GNews

google_news = GNews()
json_resp = google_news.get_news('python programming')
article = google_news.get_full_article(
    json_resp[0]['url'])


print(article.text)
