def filter_articles(articles, ignore_list, search_list):
    filtered_articles = []
    ignore_keywords = [keyword.lower() for keyword in ignore_list]
    search_keywords = [keyword.lower()
                       for keyword in search_list] if search_list else []

    for article in articles:
        title = (article.get("title") or "").lower()
        author = (article.get("author") or "").lower()
        urlToImage = (article.get("urlToImage") or "").lower()
        date = (article.get("publishedAt") or "").lower()

        description = (article.get("description") or "").lower()
        content = (article.get("content") or "").lower()
        article_text = f"{title} {author} {urlToImage} {date} {description} {content}"

        if ignore_keywords and any(keyword in article_text for keyword in ignore_keywords):
            continue

        if search_keywords and not any(keyword in article_text for keyword in search_keywords):
            continue

        filtered_articles.append(article)

    return filtered_articles
