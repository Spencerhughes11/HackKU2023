from selenium import webdriver

# Generate a list of strings
my_list = ["string1", "string2", "string3"]

# Initialize a new WebDriver instance
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://deepai.org/machine-learning-model/text2img")

# Find the text field where the strings will be input
text_field = driver.find_element_by_id("my-text-field")

# Enter the strings into the text field, separated by commas
text_field.send_keys(", ".join(my_list))

# Submit the form, if necessary
submit_button = driver.find_element_by_id("submit-button")
submit_button.click()

# Close the WebDriver instance
driver.quit()


import requests
from bs4 import BeautifulSoup

# URL of the website containing the image
url = "https://example.com"

# Send a request to the website and parse the HTML using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the image on the website and extract its URL
image = soup.find("img", {"class": "my-image"})
image_url = image["src"]

# Download the image and save it to a file
response = requests.get(image_url)
with open("image.jpg", "wb") as f:
    f.write(response.content)
