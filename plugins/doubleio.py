import app.interface


class DoubleIO(object):

    @classmethod
    def write(cls, msg):
        print msg
        print msg

app.interface.IO = DoubleIO
