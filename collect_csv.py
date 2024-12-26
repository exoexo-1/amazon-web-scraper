from bs4 import BeautifulSoup
import os
import pandas as pd
# Directory containing HTML files
directory = "data"
d={'title':[],'price':[],'link':[]}

for file in os.listdir(directory):
    if file.endswith(".html") or file.endswith(".htm"):  # Ensure only HTML files are processed
        with open(f"{directory}/{file}", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, features="html.parser")

        # Extract title and link
        h2_tag = soup.find("h2")
        if h2_tag:
            title = h2_tag.get_text(strip=True)  # Clean up title
            a_tag = h2_tag.find("a")
            if a_tag and 'href' in a_tag.attrs:
                link = "https://www.amazon.com" + a_tag['href']  # Construct full URL
            else:
                # Attempt fallback search for link within the same container
                a_tag_fallback = soup.find("a", href=True)
                link = "https://www.amazon.com" + a_tag_fallback['href'] if a_tag_fallback else "No link found"
        else:
            title = "No title found"
            link = "No link found"

        # Extract price
        price_tag = soup.find("span", class_="a-price-whole")
        if price_tag:
            price = price_tag.get_text(strip=True)
        else:
            price = "No price found"

        # Print extracted data
        print(f"Title: {title}\nPrice: {price}\nLink: {link}\n")
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)

df = pd.DataFrame(data=d)
df.to_csv("data.csv")

