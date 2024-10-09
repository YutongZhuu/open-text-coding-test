from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
driver = webdriver.Chrome()

# Open the webpage
URL = "https://www.microfocus.com/en-us/products?trial=true"
driver.get(URL)

driver.implicitly_wait(20)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

product_grid = soup.find('div', class_='products-grid')
grids = soup.find_all('div', class_='uk-card uk-card-hover uk-card-default uk-overflow-hidden uk-margin-large-bottom uk-position-relative')
res = []
for grid in grids:
    product_name = grid.find('div', class_='title').text.strip()
    starting_letter = product_name[0].upper()

    links = grid.find('div', class_ = 'cta-buttons uk-flex uk-flex-middle').find_all('a') # Assume all cards must have this field
    demo_url = ""
    free_trial_url = ""
    for button in links:
        if button.text == "Get free trial": # Assume there are only two types of texts
            free_trial_url = button.get("href")
        else:
            demo_url = button.get("href")

    footer = grid.find('div', class_ = "footer")
    community_url = ""
    support_url = ""

    if footer:
        links = [link.find('a') for link in footer.find_all('a')]
        for link in links:
            if not link:
                continue

            text = link.text
            if text == 'Community':
                community_url = link.get("href")
            elif text == 'Support':
               support_url = link.get("href")
    
    res.append({
        'name': product_name,
        'start_letter':starting_letter,
        'demo_url': demo_url,
        'free_trial_url': free_trial_url,
        'community_url': community_url,
        'support_url': support_url
    })

res = json.dumps(res)
print(res)