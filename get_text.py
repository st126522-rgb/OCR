import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
extracted_urls = [
    # "https://ekantipur.com/news/2024/04/15/iran-attacks-israel-further-tensions-in-west-asia-19-53.html",
    # "https://ekantipur.com/business/2024/04/15/army-in-charge-of-road-construction-sometimes-slow-sometimes-fast-12-06.html",
    # "https://ekantipur.com/news/2024/04/15/a-coup-in-the-far-west-shakes-the-ruling-coalition-43-03.html",
    # "https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%95%E0%A4%B8_%E0%A4%B8%E0%A4%BF%E0%A4%9F%E0%A5%80_%E0%A4%B9%E0%A4%B2%E0%A4%AE%E0%A4%BE_%E0%A4%86%E0%A4%95%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%A3#%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%A4%E0%A4%BF%E0%A4%95%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF%E0%A4%BE%E0%A4%B9%E0%A4%B0%E0%A5%82",
    # "https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B2%E0%A4%BE%E0%A4%B8%E0%A5%80%E0%A4%95%E0%A5%8B_%E0%A4%AF%E0%A5%81%E0%A4%A6%E0%A5%8D%E0%A4%A7",
    # "https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A4%BF%E0%A4%AE%E0%A5%8D%E0%A4%B0%E0%A5%8C%E0%A4%A8%E0%A4%97%E0%A4%A2_%E0%A4%A8%E0%A4%97%E0%A4%B0%E0%A4%AA%E0%A4%BE%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A4%BE",
    # "https://ne.wikipedia.org/wiki/%E0%A4%AD%E0%A5%80%E0%A4%AE%E0%A4%B8%E0%A5%87%E0%A4%A8_%E0%A4%A5%E0%A4%BE%E0%A4%AA%E0%A4%BE",
    # "https://ne.wikipedia.org/wiki/%E0%A4%AF%E0%A4%AD%E0%A4%97%E0%A5%87%E0%A4%A8%E0%A5%80_%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%97%E0%A5%8B%E0%A4%9C%E0%A4%BF%E0%A4%A8",
    # "https://ne.wikipedia.org/wiki/%E0%A4%AE%E0%A4%BE%E0%A4%9B%E0%A4%BE%E0%A4%AA%E0%A5%81%E0%A4%9A%E0%A5%8D%E0%A4%9B%E0%A5%8D%E0%A4%B0%E0%A5%87_%E0%A4%B9%E0%A4%BF%E0%A4%AE%E0%A4%BE%E0%A4%B2",
    # "https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A4%B6%E0%A5%8D%E0%A4%AF%E0%A4%AA_%E0%A4%8B%E0%A4%B7%E0%A4%BF",
    # "https://ne.wikipedia.org/wiki/%E0%A4%AC%E0%A4%BE%E0%A4%B2%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3_%E0%A4%B8%E0%A4%AE",
    # "https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A4%9A%E0%A4%A8%E0%A4%95%E0%A4%B5%E0%A4%B2_%E0%A4%97%E0%A4%BE%E0%A4%89%E0%A4%81%E0%A4%AA%E0%A4%BE%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A4%BE",
    # "https://ne.wikipedia.org/wiki/%E0%A4%B6%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BF_%E0%A4%97%E0%A5%8C%E0%A4%9A%E0%A4%A8",
    # "https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A5%8C%E0%A4%B8%E0%A4%B2%E0%A5%8D%E0%A4%AF%E0%A4%BE",
    # "https://www.setopati.com/politics/327742",
    # "https://www.setopati.com/kinmel/economy/327713",
    # "https://www.setopati.com/kinmel/economy/327752",
    # "https://www.setopati.com/kinmel/economy/327749",
    # "https://www.setopati.com/kinmel/banking/327745",
    # "https://www.setopati.com/kinmel/banking/327737",
    # "https://www.setopati.com/art/bollywood/327726",
    # "https://www.setopati.com/art/art-activity/327732",
    # "https://www.setopati.com/art/gossip/304155",
    # "https://nagariknews.nagariknetwork.com/opinion/1433630-1713747834.html",
    # "https://ekantipur.com/opinion/2024/04/12/program-by-adding-the-post-of-public-representative-47-54.html",
    # "https://ekantipur.com/opinion/2024/04/12/responsible-for-the-restoration-of-democratic-civilization-51-55.html",
    # "https://ekantipur.com/opinion/2024/04/15/why-zero-rate-of-value-added-tax-15-05.html",
    # "https://ekantipur.com/opinion/2024/04/15/state-apolitics-attack-on-federalism-11-16.html",
    # "https://ekantipur.com/opinion/2024/04/16/not-only-tunnels-but-all-infrastructure-barriers-should-be-cleared-18-35.html",
    # "https://ekantipur.com/opinion/2024/04/16/prevention-of-human-wildlife-conflict-24-01.html",
    # "https://ekantipur.com/opinion/2024/04/16/neighborhood-as-a-foreign-policy-priority-21-46.html",
    # "https://ekantipur.com/opinion/2024/04/16/a-unique-opportunity-to-collaborate-33-14.html",
    # "https://ekantipur.com/opinion/2024/04/17/structural-stagnation-in-agriculture-00-43.html",
    # "https://ekantipur.com/opinion/2024/04/17/open-the-land-of-ravi-lamichhane-06-09.html",
    # "https://ekantipur.com/opinion/2024/04/17/the-ritual-of-investment-attraction-03-15.html",
    # "https://ekantipur.com/opinion/2024/04/18/student-retention-is-more-important-than-enrollment-45-34.html",
    # "https://ekantipur.com/opinion/2024/04/18/how-to-protect-children-from-addiction-52-03.html",
    # "https://ekantipur.com/opinion/2024/04/18/a-vote-of-confidence-in-the-province-47-36.html",
    # "https://ekantipur.com/opinion/2024/04/18/other-commission-empowerment-formula-50-52.html",
    # "https://ekantipur.com/opinion/2024/04/19/one-third-female-participation-is-not-a-complete-achievement-28-48.html",
    # "https://ekantipur.com/opinion/2024/04/19/now-promoting-digital-entrepreneurship-40-31.html",
    # "https://ekantipur.com/opinion/2024/04/19/the-maze-of-land-reform-49-53.html",
    # "https://ekantipur.com/opinion/2024/04/21/women-forced-to-move-from-chhaugoth-to-tripal-and-odhar-20-55.html",
    # "https://ekantipur.com/opinion/2024/04/22/empty-cold-storage-built-on-a-budget-37-20.html",
    # "https://ekantipur.com/opinion/2024/04/22/communists-kantabijog-35-29.html",
    # "https://ekantipur.com/news/2024/04/22/the-supreme-court-did-not-issue-an-interim-order-on-the-government-of-sudurpaschim-province-12-34.html",
    # "https://ekantipur.com/news/2024/04/22/a-public-holiday-in-honor-of-the-qatari-king-07-25.html",
    # "https://ekantipur.com/business/2024/04/22/demand-15-days-time-to-set-up-a-processing-center-in-the-industry-36-52.html"
    # "https://ekantipur.com/blog/2023/11/23/a-trip-to-ramidanda-the-epicenter-hit-by-the-earthquake-44-47.html",
    # "https://ekantipur.com/blog/2024/03/03/blog-editing-continued-amazing-experience-with-atma-dai-48-37.html"
    # "https://www.onlinekhabar.com/2024/04/1468260",
    # "https://www.onlinekhabar.com/2024/04/1468148",
    # "https://www.onlinekhabar.com/2024/04/1468256",
    # "https://www.onlinekhabar.com/2024/04/1464169",
    # "https://www.onlinekhabar.com/2023/12/1413182",
    # "https://www.onlinekhabar.com/2024/04/1468148#",
    # "https://www.onlinekhabar.com/2024/04/1468101",
    # "https://www.onlinekhabar.com/2024/04/1463356",
    # "https://www.onlinekhabar.com/2024/04/1468060",
    # "https://www.onlinekhabar.com/2024/04/1468135",
    # "https://www.onlinekhabar.com/2024/03/1455789",
    # "https://www.onlinekhabar.com/2023/12/1412447",
    # "https://www.onlinekhabar.com/2024/01/1423661",
    # "https://www.onlinekhabar.com/2024/04/1466580",
    # "https://www.onlinekhabar.com/2023/09/1372430",
    # "https://www.newshousenepal.com/post/20230907180311",
    # "https://gorkhapatraonline.com/news/73665",
    # "https://www.enepalese.com/2023/07/396130.html/",
    # "https://www.bikashnews.com/2023/06/04/415329.html",
    # "https://annapurnapost.com/news/vishwatarang-of-om-224847/",
    # "https://www.edukhabar.com/news/15793"
    

]

# Create an empty list to store the scraped data
def web_scrape(urls):
    collected_paragraphs = []
    # Iterate over the URLs
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)
        response.encoding = 'utf-8'  # Set the encoding explicitly

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the desired data from the HTML
        # For example, let's extract all the paragraphs of text
        paragraphs = soup.find_all("p")

        # Append the paragraphs to the data list
        for paragraph in paragraphs:
            collected_paragraphs.append(paragraph.get_text())
    return collected_paragraphs

def get_urls(url_txt_file_path):
    with open(url_txt_file_path,"r",encoding="utf-8") as url_file_data:
        pdf_line_data=url_file_data.readlines()
        return pdf_line_data


def get_pdf_text(pdf_path):
    with open(pdf_path,"r",encoding="utf-8") as pdf_file_data:
        pdf_line_data=pdf_file_data.readlines()
        return pdf_line_data


def format_content(input_list):
    min_char_per_line = 40
    grouped_words = []
    line = ""
    for text in input_list:
        words = text.split()
        
        for word in words:
            # Check if adding the current word to the line exceeds the minimum length
            if len(line) >= min_char_per_line:
                grouped_words.append(line.strip())  # Append the completed line to the list
                line = word  # Start a new line with the current word
            else:
                # Add the current word to the line
                if line:
                    line += " " + word
                else:
                    line = word
    # Write the scraped data to a file
    with open("raw_webscraped_text.txt", "a", encoding="utf-8") as file:
        for item in grouped_words:
            file.write(item + "\n")
        

if __name__=="__main__":
    total_content=[]
    targeted_urls= [url.strip() for url in get_urls(r"txt_files\links.txt")]
    total_content.extend(get_pdf_text(r'txt_files\pdf_extract.txt'))
    total_content.extend(web_scrape(targeted_urls))
    format_content(total_content)

    
