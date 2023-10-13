import requests
from bs4 import BeautifulSoup

# Define the URL of the website we want to scrape
url = "https://quotes.toscrape.com"

# Sending an HTTP GET request to the website
response = requests.get(url)

if response.status_code == 200:
    # Parsing the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Finding and extracting the quotes
    quotes = soup.find_all("span", class_="text")

    # Saving the quotes
    with open("quotes.txt", "w") as file:
        for quote in quotes:
            file.write(quote.get_text() + "\n")

    print("Scraped quotes are saved to quotes.txt")
else:
    print("Failed to retrieve the website")
    