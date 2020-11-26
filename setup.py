#!/bin/python
"""
Must use Python 2/3 agnostic code. Set up dotfiles by moving them to the
correct subdirectories.

Would be a good idea to move only if the relevant software exists and
possibly prompt if it doesn't.

Supporting config.ini file can be used to hold all relevant metadata
(location for each subdirectory, etc).
"""
from __future__ import print_function
import os
from sys import version_info
from awhich import which

MAJOR = version_info.major
if MAJOR == 3:
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser


def folder_exists(path):
    """
    Check path to see if folder exists, if it does, no
    need to create it.
    """
    pass


def program_exists(pname):
    """
    Check to see if program with the name `pname` exists on the
    system.
    """
    return True if which(pname) else False


def home_folder():
    """
    Return the home folder by quering $HOME maybe?
    Used to replace `~` in paths.
    """
    return os.environ['HOME']


if __name__ == "__main__":
    # Can't index configparser in Python 2, use options, sections and get.
    conf = ConfigParser()
    conf.read('config.ini')
 
    # merely check things out for now.
    for section in conf.sections():
        for option in conf.options(section):
            print(conf.get(section, option), end=' ')
        print()
