# amazon-web-scraper

This mini-project involves web scraping using Selenium and BeautifulSoup to collect product data from Amazon. The project is designed to extract product titles, prices, and links from Amazon search results pages and save the data in CSV format for further analysis.

Features
Selenium: Used to navigate Amazon pages and extract product information by interacting with web elements.
BeautifulSoup: Used to parse HTML content and extract relevant product details.
Pandas: Used to store and save the extracted data in CSV format.
CSV Output: The collected product data (title, price, and link) is saved in a CSV file for further use.
Files
collect_csv.py:

This script processes all HTML files stored in the data/ directory and extracts product titles, prices, and links from them. The data is then saved to a CSV file (data.csv).
fetching_query.py:

This script uses Selenium to search for products (e.g., "laptop") on Amazon and fetches multiple pages of search results. The HTML of each result page is saved as individual files in the data/ directory.
locating_multiple.py:

This script uses Selenium to locate and print the details of multiple products on Amazon search results pages. It performs a search query and iterates through pages to extract product information.
Sample HTML Extraction:

The script also demonstrates how to extract the outerHTML of specific elements (e.g., product containers) and save them for later parsing.
Requirements
Python 3.x
Selenium: pip install selenium
BeautifulSoup: pip install beautifulsoup4
Pandas: pip install pandas
WebDriver Manager: pip install webdriver-manager
Setup Instructions
Install dependencies:

Install the necessary Python libraries by running the following command in your terminal:
bash
Copy code
pip install selenium beautifulsoup4 pandas webdriver-manager
Run the Scripts:

Use the following commands to execute the scripts:
Run fetching_query.py to scrape product pages from Amazon based on the given search query.
Run collect_csv.py to extract information from the saved HTML files and generate a CSV file.
Run locating_multiple.py to locate multiple product elements and print their details.
Data Folder:

The scripts will save the HTML files into the data/ directory. Make sure this directory exists before running the scripts, or modify the script to create the folder automatically.
CSV Output:

After running collect_csv.py, a data.csv file will be generated in the project directory containing the product details. 
