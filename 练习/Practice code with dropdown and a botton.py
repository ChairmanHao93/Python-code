from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Disable auto-close by using the detach option
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # This keeps the browser open after the script finishes

# Path to the website you want to visit
website = 'https://www.adamchoi.co.uk/overs/detailed'

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=options)

# Open the website
driver.get(website)

# Wait for the "All matches" button to become clickable
wait = WebDriverWait(driver, 10)
all_matches_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='All matches']"))
)

# Click the "All matches" button
all_matches_button.click()

# Wait for the country dropdown to become visible
country_dropdown = wait.until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='country']"))
)

# Select "Spain" from the dropdown
select_country = Select(country_dropdown)
select_country.select_by_visible_text("Spain")

# Wait for the table to load (adjust the time if necessary)
time.sleep(3)  # This pause ensures that the table data has fully loaded

# Locate all the data in the <td> tags
table_data = driver.find_elements(By.TAG_NAME, "td")

# Print the content of each <td> element
for td in table_data:
    print(td.text)

# The browser will remain open after the script finishes because of the detach option
