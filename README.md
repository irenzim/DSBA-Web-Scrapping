# How to run scrappers | quick guide 
## 1. Beautiful Soup 

## 2. Scrapy 
- download `libristo` scrapy project folder
- in `bookSpider.py` the `page_limit` is set to True and spider scraps 100 links: change the default in .__init__ constructor if the different number to be scrapped
- in bash, run command `scrapy crawl bookSpider`
- code will generate `book_data.csv` output

## 3. Selenium
- download 'Selenium' project folder
- in the file selenium_projects.py, change the gecko_path according to your own gecko in your own computer
- in your terminal, run the command 'python3 selenium_projects.py'
- code will generate 'book.csv' as the output from webscrapping
