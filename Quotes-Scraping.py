# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:05:43 2025

@author: njosp
"""

from bs4 import BeautifulSoup
import requests
import csv
import datetime


    #quote scraping
print("Scraping quotes, please wait...")    
site_data = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(site_data.text, "html.parser")

quotes = soup.find_all('span', class_= 'text')

authors = soup.find_all('small', class_= 'author')

# Get current date and time
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

#generate a unique file name with timestamp
filename = f"scraped_quotes_{timestamp}.csv"
    
    #opening csv file for writing.  
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    #write the header row
    writer.writerow(["QUOTES","AUTHOR"])
    
    
    # Write each quote and author
    for quote, author in zip(quotes, authors):
        writer.writerow([quote.get_text(), author.get_text()])

print(f"Quotes successfully saved to '{filename}'.")