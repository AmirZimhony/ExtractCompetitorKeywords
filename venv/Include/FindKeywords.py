import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import heapq
import difflib

#helper function for removing all occurences of an item from a list, will come in hand when we will filter out certain words from a string
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


#helper function for extracting second element of tuple
def take_second(elem):
    return elem[1]

#function for computing 10 most common words in text
def findTenFreqWords(text):
    text = text.split()#convert string to list
    blackList = ['של','עם','על','את']#Subjective part of code, words to filter out should differ between projects
    for word in blackList:
        text = remove_values_from_list(text,word)
    textDict = dict.fromkeys(text)#convert list to dictionary (and keep only 1 occurrence of each word)
    for word in textDict:
        textDict[word] = text.count(word)#create pairs of '(word, word occurence)' in dictionary
    WordList = [(k,v) for k,v in textDict.items()]#create tuples from dictionary
    sortedList = sorted(WordList,key= take_second)#create sorted list from tuples
    return (sortedList[-10:])#return 10 last items of sorted list i.e. 10 most common words in string)




#extract the keywords based on the  Title, H1 and meta description of the page
def returnKeywords(link):
    #----------make request---------
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    response = requests.get(link, headers=headers)
    html = response.content
    bsElement = BeautifulSoup(html, "html.parser")
    with open('{}.html'.format(str(link)[8:1]), 'wb') as file:
        file.write(bsElement.prettify('utf-8'))
    #-----------extract SEO-relevant information from tags on page-------------
    title = bsElement.title
    if title == None:
        title = 'none'
    else:
        title = title.text
    h1 = bsElement.h1
    if h1 == None:
        h1 = 'none'
    else:
        h1 = h1.text
    H2s = bsElement.find_all("h2")
    H2sTexts = []
    if H2s != None:
        for h in H2s:
            H2sTexts.append(h.text)
    H3s = bsElement.find_all("h3")
    H3sTexts = []
    if H3s != None:
        for h in H3s:
            H3sTexts.append(h.text)
    metaDes = bsElement.find('meta', {'name': 'description', })
    if metaDes == None:
        metaDes = 'none'
    else:
        metaDes = metaDes.get('content')
    metaKeyWords = bsElement.find('meta', {'name': 'keywords', })
    if metaKeyWords == None:
        metaKeyWords = 'none'
    else:
        metaKeyWords = metaKeyWords.get('content')
    All_texts = bsElement.find_all("p")
    texts = " "
    for p in All_texts:
        texts = texts + (str(p.text))
    texts = texts.strip("\n")
    imgs = bsElement.find_all("img")
    imgList = []
    for img in imgs:
        if 'alt' in img.attrs:  # make sure we scan only images that have an alt attribute
            if img['alt'] != "":  # scan only images that alt attribute for them isn't empty (avoid an index out of bounds error)
                if img['alt'][0] != '{':  # check that alt text is indeed text and not a parameter like "{{product.name}}"
                    imgList.append(str(img['alt']))
    imgList = list(dict.fromkeys(imgList))
    

    TitleList = title.split()
    DescriptionList = metaDes.split()
    H1List = h1.split()
    MetaKeywordsList = metaKeyWords.split()
    textsList = texts.split()
    print('The words constructing the title are: '+TitleList)
    #print(H1List)
    #print(DescriptionList)
    #print(MetaKeywordsList)
    print(texts)
    TenWords = findTenFreqWords(texts)
    H1Dict = dict.fromkeys(H1List)
    ListOfSEOElements = (title, h1, H2sTexts,H3sTexts, metaDes, metaKeyWords,imgList,TenWords)
    #---------compute the words most likely to be the keywords---------------
    for key in TitleList:
        H1Dict[key] = difflib.get_close_matches(key, TitleList)+difflib.get_close_matches(key, DescriptionList)+difflib.get_close_matches(key, textsList)+difflib.get_close_matches(key, imgList)+difflib.get_close_matches(key, texts)


    print([(k, H1Dict[k]) for k in H1Dict])
    return ListOfSEOElements






