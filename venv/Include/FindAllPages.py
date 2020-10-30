import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def GetLinks(name_of_site,base_site ,i):
    # Defining the url of the site we want to take the articles/pages from
    


    # Making a get request
    response = requests.get(name_of_site)
    response.status_code



    # Extracting the HTML
    html = response.content


    # Convert HTML to a BeautifulSoup object. This will allow us to parse out content from the HTML more easily.
    # Using the default parser as it is included in Python
    soup = BeautifulSoup(html, "html.parser")
    
    # Exporting the HTML to a file
    with open('solgar_articles.html', 'wb') as file:
        file.write(soup.prettify('utf-8'))

#-----------------------SUBJECTIVE PART OF CODE : Find all relevant pages, in this case they are part of <h3> elements ----------------------
    articles= soup.find_all('h3')#subjective part of code, the relevant pages might be found in 'h2' or other HTML tags in different cases
    print(len(articles))

    #In each <h3> element, extract the link to it's corresponding page and append it to a list
    importantLinks=[]
    for article in articles:
        if article.find('a')!= None:
            importantLinks.append(urljoin(str(base_site),str(article.find('a')['href'])))#we add the extracted text to the homepage's url, in order to make it a proper URL
            print(urljoin(base_site,article.find('a')['href']))

    #small trick to remove duplicates
    importantLinks = list(dict.fromkeys(importantLinks))
    return importantLinks