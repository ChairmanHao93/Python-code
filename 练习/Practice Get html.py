import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.espoo.fi/en/childcare-and-education/early-childhood-education/evaka-e-service-early-childhood-education'

# Send a request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the entire HTML code of the webpage
    html_code = soup.prettify()

    # Output the HTML code or save it to a file
    print(html_code)
    # To save it to a file, uncomment the following lines:
    # with open("website_html.html", "w", encoding="utf-8") as file:
    #     file.write(html_code)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
