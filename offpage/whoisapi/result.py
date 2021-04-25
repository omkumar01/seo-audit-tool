def domainData(response):
    data = {}
    data["registrar_name"] = response["registrar"]["name"]
    data["registrar_url"] = response["registrar"]["url"]
    data["domain_age"] = response["domain_age"]
    data["domain_exp_date"] = response["expire_date"]
    data["nameservers"] = response["nameservers"]
    return data