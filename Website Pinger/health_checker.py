"""
health_checker.py
Performs a health check on a target URL by fetching the page, extracting its title,
and reporting the HTTP status code, response time, and any errors encountered.
"""

import requests
from bs4 import BeautifulSoup
import datetime

TARGET_URL = "https://www.example.com/"    ## Edit the target URL as per your need

def health_checker(target_url=TARGET_URL):
  timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
  try:
    response = requests.get(target_url,timeout=10)
    soup = BeautifulSoup(response.text,"html.parser")
    title = soup.find("title").text if soup.find("title") else "NO TITLE"

    print(f"[{timestamp}] Status:{response.status_code} | Title:'{title}' | Time elapsed:{response.elapsed.total_seconds():.2f}s")
    return {"status":response.status_code, "title":title, "ok":True, "error":None}
  except Exception as e:
    print(f"[{timestamp}] ERROR: {str(e)}")
    return {"status":None, "title": None, "ok":False, "error":str(e)}

if __name__ == "__main__":
  health_checker()
