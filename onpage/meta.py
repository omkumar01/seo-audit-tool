def metaTags(page):
    if page.find_all("meta"):
        tags = page.find_all("meta")
        for tag in tags:
            print(tag.get("name"))
        return 0
    else:
        return "no meta tag found"
