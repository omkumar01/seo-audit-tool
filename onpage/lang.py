def getLang(page):
    lang_info = {}
    if page.find("html"):
        tag = page.find("html")
        if tag.get("lang") == None:
            lang_info["lang_exist"] = False
            lang_info["content"] = "no language attribute"
            return lang_info
        else:
            lang_info["lang_exist"] = True
            lang_info["content"] = tag.get("lang")
            return lang_info
