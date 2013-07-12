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
