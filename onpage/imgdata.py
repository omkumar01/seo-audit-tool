def imgAlt(page):
    img_data = {}
    imgcount = 0
    img_alt_found = 0
    img_alt_not_found = 0
    if page.find_all("img"):
        img = page.find_all("img")

        for i in img:
            imgcount += 1
            if i.get("alt") == None:
                img_alt_not_found += 1
            else:
                img_alt_found += 1

        img_data["imgcount"] = imgcount
        img_data["img_alt_found"] = img_alt_found
        img_data["img_alt_not_found"] = img_alt_not_found
        return img_data
    else:
        img_data["imgcount"] = imgcount
        img_data["img_alt_found"] = img_alt_found
        img_data["img_alt_not_found"] = img_alt_not_found
        return img_data