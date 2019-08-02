# pdfscrape
A python script to fetch pages, download contained pdf files

# Usage:

line 8: folder_location = r'/Users/fdrissi-/Desktop/scrp/scrappedfilestest'

change the path of the folder that you want to save the output in it.

python2 pdfscrap.py

it will prompt you to add the file containing the list of URLs (html, pdf), it the link is a pdf file, it will download it automatically, otherwise, it will fetch the page, gather all the pdf links inside it, download them.
finally, it will save all the pdf links.
