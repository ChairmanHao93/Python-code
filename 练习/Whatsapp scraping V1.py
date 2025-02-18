from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Set up Selenium WebDriver with your path
service = Service(executable_path=r"C:\Users\zhang\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for WhatsApp Web to load and for you to scan the QR code
print("Please scan the QR code on WhatsApp Web")
WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Chats']"))
)


# Locate the chat to extract messages from
chat_name = "Janne My Friend"  # Replace with the exact name of the chat
chat = driver.find_element(By.XPATH, f"//span[@title='{chat_name}']")
chat.click()

# Wait for messages to load
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='xnpuxes copyable-area']"))
)
###class="xnpuxes copyable-area"
# Scrape messages from the chat
messages = []
message_elements = driver.find_elements(By.XPATH, "//div[@class='xnpuxes copyable-area']")
for message_element in message_elements:
    message = message_element.text
    messages.append(message)

# Scroll to load more messages if needed
# This part is optional, you can adjust the number of scrolls if needed
for _ in range(3):  # Adjust the number of scrolls
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", message_elements[-1])
    time.sleep(2)  # Wait for more messages to load
    message_elements = driver.find_elements(By.XPATH, "//div[@class='_3-8er selectable-text copyable-text']")
    for message_element in message_elements:
        message = message_element.text
        messages.append(message)

# Convert the messages list to a pandas DataFrame
df = pd.DataFrame(messages, columns=["Messages"])

# Save the extracted messages to an Excel file
df.to_excel("whatsapp_messages.xlsx", index=False)

# Close the browser after the extraction
driver.quit()
