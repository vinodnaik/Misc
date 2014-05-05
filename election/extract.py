import requests
import re
from bs4 import BeautifulSoup
import sys
import string
import urllib2
from logging import *
import logging
from candidate import candidate_info
#from logconf import Logger
import time

def extract(urls):
    logger=logging.getLogger(__name__)
    log_file='extract'+str(time.time()).split('.')[0]+'.log'
    fh=logging.FileHandler(log_file)
    #logging.basicConfig()
    logger.addHandler(fh)
    logger.propagate=False
    
    for url in urls:
        try:
            #r=requests.get(url)
            u=urllib2.urlopen(url)
        except Exception as e:
            logger.error("could not open %s",url,e)
            continue
        
        data=u.read()
        soup=BeautifulSoup(data)
        logger.info("successfully cooked soup for %s",url)

        try:
            tdlist=soup.find_all('td')
        except Exception as e:
            logger.error("could not find 'td' in the soup")
            continue
        logger.info("Successfully found td in the soup")
        
        alphabets=string.uppercase
        nameheaders=[]
        uls=[]
        
        for td in tdlist:
            try:
                uls+=td.find_all('a')
            except Exception as e:
                logger.error("Could not find links in %s",td.text)
            logger.info("Successfully found links inside %s",td.text)
            
        ht={}

        candidate_list=[]
        logger.propagate=True
        for link in uls:
            wiki="http://en.wikipedia.org"+link['href']
            logger.info("Extracted url is %s",wiki)
            #try:
             #   namelist=link['title']
            #except Exception as e:
             #   logger.error("
            chash=candidate_info(wiki)
            if chash:
                candidate_list.append(chash)
            chash=None
        return candidate_list
            
    
def main():

    import logging.config
    logging.config.fileConfig('logging.conf',disable_existing_loggers=False)
    
    args=sys.argv[1:]
    
    if len(args) == 0:
        print "Usage extra.py [url]"
        logging.warn("the script was run without any arguments")
        exit(1)

    #cinfo=[]
    cinfo=extract(args)
    for cand in cinfo:
        for k,v in cand.items():
            print k,v
        
if __name__=='__main__':
    main()
    
