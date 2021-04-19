import json
import requests
import time


def exData(response):

    uuid = response["uuid"]
    time.sleep(30)
    data = requests.get(f"https://urlscan.io/api/v1/result/{uuid}/")
    return useData(data.json())


def useData(data):
    ipStats = data["stats"]["ipStats"]
    total_requests = ipStats[0]
    return total_requests.get("requests")
    # 1150, 9919