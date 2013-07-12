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
