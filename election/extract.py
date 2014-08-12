#!/usr/bin/env python
# http://en.wikipedia.org/wiki/Category:16th_Lok_Sabha_members

from bs4 import BeautifulSoup
import urllib2
import logging
import logging.config
import logging.handlers
from candidate import candidate_info
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
filehandler = logging.handlers.RotatingFileHandler(log_file_name, backupCount=5)
filehandler.setFormatter(formatter)
consolehandler = logging.StreamHandler()
consolehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.addHandler(consolehandler)
logger.info("Loggers initialized")


def extract_urls(urls):
    """

    :rtype : object
    """

    try:
        u = urllib2.urlopen(urls)
    except urllib2.URLError:
        logger.error("could not open %s", urls)
        exit()

    data = u.read()
    soup = BeautifulSoup(data)
    logger.info("successfully cooked soup for %s", urls)

    tdlist = soup.find_all('td')
    if tdlist:
        logger.info("Successfully found td")
    else:
        logger.error("could not find 'td' in the soup")
        exit()

    uls = []

    for td in tdlist:
        links = td.find_all('a')
        if links:
            uls = uls + links
            logger.debug('Successfully found links inside %s', td.text)
            links = None
        else:
            logger.error('Could not find links in %s', td.text)

    urllist = []
    wiki = "http://en.wikipedia.org"

    for link in uls:
        urllist.append(wiki + link['href'])
        logger.debug("Extracted url is %s", wiki+link['href'])

    return urllist


def extract_fromfile(file_path):
    if os.path.exists(file_path):
        logger.error("File '{0}' does not exist".format(file_path))
    file_handle = open(file_path, 'r')
    url_list = file_handle.read().split(',')
    logger.info("Extracted urls are \n", url_list)
    return url_list


def main():

    #configure the command line argument parser
    parser = argparse.ArgumentParser(description="Extract candidates info")

    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument("-l", help='The argument is a link to wiki page',
                        action="store", dest="pagelink")
    group1.add_argument("-f", help='The argument is a file containing links',
                        action="store", dest="filename")

    group2 = parser.add_mutually_exclusive_group(required=False)
    group2.add_argument("-d", help='The argument is name of database file',
                        action="store", dest="database_file_name")
    group2.add_argument("-o", help='The argument is a file containing the script results',
                        action="store", dest="output_file")

    args = parser.parse_args()

    if args.pagelink:
        urls = extract_urls(args.pagelink)
    elif args.filename:
        urls = extract_fromfile(args.filename)

    if args.database_file_name:
        db = MyDb(args.database_file_name)
        if db.initialized:
            for link in urls:
                cinfo = candidate_info(link)
                if cinfo:
                    db.storedb(cinfo)
            logger.info("Done writing to DB")

        elif args.output_file:
            out_file = args.output_file
        else:
            logger.error("Could not create the db for writing")
            out_file = "output.txt"
            try:
                f = open(out_file, 'w+')
            except Exception as e:
                logger.error("The file {0} could not be opened".format(out_file))
            else:
                logger.info("Successfully opened the {0} for writing".format(out_file))
                for link in urls:
                    cinfo = candidate_info(link)
                    if cinfo:
                        f.write(cinfo+"\n")
                logger.info("Closing output.txt")
                f.close()


if __name__ == '__main__':
    main()
