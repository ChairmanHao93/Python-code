from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Disable auto-close by using the detach option
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # This keeps the browser open after the script finishes

# Path to the Telia website
website = 'https://www.telia.fi/kauppa/puhelimet/puhelimet'

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=options)

# Open the website
driver.get(website)

# Wait for the cookie consent button to become clickable and click it
wait = WebDriverWait(driver, 20)  # Increased wait time for better handling of slow loads
cookie_consent_button = wait.until(
    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
)
cookie_consent_button.click()

# Wait for the popup close button to become clickable and close it
try:
    close_popup_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='sc-8039b9c2-0 cmXsjQ']"))
    )
    close_popup_button.click()
except Exception as e:
    print(f"Popup close button not found or unable to click: {e}")

# Wait for the page to load completely
time.sleep(3)

# Locate all the <li> elements with the given data-gtm-id
product_cards = driver.find_elements(By.XPATH, "//li[@data-gtm-id='ecom-category:div:product-card']")

# Prepare lists for storing names and prices
data = []

# Iterate over each product card to extract device names and prices
for product in product_cards:
    try:
        # Find the device name inside the product card
        device_name = product.find_element(By.XPATH, ".//h1[contains(@class, 'sc-42c5f186-3 kCGoqU')]").text
        # Find the price inside the product card
        price = product.find_element(By.XPATH, ".//div[contains(@class, 'sc-bec48294-1 gvuTRc')]").text
        # Append the extracted data to the list
        data.append([device_name, price])
    except Exception as e:
        print(f"Error while extracting data from product: {e}")

# Export the data to a CSV file
csv_file_path = "telia_devices.csv"
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Device Name", "Price"])  # Write header
    writer.writerows(data)

print(f"Data successfully written to {csv_file_path}")

# The browser will remain open after the script finishes because of the detach option
