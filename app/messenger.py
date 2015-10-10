from interface import IO


class Messenger(object):

    def send(self, msg):
        IO.write(msg)
