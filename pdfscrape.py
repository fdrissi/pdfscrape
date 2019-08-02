#!/usr/bin/python
# modules we're using (you'll need to download lxml)
import lxml.html, urllib2, urlparse, os, requests

filename = raw_input("File: ") 

#If there is no such folder, the script will create one automatically
folder_location = r'/Users/fdrissi-/Desktop/scrp/scrappedfilestest' #this is the location where you want to save the downloaded pdfs
if not os.path.exists(folder_location):os.mkdir(folder_location) #and this check if the folder doesnt exists and create it

pdflinks = [] #this is and array i put all the downloaded pdf links in it to save them all in a file when finishing all the work

with open(filename) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

i = 1
j = 1
# the url of the page you want to scrape
for cont in content:
    # the url of the page you want to scrape
    base_url = cont
    print 'Link number: ', i, '/', len(content)

    if base_url.find('.pdf') > -1:
        pdflinks.append(base_url)
        print 'Downloading pdf: ', j
        #Name the pdf files using the last portion of each link which are unique in this case
        fname = os.path.join(folder_location,base_url.split('/')[-1])
        with open(fname, 'wb') as f:
            try:
                f.write(requests.get(base_url).content)
            except Exception as e:
                print str(e)
        f.close()
        j += 1
    else:
        # fetch the page
        res = urllib2.urlopen(base_url)

        # parse the response into an xml tree
        try:
            tree = lxml.html.fromstring(res.read())
        except Exception as e:
            print str(e)

        # construct a namespace dictionary to pass to the xpath() call
        # this lets us use regular expressions in the xpath
        ns = {'re': 'http://exslt.org/regular-expressions'}

        # iterate over all <a> tags whose href ends in ".pdf" (case-insensitive)
        for node in tree.xpath('//a[re:test(@href, "\.pdf$", "i")]', namespaces=ns):
            # print the href, joining it to the base_url
            pdflinks.append(urlparse.urljoin(base_url, node.attrib['href']))
            print 'Downloading pdf: ', j
            #Name the pdf files using the last portion of each link which are unique in this case
            fname = os.path.join(folder_location,urlparse.urljoin(base_url, node.attrib['href']).split('/')[-1])
            with open(fname, 'wb') as f:
                try:
                    f.write(requests.get(urlparse.urljoin(urlparse.urljoin(base_url, node.attrib['href']), node.attrib['href'])).content)
                except Exception as e:
                    print str(e)
            f.close()
            j += 1
    i += 1

fname = os.path.join(folder_location,'pdflinks') #here i save all the pdf links in a file 
with open(fname, 'w') as f:
    for item in pdflinks:
        print >> f, item