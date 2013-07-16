#!/usr/bin/env python
"""
This script will parse the RSS feed from Planet Fedora
and will print out the Authors and the Post Titles

Module dependencies:
    - feedparser
"""

from sys import exit
import re
import feedparser


def parse_feed(feed_):
    """
    The following function will parse the feed and return
    a list of tuples, Author Post, to be used later.
    """

    author = range(len(feed_.entries))
    post = range(len(feed_.entries))

    for i in range(len(feed_.entries)):
        author[i] = re.findall("(.*):\s.*", feed_.entries[i].title)
        post[i] = re.findall(".*:\s(.*)", feed_.entries[i].title)

    author = [item for sublist in author for item in sublist]
    post = [item for sublist in post for item in sublist]

    parsed_info = zip(author, post)

    return parsed_info


def print_feed(parsed_info):
    """
    This function will print out information
    from a list of tuples
    """

    print "RSS Planet Parser"

    for author, post in parsed_info:
        print "Author: %s\nPost: %s\n" % (author, post)


if __name__ == '__main__':
    """
    The main function will try to connect to the xml RSS link.
    If connecting fails, the script will exit with an error 1.
    Otherwise, it will read the link and send it to be parsed
    and then printed out.
    """

    try:
        feed_ = feedparser.parse("http://planet.fedoraproject.org/rss20.xml")

    except IOERROR:
        print "Could not connect to server"
        exit(1)

    else:
        parsed_info = parse_feed(feed_)
        print_feed(parsed_info)
        exit(0)
