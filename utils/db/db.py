import logging

from psycopg2 import connect


class DataBase:
    def __init__(self, database_url):
        """Connecting to database and saving connection cursor"""
        logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.INFO)
        logging.info("Connecting to the PostgreSQL database...")

        self.__connection = connect(database_url)
        self.__cursor = self.__connection.cursor()

        logging.info("PostgreSQL database version:")
        self.__cursor.execute('SELECT version()')
        logging.info(self.__cursor.fetchone())

    def __del__(self):
        """Closing a database connection"""
        logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.INFO)

        self.__cursor.close()
        self.__connection.close()

        logging.info("Database connection closed")
