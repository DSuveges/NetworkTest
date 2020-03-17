import sqlite3
import os.path

class db_connection(object):
    """
    This class establishes the connection with the database. It also has the table definitions.
    If the requested db file does not exist, creates the database with the proper tables.
    """

    # Table with all the return values of the pings and corresponding server information:
    pings_table_sql = """CREATE TABLE IF NOT EXISTS PINGS (
        ID INTEGER PRIMARY KEY,
        PING_TIME DATETIME NOT NULL,
        PING_VALUE INTEGER NOT NULL,
        SERVER_ID INTEGER NOT NULL,
        FOREIGN KEY (SERVER_ID) REFERENCES SERVER (ID)
    )"""

    # Table with server information:
    servers_table_sql = """CREATE TABLE IF NOT EXISTS SERVER (
        ID INTEGER PRIMARY KEY,
        URL TEXT NOT NULL,
        ALIAS TEXT NOT NULL
    )"""

    def __init__(self, filename):
        # Check if file exists:
        if not os.path.isfile(filename):
            print ("[Info] {} could not be opened. DB is being created.".format(filename))

        # Create connection:
        self._create_connection(filename)

        # Create all tables:
        self._create_tables()

    def _create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            self.conn = sqlite3.connect(db_file)
        except:
            print("[Error] DB could not be connected ({}). Exing".format(db_file))
            raise

    def _create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except:
            print('[Error] Table could not be connected.')
            raise

    def _create_tables(self):
        tables_to_create = ['servers', 'pings']

        # create all tables
        for table in tables_to_create:
            print('[Info] Creating table: {}'.format(table))
            sql_statement = getattr(self, table+'_table_sql')
            self._create_table(sql_statement)

