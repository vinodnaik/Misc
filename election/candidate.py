import urllib2
import sys
import string
from bs4 import BeautifulSoup
import re
import logging

def candidate_info(link):
    logger=logging.getLogger(__name__)
    log_file="candidate_info"+str(time.time()).split('.')[0]+".log"
    fh=logging.FileHandler(log_file)
    logger.addHandler(fh)
    logger.propagate=False
    cand_info={}
    
    try:
        u=urllib2.urlopen(link)
    except Exception as e:
        logger.error("Could not open %s",link,e)
        return

    soup=BeautifulSoup(u.read())
    try:
        table=soup.find('table',attrs={'class':'infobox vcard'})
    except Exception as e:
        log.error("Could not find candidate info for %s",link)
        return

    name="Name not found"
    try:
        name=table.find("span",{"class":"fn"})
    except Exception as e:
        log.error("Could  not find web eliment for candidate name for %s",table.text)
            
    try:
        cand_info['name']=name.text.encode('ascii','ignore')
    except Exception as nm:
        log.error("Could  not find candidate name for %s",name.text)

    age="Age not found"
    try:
        age=table.find('span',{"class":"noprint ForceAgeToShow"})
    except Exception as e:
        log.error("Could  not find candidate age for %s",cand['name'])
    try:
        cand_info['age']=age.text.encode('ascii','ignore')
    except Exception as ag:
        pass
    
    """
    match=re.search(r'\d+',table.find('span',{"class":"noprint ForceAgeToShow"}))#.text.encode('ascii','ignore'))

    if match:
        cand_info['age']=match.group().text.encode('ascii','ignore')
   """
    rows=None
    try:
        rows=table.find_all('th')
    except Exception as e:
        pass
    if rows:
        for row in table.find_all('th'):
            if row.text=='Political party':
                try:
                    cand_info['Political party']= row.parent.text.encode('ascii','ignore').split('\n')[2]
                except Exception as e:
                    pass
            elif row.text=='Constituency':
                try:
                    cand_info['Constituency']= row.parent.text.encode('ascii','ignore').split('\n')[2]
                except Exception as e:
                    pass
  
    return cand_info
    
def main():
    args=sys.argv[1:]
    if len(args) ==0:
        print "Provide url"
        exit(1)

    candidates_hash={}
    candidates_hash=candidate_info(args[0])

    for v,k in candidates_hash.items():
        print v,k
        
if __name__=='__main__':
    main()
