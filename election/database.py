import sqlite3
import logging
logger = logging.getLogger(__name__)


class MyDb:
    initialized = False

    def __init__(self, dbfile):
        try:
            self.conn = sqlite3.connect(dbfile)
        except Exception as e:
            logger.error("Could not create a connection to the db", e)
            return
        logger.info("Successfully created a connection to the db")

        self.c = self.conn.cursor()

        #Create table
        try:
            self.c.execute('''CREATE TABLE if not exists candidates(name text,
            age text,constituency text, party text)''')
        except Exception as e:
            logger.error("Could not create a table", e)
            return
        logger.info("Successfully created the table candidate")
        self.initialized = True

    def storedb(self, candidate):
        name = None
        age = None
        constituency = None
        party = None

        try:
            candidate['name']
        except (NameError, KeyError):
            logger.error("Candidate name is not present")
            name = None
        else:
            name = candidate['name']

        try:
            candidate['age']
        except (NameError, KeyError):
            logger.error("Candidate age is not present")
            age = None
        else:
            age = candidate['age']

        try:
            candidate['constituency']
        except (NameError, KeyError):
            logger.error("Candidate constituency is not present")
            constituency = None
        else:
            constituency = candidate['constituency']

        try:
            candidate['party']
        except (NameError, KeyError):
            logger.error("Candidate party is not present")
            party = None
        else:
            party = candidate['party']

        try:
            self.c.execute("INSERT INTO candidates VALUES (?,?,?,?)", (name, age, constituency, party))
        except Exception as e:
            logger.error("Could not add record for {0} Exception : ({1})".format(name, e.args))
        else:
            logger.info("Successfully written details for '{0}' to the db".format(name))
            self.conn.commit()

    def __del__(self):
        self.conn.close()

