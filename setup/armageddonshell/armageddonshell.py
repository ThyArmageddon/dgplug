#!/usr/bin/env python
from cmd2 import Cmd
from getpass import getuser
from sharevalue import Stock

__version__ = '0.3.1'


class Application(Cmd):
    """
    The main Application class

   """

    def __init__(self):
        Cmd.__init__(self)

    def do_hello(self, line):
        print "Hello:", line

    def do_sayit(self, line):
        print "Python Rocks!"

    def do_greet(self, line):
        """
        Greet the user by printing
        the username.
        """
        print "Hello %s" % getuser()

    def do_stock(self, line):
        """
        Call Stock from sharevalue to get the stock market
        value of a ticker.
        """
        print Stock(line)

def main():
    app = Application()
    app.cmdloop()

if __name__ == '__main__':
    main()
