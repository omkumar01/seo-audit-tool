def metaTags(page):
    meta_data = {}
    if page.find_all("meta"):
        tags = page.find_all("meta")
        for tag in tags:
            name = tag.get("name")
            prop = tag.get("property")
            if name == "viewport":
                meta_data["viewport"] = tag.get("content")
            if name == "keywords":
                meta_data["keywards"] = tag.get("content")
            if name == "description":
                meta_data["description"] = tag.get("content")
            if name == "robots":
                meta_data["robots"] = tag.get("content")
            if name == "twitter:card":
                meta_data["twitter:card"] = tag.get("content")
            if name == "twitter:title":
                meta_data["twitter:title"] = tag.get("content")
            if name == "twitter:description":
                meta_data["twitter:description"] = tag.get("content")
            if name == "twitter:image":
                meta_data["twitter:image"] = tag.get("content")

            if prop == "og:type":
                meta_data["og:type"] = tag.get("content")
            if prop == "og:image":
                meta_data["og:image"] = tag.get("content")
            if prop == "og:url":
                meta_data["og:url"] = tag.get("content")
            if prop == "og:title":
                meta_data["og:title"] = tag.get("content")
            if prop == "og:description":
                meta_data["og:description"] = tag.get("content")

            if tag.get("charset"):
                meta_data["charset"] = tag.get("charset")

        return meta_data

    else:
        return 0
