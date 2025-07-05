def filter_articles(articles, ignore_list, search_list, category="general"):
    filtered_articles = []
    ignore_keywords = [keyword.lower() for keyword in ignore_list]
    search_keywords = [keyword.lower()
                       for keyword in search_list] if search_list else []

    # Add hardcoded words to ignore only for general category
    hardcoded_ignore = []
    if category == "general":
        hardcoded_ignore = ["dead", "killed", "fire",
                            "wildfire", "wildfires", "warn", "administration" "frontline",
                            "front-line", "legislation", "trope", "congress", "congressional",
                            "congressman", "congresswoman", "senator", "senators", "house of representatives",
                            "house of rep", "house", "senate", "tariff", "tax", "taxes", "taxation", "taxpayer",
                            "taxpayers", "taxpayer-funded", "taxpayer money", "taxpayer dollars", "taxpayer-funded",
                            "government-funded", "pentagon", "pentagon budget", "terrorist", "terrorism", "terrorists", "taliban"]

    domains_ignore = ["blabbermouth", "death", "anti-semitic",
                      "anti-semitism", "antisemitic", "antisemitism",]

    ignore_keywords = ignore_keywords + domains_ignore

    for article in articles:
        title = (article.get("title") or "").lower()
        author = (article.get("author") or "").lower()
        urlToImage = (article.get("urlToImage") or "").lower()
        date = (article.get("publishedAt") or "").lower()

        description = (article.get("description") or "").lower()
        content = (article.get("content") or "").lower()
        article_text = f"{title} {author} {urlToImage} {date} {description} {content}"

        # Combine user ignore list with hardcoded ignore list
        all_ignore_keywords = ignore_keywords + \
            [word.lower() for word in hardcoded_ignore]

        if all_ignore_keywords and any(keyword in article_text for keyword in all_ignore_keywords):
            continue

        if search_keywords and not any(keyword in article_text for keyword in search_keywords):
            continue

        filtered_articles.append(article)

    return filtered_articles
