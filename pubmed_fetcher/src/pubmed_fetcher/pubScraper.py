import requests
import pandas as pd
import time
from typing import List

# NCBI PubMed API URLs
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

# Set your email and API key for better request limits
EMAIL = "mlvijayalakshmiloganadhan@gmail.com	"  # Replace with your email
API_KEY = "ce7eb712ebe7085eba9f5547b6df94316108"  # Replace with your API key or leave as None


def fetch_pubmed_ids(query: str) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 100,
        "tool": "pubmed_fetcher",
        "email": EMAIL,
    }
    if API_KEY:
        params["api_key"] = API_KEY

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

    data = response.json()
    print("DEBUG: PubMed API Response:", data)  # Debugging output

    return data.get("esearchresult", {}).get("idlist", [])


def fetch_paper_details(pubmed_ids):
    if not pubmed_ids:
        print("⚠ No PubMed IDs found!")
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "json",
        "tool": "pubmed_fetcher",
        "email": EMAIL,
    }
    if API_KEY:
        params["api_key"] = API_KEY

    response = requests.get(DETAILS_URL, params=params)
    response.raise_for_status()

    data = response.json()
    print("📄 Paper Details Response:", data)  # Debugging output

    papers = []
    for pubmed_id in pubmed_ids:
        details = data.get("result", {}).get(pubmed_id, {})
        if details:
            papers.append({
                "PubMed ID": pubmed_id,
                "Title": details.get("title", "N/A"),
                "Authors": ", ".join(author.get("name", "Unknown") for author in details.get("authors", [])),
                "Journal": details.get("source", "N/A"),
                "Publication Date": details.get("pubdate", "N/A"),
            })
        time.sleep(0.1)  # Respect NCBI rate limits

    return papers


def save_to_csv(papers, filename):

    if not papers:
        print("⚠ No papers found to save.")
        return

    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"✅ Results saved to {filename}")


def get_papers(query, filename="results.csv"):

    print(f"🔍 Fetching papers for query: {query}...")

    pubmed_ids = fetch_pubmed_ids(query)
    if not pubmed_ids:
        print("❌ No results found for the given query.")
        return

    papers = fetch_paper_details(pubmed_ids)
    save_to_csv(papers, filename)


# Example usage
if __name__ == "__main__":
    get_papers("cancer treatment")
