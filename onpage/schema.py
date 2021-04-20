def checkSchema(page):
    if page.find_all("script"):
        scriptsTags = page.find_all("script")
        for scriptsTag in scriptsTags:
            if scriptsTag.get("type") == "application/ld+json":
                return True

    else:
        return False
