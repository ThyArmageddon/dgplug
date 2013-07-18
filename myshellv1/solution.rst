MyShellv1
---------

Even though the name of the project is MyShellv1_, the actual version of it is 0.3. Anyway, this script will use sharevalue.py_ written previously, which was edited to be used as module as well, which uses, by itself, YahooAPI.py_.

.. _MyShellv1: https://raw.github.com/ThyArmageddon/dgplug/master/myshellv1/myshellv1.py
.. _sharevalue.py: https://raw.github.com/ThyArmageddon/dgplug/master/myshellv1/sharevalue.py
.. _YahooAPI.py: https://raw.github.com/ThyArmageddon/dgplug/master/myshellv1/YahooAPI.py


Code
----

YahooAPI.py
~~~~~~~~~~~

.. code:: python

        """
        Yahoo API Module
        ================

        YahooFinance Class
        ------------------
        This class will save the ticker in a correct link format
        and will output the correct value when value is called

        """

        import urllib2


        class YFinance(object):

            """
            The YahooAPI has a correct link
            and the value returned from Yahoo Finance
            """

            def __init__(self):
                """
                The default link is None
                """
                self._link = None

            @property
            def link(self):
                """
                This will return the link when needed
                to access the website and get the value
                """
                return self._link

            @property
            def value(self):
                """
                We try to connect to the link
                if everything goes well, we get the value
                we check if the value is not 0 and return it
                if we can't connect we will return -1
                """
                try:
                    fobj = urllib2.urlopen(self._link)
                    data = fobj.read()
                    value = float(data)
                    fobj.close()
                    if value == 0.0:
                        return
                    return value

                except IOError:
                    return -1

            @link.setter
            def link(self, ticker):
                """
                The link recieves a ticker and saves it as a link
                The link will be used later to get the information
                from the web page.
                """
                link = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1" \
                    % ticker
                self._link = link

sharevalue.py
~~~~~~~~~~~~~

.. code:: python

        #!/usr/bin/env python
        """
        This python script will use the API modules
        availables to check the value of a specific
        ticker online and return it
        """

        import sys
        from YahooAPI import YFinance

        def Stock(ticker=''):
            if not ticker:
                print "No Ticker"
                sys.exit(1)

            else:
                """
                We create a class from the Yahoo API
                We set the ticker argv[1]
                We ask for the value of the market
                """
                finance = YFinance()
                finance.link = ticker
                value = finance.value

                """
                We test if value is set first
                if it is not we exit because the ticker is wrong
                We, then, test if value is set to -1
                if it is we exit because we couldn't connect
                """
                if not value:
                    print """
                    You submitted a ticker that doesn't exist
                    Please try a different ticker than %s
                    """ % ticker
                    sys.exit(1)
                if value == -1:
                    print """
                    We were able to connect to the website
                    The website might be down
                    Please check your connection and try again.
                    """
                    sys.exit(1)

                else:
                    return value


        if __name__ == '__main__':
            """
            We start by testing the number of arguments
            and exit if the number of arguments is less
            than 2
            """

            if len(sys.argv) != 2:
                print """
                Incorrect argument length

                Usage:
                sharevalue.py <ticker>
                """
                sys.exit(1)

            """
            We create a class from the Yahoo API
            We set the ticker argv[1]
            We ask for the value of the market
            """
            finance = YFinance()
            finance.link = sys.argv[1]
            value = finance.value

            """
            We test if value is set first
            if it is not we exit because the ticker is wrong
            We, then, test if value is set to -1
            if it is we exit because we couldn't connect
            """
            if not value:
                print """
                You submitted a ticker that doesn't exist
                Please try a different ticker than %s
                """ % (sys.argv[1])
                sys.exit(1)
            if value == -1:
                print """
                We were able to connect to the website
                The website might be down
                Please check your connection and try again.
                """
                sys.exit(1)

            """
            If everything goes well, we print the value
            """
            print """
                The current value of %s is %.2f
            """ % (sys.argv[1], value)

myshellv1
~~~~~~~~~

.. code:: python

        #!/usr/bin/env python
        from cmd2 import Cmd
        from getpass import getuser
        from sharevalue import Stock

        __version__ = '0.3'


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


        if __name__ == '__main__':
            app = Application()
            app.cmdloop()
