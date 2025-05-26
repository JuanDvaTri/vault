# Juan Rodriguez
# This script scrapes the BBC news website for headlines related to Ukraine.
import os
folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'headlines')
os.makedirs(folder, exist_ok=True) # creates a directory called 'headlines' if it doesn't already exist

import requests
from bs4 import BeautifulSoup
import time

requests.get('https://www.bbc.com/search?q=ukraine')            # this little block of code checks if the connection is succesful
if requests.get('https://www.bbc.com/search?q=ukraine').status_code == 200:
    print("Connection to BBC news successful!")
else:
    print("Failed to connect to BBC news. Please check your internet connection or the URL.")

# This for loop iterates through the first 6 pages of the BBC news search results for "ukraine"
for page_num in range(0,6):
    time.sleep(2) # to avoid overwhelming the server with requests

    r = requests.get(f'https://www.bbc.com/search?q=ukraine&page={page_num}') 
    # gets HTML content from the URL, iterating through the pages
    if r.status_code != 200:
        print(f'Failed to retrieve page {page_num}, status code: {r.status_code}')
        continue
    # If the request was not successful, it prints an error message and continues to the next iteration.
    soup = BeautifulSoup(r.text, 'html.parser')
    # I am using BeautifulSoup to parse the HTML content.

    headlines = soup.find_all('h2', attrs={'data-testid': 'card-headline'}) # finds all headlines with the specified attributes}

    file_path = os.path.join(folder, f'ukraine_bbc_headlines{page_num}.md')
    with open(file_path, 'w', encoding='utf-8') as file:  # opens a file to write the headlines
     for headline in headlines:      # the loop only prints headlines that contain the word "ukraine"
        text = headline.text
        if 'ukraine' in text.lower():
            file.write(f"## Found the following: {text}  \n\n")  # prints the headline text
        else:
            file.write(f"## No headlines found containing 'ukraine' on this page.  \n\n")


print("Scraping completed. Check the generated markdown files for the headlines.")
# This script scrapes the BBC news website for headlines related to Ukraine and saves them in markdown files.

# okay this shit works whatever





