# ExtractCompetitorKeywords
A project for finding the (organic) keywords competitor websites are promoting.

This project is about understanding the business strategy of companies. 
How exactly? By finding the organic keywords they atempt to be ranked for on Google i.e. appear in the top search results for queries including these keywords.
For this purpose I decided to focus on some well known meta tags that are known to be important for Search Engine Optimization (SEO), such as title, meta description, h1,
in addition to more sophisticated information like the 10 most common words in the text of a webpage. 

There are 3 components to this task: 

1.Finding all relevant pages on a company's website.

2.Extracting the technical data from the website's pages that are supposed to be ranked for keywords. 

3.Combining all the info to a file and printing the results.

There are parts of this code that are subjective, and might need to be modified if you try to run this code on different websites. For example - the HTML tag used for listing
the different pages of the website containing the information we desire. A quick inspection of the source code of the page including all of the relevant links should provide
us with the answer for this problem.
All subjective parts are noted in comments inside the code.

The final output of this project is a xlsx(excel) file, containing information extracted from web pages on the company's website: 

1.URL

2.Various data from SEO-relevant HTML tags

3.A list of the 10 most common words on each page, including the number of occurences of each word.

