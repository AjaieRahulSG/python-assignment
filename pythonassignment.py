
import requests
from bs4 import BeautifulSoup
import csv

# the URL of the first page
url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

# initialize a CSV file for storing the scraped information
with open('product.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # write the header row
    writer.writerow(["Product URL", "Product Name", "Product Price", "Rating", "Number of Reviews"])
    
    # iterate through the pages
    page_number = 1
    while page_number <= 20:
        # send a request to the website and get the HTML content
        response = requests.get(url)
        html_content = response.content
        
        # parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # find all the products on the page
        products = soup.find_all("div", {"data-index": True})
        
        # iterate through the products and extract the required information
        for product in products:
    # extract the product URL
            product_url_element = product.find("a", {"class": "a-link-normal"})
            if product_url_element:
                product_url = product_url_element["href"]
            else:
                product_url = None

            # extract the product name
            product_name_element = product.find("span", {"class": "a-size-medium"})
            if product_name_element:
                product_name = product_name_element.text
            else:
                product_name = None

            # extract the product price
            product_price_element = product.find("span", {"class": "a-price-whole"})
            if product_price_element:
                product_price = product_price_element.text
            else:
                product_price = None

            # extract the rating
            product_rating_element = product.find("span", {"class": "a-icon-alt"})
            if product_rating_element:
                product_rating = product_rating_element.text
            else:
                product_rating = None

            # extract the number of reviews
            product_reviews_element = product.find("span", {"class": "a-size-base"})
            if product_reviews_element:
                product_reviews = product_reviews_element.text
            else:
                product_reviews = None

            # print the information
            print("Product URL:", product_url)
            print("Product Name:", product_name)
            print("Product Price:", product_price)
            print("Rating:", product_rating)
            print("Number of Reviews:", product_reviews)

            # write the information to the CSV file
            writer.writerow([product_url, product_name, product_price, product_rating, product_reviews])
        
        # increment the page number
        page_number += 1
        
        # update the URL for the next page
        url = f"https://www.amazon.in/s?k=bags&page={page_number}&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{page_number}"


