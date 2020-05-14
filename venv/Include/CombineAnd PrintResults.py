from Include import FindAllPages


#getting the Homepage of the Website we are scraping aka the name of our competitor
base_site = input("Please enter the Homepage of the website we are scraping").strip()


#getting links of pages we are about to scan for their keywords
names_of_sites = []
URL = "null"
j=0
URL = input("Please enter the URLs of the webpages containing the information we want to extract and press 'Enter' between each URL, upon completion please enter 'x':").strip()
print(URL)
while URL != 'x':
    names_of_sites.insert(j,URL)
    j+=1
    URL = input("Please enter the URLs of the webpages containing the information we want to extract and press 'Enter' between each URL, upon completion please enter 'x':").strip()

links=[]
for i in range(len(names_of_sites)):
    links.append(FindAllPages.GetLinks(names_of_sites[i],base_site,i))
print(links)