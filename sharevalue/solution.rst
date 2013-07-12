Objective
---------

Writing a python script to get the value of the market share of a specific NASDAQ from Yahoo.

Solution
--------

I divided the code into two files. The main code in sharevalue.py_ and the Yahoo API module in YahooAPI.py_. This way the API module can be used again with a different python script and the main code can use different API modules.

sharevalue.py
"""""""""""""


.. code:: python

        #!/usr/bin/env python
        """
        This python script will use the API modules
        availables to check the value of a specific
        ticker online and return it
        """
        
        import sys
        from YahooAPI import YFinance
        
        
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

YahooAPI.py
"""""""""""

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

.. _sharevalue.py: https://raw.github.com/ThyArmageddon/dgplug/master/sharevalue/sharevalue.py

.. _YahooAPI.py: https://raw.github.com/ThyArmageddon/dgplug/master/sharevalue/YahooAPI.py
