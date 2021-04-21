def headerCount(page):
    headcount = {}
    h1Tag = page.find_all("h1")
    count = 0
    for items in h1Tag:
        count += 1
    headcount["h1count"] = count

    h2Tag = page.find_all("h2")
    count = 0
    for items in h2Tag:
        count += 1
    headcount["h2count"] = count

    h3Tag = page.find_all("h3")
    count = 0
    for items in h3Tag:
        count += 1
    headcount["h3count"] = count

    h4Tag = page.find_all("h4")
    count = 0
    for items in h4Tag:
        count += 1
    headcount["h4count"] = count

    h5Tag = page.find_all("h5")
    count = 0
    for items in h5Tag:
        count += 1
    headcount["h5count"] = count

    return headcount
