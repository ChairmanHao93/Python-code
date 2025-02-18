import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage content
url = "https://subslikescript.com/movie/Fear_and_Loathing_in_Las_Vegas-120669"
response = requests.get(url)
webpage = response.content

# Step 2: Parse the webpage using BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Step 3: Extract the title from the <h1> tag
title = soup.find("h1").get_text(strip=True)

# Step 4: Extract the script from the <div class="full-script"> tag, I changed it to 2 line spacing
script_content = soup.find("div", class_="full-script").get_text(strip=True, separator='\n\n')

# Step 5: Save the extracted content to a .txt file with the title as filename
file_name = f"{title}.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(script_content)

print(f"Data saved as {file_name}")
