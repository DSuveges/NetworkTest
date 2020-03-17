import sqlite3
from datetime import datetime


class db_handler(object):
    """
    This class defines the modules to add data directly to the database.
    Contains all the SQL statements as well.
    """

    # Check if server is in the database:
    check_server = '''SELECT * FROM SERVER WHERE URL = :url'''

    # Add server to the database:
    add_server = '''INSERT INTO SERVER (URL, ALIAS)
                    VALUES(:url, :alias)'''

    # Add ping response to the database:
    add_ping_response_row = '''INSERT INTO PINGS (PING_TIME, PING_VALUE, SERVER_ID)
                    VALUES(:ping_time, :ping_value, :server_id)'''

    def __init__(self, connection):
        """
        To initialize the db handler object,
        """

        if not isinstance(connection, sqlite3.Connection):
            raise TypeError ("Connection object is expected for initialize add_data object.")

        self.conn = connection
        self.cursor = connection.cursor()

    def add_servers(self, servers):
        """
        Looking up a server in the db

        :param servers: list of tuples of the server url and the corresponding alias
        :return: list of tuples with of the server url and the corresponding table ID
        """

        return_value = []

        for (url, alias) in servers:
            # Fetch data from db:
            self.cursor.execute(self.check_server, {'url': url})

            # If the server is already in the database:
            try:
                (ID, URL, ALIAS) = self.cursor.fetchone()

            # If the server is not in the row, we add it:
            except TypeError:
                self.cursor.execute(self.add_server, {'url': url, 'alias': alias})
                ID = self.cursor.lastrowid
                self.conn.commit()

            return_value.append((url, ID))

        return return_value

    def add_ping_response(self, responses):
        """
        This function adds a row to ping table

        :param responses: list of tuples of the server ID and ping response
        """

        for (ID, response) in responses:

            # Add ping response:
            self.cursor.execute(self.add_ping_response_row, {'ping_time': datetime.now(),
                                                         'ping_value': response,
                                                         'server_id': ID})
            # Committing row:
            self.conn.commit()