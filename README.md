# How to run scrappers | quick guide 
## 1. Beautiful Soup 
- download `soup` project folder
- install necessary libraries: requests, re, pandas, BeautifulSoup, time
- in `soup.py` the `page_limit` is set to True and the limited number of pages will be scraped (number can be edited as well), to scrap all the pages change `page_limit = False` 
- Run the code in Python3 interpreter: `python3 soup.py`
- code will generate `book.csv` output


## 2. Scrapy 
- download `libristo` scrapy project folder
- in `bookSpider.py` the `page_limit` is set to True and spider scraps 100 links: change the default in .__init__ constructor if the different number to be scrapped
- in bash, run command `scrapy crawl bookSpider`
- code will generate `book_data.csv` output

## 3. Selenium
- download the `selenium` project folder
- in `selenium_projects.py` change the `gecko_path` according to the gecko in the local computer
- run the code in Python3 interpreter : `python3 selenium_projects.py`
- the code will run and mozilla firefox will automatically appear to the pages of the website
- after scrapping, the code will generate `book.csv` as the output
