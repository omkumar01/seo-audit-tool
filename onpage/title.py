def titleText(page):
    if page.find("title"):
        return page.find("title").get_text()
    else:
        return "no title tag found"
