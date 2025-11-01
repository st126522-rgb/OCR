import requests
import re
from bs4 import BeautifulSoup
def web_scrape(urls):
    collected_td = []
    # Iterate over the URLs
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)
        response.encoding = 'utf-8'  # Set the encoding explicitly

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the desired data from the HTML
        # For example, let's extract all the paragraphs of text
        tables = soup.find_all("td")

        # Append the paragraphs to the data list
        for table_data in tables:
            collected_td.append(table_data.get_text())
    return collected_td

urls=[r'https://www.learnentry.com/english-nepali/1000-most-common-nepali-words/',r'https://nepali.imnepal.com/learn-nepali-words/']
td_values=web_scrape(urls)
def remove_non_dev(line):
    pattern = r'[^\u0900-\u097F,?\s]'  # Define a pattern to remove non-Devanagari characters and whitespace
    data_line = re.sub(pattern, ' ', line.strip())   
    return data_line 
td_values=[remove_non_dev(td) for td in td_values]
print(len(td_values))