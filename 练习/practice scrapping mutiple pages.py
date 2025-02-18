import requests
from bs4 import BeautifulSoup
import os

# Step 1: Fetch the main page with all movie links
base_url = "https://subslikescript.com/movies"
response = requests.get(base_url)
webpage = response.content

# Step 2: Parse the webpage using BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Step 3: Find the "scripts-list" <ul> and extract all <a href> links within it
scripts_list_section = soup.find("ul", class_="scripts-list")  # Locate the ul with class "scripts-list"
if scripts_list_section:
    movie_links = scripts_list_section.find_all("a", href=True)  # Find all <a> tags with href inside this section

    # Step 4: Loop through each movie link, fetch the script, and save it as a .txt file
    for link in movie_links:
        movie_url = "https://subslikescript.com" + link['href']  # Construct full URL
        try:
            # Fetch the movie's page content
            movie_response = requests.get(movie_url)
            movie_page = movie_response.content

            # Parse the movie page
            movie_soup = BeautifulSoup(movie_page, "html.parser")

            # Extract the movie title from <h1> tag
            title = movie_soup.find("h1").get_text(strip=True)

            # Extract the script content from <div class_="full-script"> tag
            script_content = movie_soup.find("div", class_="full-script")
            if script_content:
                script_text = script_content.get_text(strip=True, separator='\n\n')

                # Step 5: Save the script content to a .txt file with the movie title as filename
                file_name = f"{title}.txt"
                # Optionally, replace characters in title that are not valid in file names (e.g., slashes)
                file_name = file_name.replace("/", "-").replace("\\", "-").replace(":", "-")

                # Create a folder to store the scripts if needed
                if not os.path.exists("scripts"):
                    os.makedirs("scripts")

                file_path = os.path.join("scripts", file_name)

                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(script_text)
                
                print(f"Saved: {file_name}")
            else:
                print(f"No script found for {title}")
        
        except Exception as e:
            print(f"Error processing {movie_url}: {e}")

else:
    print("No scripts list found on the page.")
