import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

# Define the URL of the website we want to scrape
user_url = input("Enter the URL of the website you want to scrape: ")

# Ensuring the URL starts with 'http://' or 'https://
parsed_url = urlparse(user_url)
if not parsed_url.scheme:
    user_url = urlunparse(("http", user_url, "", "", "", ""))

# Let the user define the file name for a scraped data
file_name = input("Enter the name of the file to save the data: ")

# Ask user for the HTML element or atribute to scrape
element = input("Enter the element you want to scrape (like 'p', 'div', 'h1' etc.): ")
attribute = input("Enter the name ot the attribute you want o scrape (like 'class', 'id' etc.): ")

# Sending an HTTP GET request to the website
response = requests.get(user_url)

if response.status_code == 200:
    # Parsing the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Finding and extracting the quotes
    selected_elements = soup.find_all(element, class_=attribute)

    # Saving the quotes
    with open(file_name, "w") as file:
        for item in selected_elements:
            file.write(item.get_text() + "\n")

    print(f"Scraped quotes are saved to {file_name}")
else:
    print("Failed to retrieve the website")
    