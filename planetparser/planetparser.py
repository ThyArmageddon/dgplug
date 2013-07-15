#!/usr/bin/env python
"""
planetparser is a script that parses the information on
http://planet.fedoraproject.org/ and prints the
the post title, the author, the link to the original
post and the post itself to the terminal
"""

from urllib import urlopen
from sys import exit, argv
from bs4 import BeautifulSoup
import re

def ParseAuthor(link):
    """
    In here, we use a regex to find and output the names of the authors
    on the whole page. This will return a list of the names
    """
    PatternAuthor = re.compile('<div\sclass="blog-entry\s(.+)">')
    return re.findall(PatternAuthor, link)


def ParsePostTitle(link):
    """
    In here, we use a regex to find and output the post titles
    on the whole page. This will return a list of the titles
    """
    PatternPostTitle = re.compile('<div\sclass="blog-entry-title">' +
                                  '<a\shref=.+>(.+)</a></div>')
    return re.findall(PatternPostTitle, link)


def ParseLink(link):
    """
    In here, we use a regex to find and output the post links
    on the whole page. This will return a list of the links
    """
    PatternLink = re.compile('<div\sclass="blog-entry-title">' +
                             '<a\shref="(.+)">.+</a></div>')
    return re.findall(PatternLink, link)


def ParsePost(link):
    """
    This function uses BeautifulSoup to find the content of the
    posts and will return the list of posts in html unchanged
    """
    Soup = BeautifulSoup(link)
    Posts = Soup.findAll(attrs={"class":"blog-entry-content"})
    return Posts


def PrintList(ListAuthor, ListPostTitle, ListLink, NoPost ,ListPost=''):
    """
    This function will print out the information given to it in lists
    in a formatted way to the terminal
    """
    print ""
    print "Fedora Planet"
    print "-------------\n"

    for i in range(len(ListAuthor)):
        print "Author: %s" % ListAuthor[i]
        print "Post Title: %s" % ListPostTitle[i]
        print "Link: %s" % ListLink[i]
        if NoPost == 0:
            print "-" * (len(ListLink[i]) + 6)
            print "\n"
            # We use .text to get only the text; strip html tags
            print "\t%s" % ListPost[i].text
            print "\n"
            print "*" * 100

        print "\n"


if __name__ == '__main__':
    """
    The first thing we need to do is open the url and read it
    We'll raise an exception if this doesn't work for some reason
    and we'll exit the script
    """

    NoPost = 0

    if len(argv) > 2:
        print "Too many arguments"
        print "Please use -h or --help for further help"
        exit(1)

    if len(argv) == 2:
        if argv[1] == '-h' or argv[1] == '--help':
            print "Usage: ./planetparser.py [OPTIONS]"
            print "Parses Planet Fedora and outputs information from the page.\n"
            print "Mandatory arguments"
            print "-h, --help\t\tprint this help page"
            print "-n, --no-post\t\tdo not print posts"
            exit(1)

        elif argv[1] == '-n' or argv[1] == '--no-post':
            NoPost = 1

        else:
            print "Wrong arguments"
            print "Please use -h or --help for further help"
            exit(1)

    try:
        link = urlopen("http://planet.fedoraproject.org/").read()

    except IOError:
        print "Could not connect to website"
        print "Please check your connection and try again"
        exit(1)

    # Get the list of authors
    ListAuthor = ParseAuthor(link)
    # Get the list of post titles
    ListPostTitle = ParsePostTitle(link)
    # Get the list of the links
    ListLink = ParseLink(link)
    """
    If the user does not want to display the posts
    Don't bother to parse them
    """
    if NoPost == 0:
        # Get the posts posted on the page
        ListPost = ParsePost(link)
        PrintList(ListAuthor, ListPostTitle, ListLink, NoPost, ListPost)
    # Print the output in a formated manner
    else :
        PrintList(ListAuthor, ListPostTitle, ListLink, NoPost)
    exit(0)
