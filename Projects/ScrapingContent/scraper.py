# Real python practice project
# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_cards = results.find_all("div", class_="card-content")

for job_card in job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

print("""
---
ALL JOBS THAT MENTION PYTHON
---
""")

# Finding all the jobs that mention python
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# Getting surrounding information for jobs that mention python
python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Count of python jobs
print("""
---
COUNT OF PYTHON JOBS
---
""")

print(len(python_jobs))

print("""
---
PYTHON JOBS
---
""")


# Printing all the python jobs
for job_card in python_job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    link_url = job_card.find_all("a")[1]["href"] # Find second [1] link (tagged as "a") then grab the href attribute
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: {link_url}\n")
    print()

# Extract attributes from HTML elements

print("""
---
LINK TEXT
---
""")

