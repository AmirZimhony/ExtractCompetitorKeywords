from Include import FindAllPages,FindKeywords
import xlsxwriter
import time
import requests
from bs4 import BeautifulSoup

#getting the Homepage of the Website we are scraping aka the name of our competitor
base_site = input("Please enter the Homepage of the website we are scraping").strip()
while base_site[0:8]!='https://':
    base_site = input("Incorrect input, Please enter a legitimate webpage").strip()


#setting up the xlsx worksheet, and description of each row
workbook = xlsxwriter.Workbook('ExtractedKeywords.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,'Site')
worksheet.write(1,0,'Title')
worksheet.write(2,0,'H1')
worksheet.write(3,0,'H2s')
worksheet.write(4,0,'H3s')
worksheet.write(5,0,'MetaDescription')
worksheet.write(6,0,'MetaKeywords')
worksheet.write(7,0,'imgList')
worksheet.write(8,0,'TenWords')


#getting links of pages we are about to scan for their keywords
names_of_sites = []
URL = "null"
j=0
insertion_cmd = "Please enter the URLs of the webpages containing the information we want to extract and press 'Enter' between each URL, upon completion please enter 'x':"
URL = input(insertion_cmd).strip()
print(URL)
while URL != 'x' and URL != 'X':
    names_of_sites.insert(j,URL)
    j+=1
    URL = input(insertion_cmd).strip()

#create the list of all pages we want to extract keywords from -> links
links = [None]*len(names_of_sites)
RealLinks = []#RealLinks now truly contains all the links of pages we want to extract info from
for i in range(len(names_of_sites)):
    links[i] = FindAllPages.GetLinks(names_of_sites[i],base_site,i)
    for link in links[i]:
        RealLinks.append(link)



i = 1
for link in RealLinks:
    list = FindKeywords.returnKeywords(link)
    worksheet.write(0,i,link)
    worksheet.write(1, i, str(list[0]))
    worksheet.write(2, i, str(list[1]))
    worksheet.write(3, i, str(list[2]))
    worksheet.write(4, i, str(list[3]))
    worksheet.write(5, i, str(list[4]))
    worksheet.write(6, i, str(list[5]))
    worksheet.write(7, i, str(list[6]))
    worksheet.write(8, i, str(list[7]))
    i = i+1
    time.sleep(0.5)
workbook.close()