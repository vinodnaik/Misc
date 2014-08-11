# http://en.wikipedia.org/wiki/Category:16th_Lok_Sabha_members

from bs4 import BeautifulSoup
import sys
import string
import urllib2
import logging
import logging.config
import logging.handlers
from candidate import candidate_info
import time
import os
import argparse
from database import MyDb

#configure logging
if not os.path.exists("logs"):
    os.makedirs("logs")
log_file_name = "logs/loksabha-members.log"
formatter = logging.Formatter('%(levelname)s:%(module)s:%(funcName)s:%(asctime)s:%(message)s')
logger = logging.getLogger(__name__)
logging.basicConfig(filename=log_file_name, level=logging.INFO, filemode='w')
#logger = logging.getLogger(__name__)
filehandler = logging.handlers.RotatingFileHandler(log_file_name, backupCount=5)
filehandler.setFormatter(formatter)
consolehandler = logging.StreamHandler()
consolehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.addHandler(consolehandler)
logger.info("Its working")


def extract_urls(urls):
    """

    :rtype : object
    """

    try:
        u = urllib2.urlopen(urls)
    except Exception as e:
        logger.error("could not open %s. The exception is %s", urls, e)
        exit()

    data = u.read()
    soup = BeautifulSoup(data)
    logger.info("successfully cooked soup for %s", urls)

    try:
        tdlist = soup.find_all('td')
    except Exception as e:
        logger.error("could not find 'td' in the soup")
        exit()
    logger.info("Successfully found td in the soup")

    uls = []

    for td in tdlist:
        try:
            uls = uls + td.find_all('a')
        except Exception as e:
            logger.error('Could not find links in %s', td.text)
            continue
        logger.info('Successfully found links inside %s', td.text)

    urllist = []

    i = 0
    wiki = "http://en.wikipedia.org"
    for link in uls:
        #wiki = "http://en.wikipedia.org" + link['href']
        urllist.append(wiki + link['href'])
        logger.info("Extracted url is %s", wiki+link['href'])
        #wiki = None

    return urllist


def extract_fromfile(file_path):
    if os.path.exists(file_path):
        logger.error("File '{0}' does not exist".format(file_path))
    fhandle = open(file_path, 'r')
    url_list = fhandle.read().split(',')
    logger.info("Extracted urls are \n", url_list)
    return url_list


def main():

    # #configure logging
    # if not os.path.exists("logs"):
    #     os.makedirs("logs")
    # log_file_name = "logs/loksabha-members.log"
    # logger = logging.getLogger(__name__)
    # logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(levelname)s:%(module)s:%(funcName)s:'
    #                                                                        '%(asctime)s:%(message)s', filemode='w')
    # #logger = logging.getLogger(__name__)
    # handler = logging.handlers.RotatingFileHandler(log_file_name, backupCount=5)
    # logger.addHandler(handler)
    # logger.info("Its working")

    #configure the command line argument parser
    parser = argparse.ArgumentParser(description="Extract candidates info")
    #    parser.add_argument('input', help='File containing links or a link to webpage')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-l", help='The argument is a link to wiki page', action="store",
                       dest="pagelink")
    group.add_argument("-f", help='The argument is a file containing links',
                       action="store", dest="filename")
    args = parser.parse_args()

    if args.pagelink:
        urls = extract_urls(args.pagelink)
    elif args.filename:
        urls = extract_fromfile(args.filename)

    try:
        f = open("output.txt", 'w+')
    except Exception as e:
        logger.error("The file output.txt could not be opened")
    logger.info("Successfully opened the output.txt for writing")

    i = 0
    db = MyDb()

    if db.initialized:
        for link in urls:
            cinfo = candidate_info(link)
            if cinfo:
                db.storedb(cinfo)
                # for k, v in cinfo.items():
                #     f.write(k + "---->" + v+'\n')
            #f.write("\n")

    #logger.info("Closing output.txt")
    f.close()


if __name__ == '__main__':
    main()
