#!/usr/bin/env python
"""
This script will output the users on the current system
"""

from sys import exit
from os import path
from pwd import getpwall
import re


def print_users():
    """
    We get the information from passwd and the range of UIDs.
    Then we print all the users in the range.
    """
    passwd_info = getpwall()

    min_uid, max_uid = find_uid_range()

    print "Users on this system are:"
    print "-------------------------"

    for user in passwd_info:
        if (not user.pw_uid) or (user.pw_uid >= min_uid and user.pw_uid <= max_uid):
            print user.pw_name


def find_uid_range():
    """
    When a user uses useradd the system will assign a UID in the range
    mentioned in login.defs. So the assumption is that very rarely users
    choose their own UIDs and let the system choose instead. So we
    parse the login.defs file and get the values of UID_MIN and
    UID_MAX and return it as this is the range of UIDs autoassigned
    to users.
    """
    if path.exists("/etc/login.defs"):
        f = open("/etc/login.defs").read()
        min_uid_pattern = re.compile('\n\s*UID_MIN\s+(\d+)\s*\n')
        max_uid_pattern = re.compile('\n\s*UID_MAX\s+(\d+)\s*\n')
        min_uid = re.findall(min_uid_pattern, f)
        max_uid = re.findall(max_uid_pattern, f)
        return int(min_uid[0]), int(max_uid[0])
    else:
        print "Could not find login.defs file on system"
        exit(1)


if __name__ == '__main__':

    print_users()
    exit(0)
