# webscraping
HHA 507 // Week 7 // Assignment 7

## This repository focuses on the useful information gathering method known as webscraping, in which the user utilizes modules requests and Beautiful Soup 4 to systematically pull information from a website's html based on class attributes of specific elements containing text or other useful information to be gleaned.

## When vetting for sites to scrape from, there are a few important factors to consider. Firstly, does the site allow webscraping? Certain sites possess anti-scraping safeguards to prevent request traffic from creating latency. At times, even if a site does allow scraping, there may be a request limit imposed upon the user. Best practice is to not scrape unnecessarily.

## Secondly, the structure of the site's html must be considered. Some websites will have scrape-friendly formats, with neat nesting and arranged rows and tables. Others will have complicated structures with differing class names for every element. In this repo we have selected friendlier structures.

## It's important to employ trial and error when pulling desired data. To make a dataframe of information, all element lists must be the same length. In order to achieve such specificity, it's often routine to isolate the exact element which contains the text that we require. This can be achieved by right-clicking on the site's interface and selecting 'inspect' for Linux envrionments. The site's HTML will present itself and as the user hovers over element code, corresponding elements will be highlighted on the site's interface. In this manner, a user can track the element down to its exact text source.

## In some cases, the class used by the text source element may be used elsewhere in the html and generate extraneous information. In that case, it is recommended that the user zooms out one level and tries a different element class belonging to a different nest level. The recursive nature of webscraping can be clearly observed within the included py file.

## In cases where sites are not as friendly, the workaround may to be to save the site's html directly to the repo's directory (with the html only option rather than full site). Then, the user can define the soup with a variable that opens the html within the py file. Afterwards, the recursive element-combing process is relatively the same.

## All requirements and dependencies are included in requirements.txt, including requests and bs4.