import requests
from bs4 import BeautifulSoup

# Define the URL of the website we want to scrape
url = input("Enter the URL of the website you want to scrape: ")

# Let the user define the file name for a scraped data
file_name = input("Enter the name of the file to save the data: ")

# Sending an HTTP GET request to the website
response = requests.get(url)

if response.status_code == 200:
    # Parsing the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Finding and extracting the quotes
    quotes = soup.find_all("span", class_="text")

    # Saving the quotes
    with open(file_name, "w") as file:
        for quote in quotes:
            file.write(quote.get_text() + "\n")

    print("Scraped quotes are saved to quotes.txt")
else:
    print("Failed to retrieve the website")
    