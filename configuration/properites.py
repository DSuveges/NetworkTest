# All configurations required for the application:


class Configuration():
    """
    This class only provides parameters for the application

    ping_interval: interval in seconds to ping the specified servers.
    server_list: list of tuple with server IP/URL and the applied alias.
    db_file: file name of the sqlite3 database file.
    """
    ping_interval = 10  # In seconds
    server_list = [
        ('google.com', 'remote'),
        ('192.168.1.254', 'local')
    ]
    db_file = 'network_test_database.db'
