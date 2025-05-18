from serpapi import GoogleSearch
import os

def fetch_google_results(query, max_results=5):
    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": max_results
    }
    results = GoogleSearch(params).get_dict()
    return [res["link"] for res in results.get("organic_results", [])]
