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

    def __check_user_existing(self, user_id):
        """Check user existing"""
        self.__cursor.execute('SELECT * FROM users WHERE user_id=(%s);', (user_id,))
        res = self.__cursor.fetchall()
        return bool(len(res))

    def add_new_user(self, user_id):
        """Add new user in database if he not existing"""
        with self.__connection:
            if not self.__check_user_existing(user_id=user_id):
                self.__cursor.execute('INSERT INTO users (user_id) VALUES(%s);', (user_id,))
                self.__connection.commit()

    def add_comment_from_user(self, user_id, comment):
        """Add new comment from user"""
        with self.__connection:
            self.__cursor.execute('INSERT INTO comments (comment, user_id) VALUES(%s, %s);', (comment, user_id,))
            self.__connection.commit()
