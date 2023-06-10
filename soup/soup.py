
# Pola Parol
# 419325

import requests
from bs4 import BeautifulSoup as BS
import re
import pandas as pd
import time

# starting measuring time
start_time = time.time()

# Setting limit_pages = True, 100 pages will be scraped
limit_pages = True 

# setting url to libristo page 
url = 'https://www.libristo.pl/books-in-english/humanities.html'
saved_pages = []
counter = 0

# Check if the limit_pages parameter is True
if limit_pages is True:
    while counter < 101:  
        response = requests.get(url)
        bs = BS(response.text, 'html.parser')
        saved_pages.append(url) # adding links to saved_pages list
        link = bs.find('a', href=re.compile('/books-in-english/humanities*'))

        if link is None: 
            print("end")
            break

        next_url = link['href']
        url = 'https://www.libristo.pl' + next_url # creating 100 links for 100 pages 
        counter += 1 # incrementing number of created links to pages

# If limit_pages is False, scrape all pages until no more links are found
else: 
    response = requests.get(url)
    bs = BS(response.text, 'html.parser')
    saved_pages.append(url)
    link = bs.find('a', href=re.compile('/books-in-english/humanities*'))

    while link is not None:
        next_url = link['href']
        url = 'https://www.libristo.pl' + next_url 
        response = requests.get(url)
        bs = BS(response.text, 'html.parser')
        saved_pages.append(url)
        link = bs.find('a', href=re.compile('/books-in-english/humanities*'))

# creating a list for saving books' information
books_data = []

# Scraping book information from each saved page
for link in saved_pages:
    book_response = requests.get(link)
    book_bs = BS(book_response.text, 'html.parser')
    
    book_list = book_bs.find('ol', class_='LST')
    books = book_list.find_all('li')
    
    # Extracting for each book its details
    for book in books:
        try:
            title = book.find('h3').text.strip()
        except:
            title = ''

        try:
            author_info = book.find('h4').text.strip()
            author = author_info.split('|')[0].strip()
        except:
            author = ''

        try:
            year_info = book.find('h4').text.strip()
            year_match = re.search(r'\b\d{4}\b', year_info)
            if year_match:
                Year = year_match.group()
            else:
                Year = ' '
        except:
            Year = ''

        try:
            strong_tag = book.find('strong', string='Language')
            language = strong_tag.find_next_sibling(text=True).strip()
            if language:
                Language = language.strip(': ')
            else:
                Language = ''
        except:
            Language = ''

        try:
            strong_tag = book.find('strong', string='Binding')
            cover = strong_tag.find_next_sibling(text=True).strip()
            if cover:
                Cover_type = cover.strip(': ')
            else:
                Cover_type = ''
        except:
            Cover_type = ''
        
        try:
            link_tag = book.find('a', href=re.compile('/book/.*'))
            try:
                Link = 'https://www.libristo.pl' + link_tag['href']
            except:
                Link = ''
        except:
            Link = ''
        
        try:
            buy_div = book.find('div', class_='LST_buy')
            Price = buy_div.find('p').strong.text.strip()
        except:
            Price = ''

        try:
            discount_div = book.find('div', text=re.compile('Sale.*'))
            discount_all = discount_div.text.strip()
            discount_percentages = re.findall(r'\b(\d+)\b', discount_all)
            Discount = discount_percentages[0] if discount_percentages else '0'
        except:
            Discount = '0'
         
        # Adding book data 
        books_data.append({'Title': title, 'Author': author, 'Year': Year, 'Language': Language, 'CoverType': Cover_type, 'BookLink': Link, 'Price': Price, 'Disc': Discount})

# Creating a DataFrame and saving it to a CSV file
df = pd.DataFrame(books_data)
df.to_csv('book.csv')

# calculating execution time 
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")