import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

# Define the URL of the website
url = "https://wolt.com/fi/fin/jarvenpaa/restaurant/sapporo-sushi?srsltid=AfmBOopI2jAjpMWZ4R0a_sU0Z5hDdxCh8pwBVaL1Ob09lf-9gpSYkrIk"

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the last component of the URL path
url_path = urlparse(url).path
folder_name = url_path.rstrip('/').split('/')[-1]

# Create the folder based on the path
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Find all divs with the specified class that contain the menu items
menu_item_divs = soup.find_all('div', class_='sc-d1b749f8-0 logstQ cb-elevated cb_elevation_elevationXsmall_equ2')

# Function to sanitize a string for use in filenames
def sanitize_filename(text):
    return re.sub(r'[\\/:"*?<>|]', '', text)

# Download and save images with sanitized heading names as filenames
for item_div in menu_item_divs:
    heading_tag = item_div.find('h3', {'data-test-id': 'horizontal-item-card-header'})
    img_tag = item_div.find('img')

    if heading_tag and img_tag:
        img_url = img_tag.get('src')

        # Construct absolute URL
        img_url = urljoin(url, img_url)

        # Get the image content
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            # Extract the sanitized image file name from the heading text
            heading_text = heading_tag.get_text(strip=True)
            sanitized_filename = sanitize_filename(heading_text)
            img_filename = f"{sanitized_filename}.jpg"  # Assuming the images are JPEGs

            # Save the image to the folder
            with open(os.path.join(folder_name, img_filename), "wb") as img_file:
                img_file.write(img_response.content)
            print(f"Downloaded: {img_filename}")
        else:
            print(f"Failed to download: {img_url}")
    else:
        print("Heading or image not found in menu item.")

print("Image extraction completed.")
