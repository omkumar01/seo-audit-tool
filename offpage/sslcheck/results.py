def exSSL(response):
    data = {}
    if response["status"] == True:
        data["ssl_exist"] = response["status"]
        data["valid_upto"] = response["validTo"]
        ex = response["expiresIn"]
        data["expires_in"] = f"{ex} days"
        data["issuer"] = response["issuer"]["O"]
        return data
    else:
        data["ssl_exist"] = False
        return data
