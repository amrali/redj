import irc.client

class Client(irc.client.SimpleIRCClient):
    """\
    An IRC client to handle the most basic functionality.
    """

    def __init__(self, target):
        super(Client, self).__init__()
        self.target = target

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

