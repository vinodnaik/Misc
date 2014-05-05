import urllib2
import sys
import string
from bs4 import BeautifulSoup
import re
import logging
import time
import os

def candidate_info(link,fh=None):
    logger=logging.getLogger(__name__)

    if not os.path.exists("logs"):
        os.makedirs("logs")

    if not fh:
        log_file='logs/candidate_info'+str(time.time()).split('.')[0]+'.log'
        fh=logging.FileHandler(log_file)

    logger.addHandler(fh)
    logger.propagate=False
    cand_info={}

    #code to open the link
    try:
        u=urllib2.urlopen(link)
    except Exception as e:
        logger.exception("Could not open %s",link)
        #logger.exception()
        return
    
    logger.info("Successfully opened %s",link)
    #Cook a soup
    soup=BeautifulSoup(u.read())

    table=None
    #Capture the html element infobox vcard which normally contains the candidate info
    try:
        table=soup.find('table',attrs={'class':'infobox vcard'}) or soup.find('table',attrs={'class':'infobox biography vcard'})
    except Exception as e:
        logger.exception("Could not find infobox vcard for %s",link)
        return

    logger.info("Successfully opened infobox vcard for %s",link)
    #code to capture the candidate name which is associated with the html element fn
    name_soup=None
    name=None
    try:
        name_soup=table.find("span",{"class":"fn"})
    except Exception as e:
        logger.exception("Could  not find web element fn for candidate name for %s",link)
                
    if name_soup:
        #The resulting text is in unicode which has to be encoded in ascii
        try:
            cand_info['name']=name_soup.text.encode('ascii','ignore')
        except Exception as nm:
            logger.exception("Could  not extract candidate name from unicode %s",name)
            #logger.error(nm)
            #If extracting from the web page fails, extract from the link
            name=link.split('/')[-1].replace('_',' ')
            logger.info("Successfully extracted candidate name %s",name)
            cand_info['name']=name

    #Extract age which we can find in the html element: noprint ForceAgeToShow
    age_soup=None
    age=None
    try:
        age_soup=table.find('span',{"class":"noprint ForceAgeToShow"})
    except Exception as e:
        logger.exception("Could  not extract candidate age for %s",name)

    #try encoding the age from unicode
    if age_soup:
        logger.info("Successfully extracted age soup from soup")
        try:
            age=age_soup.text.encode('ascii','ignore')
        except Exception as ag:
            logger.exception("Could not encode age for %s",age)
            #log.error(ag)

    #The extracted age is in the form (ageXX).Extract numeric data from it
    if age:
        match=re.search(r'\d+',age)
        if match:
            cand_info['age']=match.group()
            logger.info("Successfully extracted numerical age for %s",name)
        else:
            logger.error("Malformed string encountered for age of %s",name)

    #Search for the html table rows,'th' elements which contain the party and constituency information
    rows=None
    try:
        rows=table.find_all('th')
    except Exception as e:
        logger.exception("Could not find the 'th' element for the candidate %s",name)
            
    if rows:
        for row in rows:           #table.find_all('th'):
            if row.text=='Political party':
                try:
                    cand_info['Political party']= row.parent.text.encode('ascii','ignore').split('\n')[2]
                    logger.info("Successfully extracted party name for %s",name)
                except Exception as e:
                    logger.exception("Could not find political party for %s",link)
            elif row.text=='Constituency':
                try:
                    cand_info['Constituency']= row.parent.text.encode('ascii','ignore').split('\n')[2]
                    logger.info("Successfully extracted constituency for %s",name)
                except Exception as e:
                    logger.exception("Could not find constituency for %s",link)
  
    return cand_info
    
def main():
    args=sys.argv[1:]
    if len(args) ==0:
        print "Provide url"
        exit(1)

    for arg in args:
        candidates_hash={}
        candidates_hash=candidate_info(arg)
        for v,k in candidates_hash.items():
            print v,k
        candidates_hash=None
        
if __name__=='__main__':
    main()
