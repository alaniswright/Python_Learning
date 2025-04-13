import requests
from bs4 import BeautifulSoup

URL = "https://www.legislation.gov.uk/new/uk/2025-04-10"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

laws = soup.find_all("h6")

law_entries = [
    h6_element.parent for h6_element in laws
]

for law in law_entries:
    title_element = law.find("h2")
    summary = law.find("p")
    print(title_element)
    print(summary)
