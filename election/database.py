import sqlite3
import logging
logger = logging.getLogger(__name__)


class MyDb:
    initialized = False

    def __init__(self):
        try:
            self.conn = sqlite3.connect('example.db')
        except Exception as e:
            logger.error("Could not create a connection to the db", e)
            return
        logger.info("Successfully created a connection to the db")

        self.c = self.conn.cursor()

        #Create table
        try:
            self.c.execute('''CREATE TABLE if not exists candidates(name text, age number,
            constituency text, party text)''')
        except Exception as e:
            logger.error("Could not create a table", e)
            return
        logger.info("Successfully created the table candidate")
        self.initialized = True

    def storedb(self, **candidate):
        name = None
        age = None
        const = None
        party = None
        if candidate['name']:
            name = candidate['name']
        if candidate['age']:
            age = candidate['age']
        if candidate['constituency']:
            const = candidate['consttuency']
        if candidate['party']:
            party = candidate['party']
        try:
            self.c.execute("INSERT INTO stocks candidates (name,age,const,party)")
        except Exception as e:
            logger.error("Could not add record for %s", name)

