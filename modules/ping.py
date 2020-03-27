from ping3 import ping


class Ping(object):
    """
    dfd
    """

    def __init__(self, servers=None):
        """
        :param servers:
        """
        if servers and isinstance(servers, str):
            self.servers = [servers]
        elif servers and isinstance(servers,list):
            self.servers = servers
        elif servers:
            raise TypeError('The provided server ({}) must a string or list.'.format(servers))
        else:
            raise ValueError('To initialize ping object server name, or list of servers needs to be provided.')
        print(self.servers)

    def __len__(self):
        return len(self.servers)

    def ping(self):
        """
        :return: list of return values of the ping.
        """
        return [1 if ping(x, size=12) else 0 for x in self.servers]

