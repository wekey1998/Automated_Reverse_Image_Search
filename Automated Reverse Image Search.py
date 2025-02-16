#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load the DataFrame from the Excel file
input_file = "your_input_file.xlsx"  # Replace with actual input file path
output_file = "your_output_file.xlsx"  # Replace with actual output file path

df = pd.read_excel(input_file)

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--force-device-scale-factor=0.8")  # Zoom level set to 80%

# Set geolocation to Washington, US (latitude: 47.6062, longitude: -122.3321)
chrome_options.add_argument("--enable-geolocation")
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--use-fake-ui-for-media-stream")

# Set the geolocation preference
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 1
})

# Set up the ChromeDriver with the configured options
service = Service(executable_path="path_to_chromedriver")  # Replace with actual path

driver = webdriver.Chrome(service=service, options=chrome_options)
updated_rows = []

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    try:
        image_url = row['image_url']
        base_url = row['base_url']
        brand_name = row['brand_name']
        print(f"Processing Image URL: {image_url}... ({index + 1}/{len(df)})")

        driver.get("https://www.google.com/imghp")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@jscontroller='lpsUAf']"))
        ).click()

        paste_image_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Paste image link']"))
        )
        paste_image_input.send_keys(image_url)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='Qwbd3' and @jsname='ZtOxCb']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='WF9wo']"))
        ).click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Exact matches')]"))
        )

        product_links = driver.find_elements(By.XPATH, "//a[@href]")
        title_match_urls, url_match_urls = [], []

        for link in product_links:
            url = link.get_attribute("href")
            title = link.get_attribute("aria-label")
            if title and brand_name.lower() in title.lower():
                title_match_urls.append(url)
            if base_url.lower() in url.lower():
                url_match_urls.append(url)

        for match_url in url_match_urls:
            updated_rows.append({'image_url': image_url, 'url_match': match_url, 'title_match': '', 'title': title})
        for match_url in title_match_urls:
            updated_rows.append({'image_url': image_url, 'url_match': '', 'title_match': match_url, 'title': title})

    except Exception as e:
        print(f"Error processing {image_url}: {e}")
        continue

updated_df = pd.DataFrame(updated_rows)
updated_df.to_excel(output_file, index=False)
driver.quit()
print("Processing completed. Results saved to:", output_file)


