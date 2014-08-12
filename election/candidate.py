import urllib2
from bs4 import BeautifulSoup
import re
import logging

logger = logging.getLogger(__name__)


def candidate_info(link):
    cand_info = {}

    #code to open the link
    try:
        u = urllib2.urlopen(link)
    except urllib2.URLError:
        logger.exception("Could not open %s", link)
        return None
    logger.info("Successfully opened %s", link)

    #Cook a soup
    soup = BeautifulSoup(u.read())

    table = None
    #Capture the html element infobox vcard which normally contains the candidate info
    table = soup.find('table', attrs={'class': 'infobox vcard'}) or soup.find('table', attrs={'class': 'infobox biography vcard'})
    if table:
        logger.info("Successfully opened infobox vcard for %s", link)
    else:
        logger.error("Could not find infobox vcard for %s", link)
        return

    #code to capture the candidate name which is associated with the html element fn
    name_soup = None
    name = None
    name_soup = table.find("span", {"class": "fn"})
    if name_soup:
        logger.info("Successfully found class:fn for %s", link)
        name = name_soup.text.encode('ascii', 'ignore')
        cand_info['name'] = name
        if not name:
            #If extracting from the web page fails, extract from the link
            name = link.split('/')[-1].replace('_', ' ')
            logger.info("Successfully extracted candidate name %s", name)
            cand_info['name'] = name
        if not name:
            logger.error("could not find the candidate name")
            return
    else:
        logger.error("Could  not find web element fn for candidate name for %s", link)
        return
                
    #Extract age which we can find in the html element: noprint ForceAgeToShow
    age_soup = None
    age = None
    age_soup = table.find('span', {"class": "noprint ForceAgeToShow"})
    if age_soup:
        logger.info("Successfully extracted age soup from soup")
        #try encoding the age from unicode
        try:
            age = age_soup.text.encode('ascii', 'ignore')
        except Exception as ag:
            logger.exception("Could not encode age for %s", age)
    else:
        logger.exception("Could  not extract candidate age for %s", name)

    #The extracted age is in the form (ageXX).Extract numeric data from it
    if age:
        match = re.search(r'\d+', age)
        if match:
            cand_info['age'] = match.group()
            logger.info("Successfully extracted numerical age for %s", name)
        else:
            logger.error("Malformed string encountered for age of %s", name)

    #Search for the html table rows,'th' elements which contain the party and constituency information
    rows = None
    rows = table.find_all('th')

    if rows:
        for row in rows:
            if row.text == 'Political party':
                cand_info['party'] = row.parent.text.encode('ascii', 'ignore').split('\n')[2]
                logger.info("Successfully extracted party name for %s", name)
            if row.text == 'Constituency':
                cand_info['constituency'] = row.parent.text.encode('ascii', 'ignore').split('\n')[2]
                logger.info("Successfully extracted constituency for %s", name)

    try:
        cand_info['party']
    except (NameError, KeyError):
        logger.error("Party details are absent for %s", cand_info['name'])
    try:
        cand_info['constituency']
    except (NameError, KeyError):
        logger.error("Constituency details are absent for %s", cand_info['name'])


    return cand_info
