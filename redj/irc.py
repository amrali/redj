import ssl
import irc.client

class Client(object):
    """\
    An IRC client to handle the most basic functionality.
    """

    def __init__(self):
        self.ircobj = irc.client.IRC()
        self.ircobj.add_global_handler('all_events', self._dispatcher, -10)

    def connect(self, *args, **kwargs):
        """\
        Connect to an IRC server.

        :param server: Server name.
        :param port: Port number.
        :param nickname: The nickname.
        :param password: Password (optional).
        :param username: The username (optional).
        :param ircname: The realname (optional).
        """
        self._connect(*args, **kwargs)

    def ssl_connect(self, *args, **kwargs):
        """\
        Connect to an IRC server over SSL.

        :param server: Server name.
        :param port: Port number.
        :param nickname: The nickname.
        :param password: Password (optional).
        :param username: The username (optional).
        :param ircname: The realname (optional).
        """
        ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
        kwargs['connect_factory'] = ssl_factory
        self.connect(*args, **kwargs)

    def on_welcome(self, conn, event):
        """\
        What should I do when I'm connected to a server.
        """
        if irc.client.is_channel(self.target): # Join it if `target` is a channel
            conn.join(self.target)
        else: # TODO: What should I do when `target` is not a channel?
            # conn.privmsg(self.target, "hey sexy")
            # conn.quit("leaving the party")
            pass

    def on_join(self, conn, event):
        """\
        What should I do when I join a channel.
        """
        pass # TODO: Implement

    def on_disconnect(self, conn, event):
        """\
        What should I do on disconnect.
        """
        pass # TODO: Implement

    def on_kick(self, conn, event):
        """\
        What should I do when kicked out of a channel.
        """
        pass # TODO: Implement

    def _dispatcher(self, conn, event):
        """\
        Dispatch events to an event handler if one is available.
        """
        do_nothing = lambda c, e: None
        method = getattr(self, "on_{}".format(event.type), do_nothing)
        method(connection, event)

    def _connect(self, *args, **kwargs):
        """\
        Create a new connection.
        """
        conn = self.ircobj.server()
        conn.connect(*args, **kwargs)

