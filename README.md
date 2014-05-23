Crawling-Semi-Structured-Data
=============================

This repository consists of the project done as part of the course Web Mining- Monsoon 2013. The course was instructed by [Dr. Manish Gupta](http://research.microsoft.com/en-us/people/gmanish/)

##Requirements
Python 2.6 or higher with beautiful soup (bs4)

##Problem

Web Pages for different businesses from the same website. Each webpage is an HTML containing details about the business. It does not have the email id, but it has the website address for the business which can be used to find the contact us page for the website and thereby extract its email id. The goal is to extract business id (i.e., the file name for the business), business name, business phone number, business home page URL, contact-us URL for the business, email id for the business.

The extraction of the above details is done in two steps:

Step 1:  
In this step the business id (i.e., the file name for the business), business name, business home page URL, business phone number is extracted and stored in a file named extractedUrl.txt.This step requires the input as a folder named "Dataset" containing the html files named as "business<unique id>"" 

Run the file:  
extractUrl.py

Step 2:  
In this step contact-us URL for the business and the email id for the business is extracted and the final file satisfying the given goal is stored as result.txt.This step takes as input the file generated in the previous step.

Run the file:  
findContact.py

###HEURISTICS 

####FOR FINDING CONTACT PAGE:

After obtaining the homepage, I try to search the url for the contact page. This is done by first extracting the anchor tags from the web page as the url can only be present in the anchor tag.

Now we search in the anchor tag in the following steps:  
Extract the href value from the anchor tag and find the word contact using the regular expression "r'.*contact.*',re.IGNORECASE". If a search is found I pick the href value and break else move one step further and try to find the word contact in the text of the tag. This is because the url may not have the word contact in it and yet represent the url of the contact page. But the text should have the word contact. I check this by using the same regular expression. If the contact url is found I update accordingly.

####FOR FINDING EMAIL ID:

I obtain the Email Id's by either searching in the contact page or in the home page. If the contact page of the page exists, I extract that page. Next from the extracted wenpage, I try to match the regular expression "r'[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]+', re.IGNORECASE". If a match exists I do the updates and break else I go back to the home page and search for the same regular expression.
