import json
import requests
import time


def exData(response):

    uuid = response["uuid"]
    time.sleep(30)
    data = requests.get(f"https://urlscan.io/api/v1/result/{uuid}/")
    return useData(data.json())


def useData(data):
    reData = {}
    ipStats = data["stats"]["ipStats"]
    total_requests = ipStats[0]
    reData["total_requests"] = total_requests.get("requests")
    reData["secure_percentage"] = data["stats"]["securePercentage"]
    techs = data["meta"]["processors"]["wappa"]["data"]
    technology_used = []
    for tech in techs:
        technology_used.append(tech["app"])
    reData["technology_used"] = technology_used
    return reData