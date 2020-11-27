#!/bin/python
"""
Must use Python 2/3 agnostic code. Set up dotfiles by symlinking them to the
correct subdirectories.

Would be a good idea to symlink only if the relevant software exists and
possibly prompt if it doesn't. (though no harm is really done.)

Supporting config.ini file can be used to hold all relevant metadata
(location for each subdirectory, etc)
"""
from __future__ import print_function
import os
from sys import version_info
from collections import namedtuple
from awhich import which

MAJOR = version_info.major
if MAJOR == 3:
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

# For holding entries, fields must match config.ini fields.
Entry = namedtuple('Entry', 'filename destination bin')


def config_to_entries(config):
    """ Take configparser and yield entries. """
    for section in config.sections():
        temp = []
        for option in config.options(section):
            if option == 'destination':
                value = replace_tilde(config.get(section, option))
            else:
                value = config.get(section, option)
            temp.append(value)
        yield Entry(*temp)


def replace_tilde(path):
    """
    Very basic replacement. If it starts with a tilde,
    prepend $HOME to it.
    """
    if not path.startswith("~"):
        return path
    # do not trim '/' after tilde.
    return "".join([home_folder(), path[1:]])


def make_symlink(entry):
    """ Create a symbolic link from our source inside dotfiles
    to our destination (wherever that may be.)
    """
    # Should check if it already exists and if so if
    # the file we are trying to symlink is more recent.
    os.symlink(entry.filename, entry.destination)


def folder_exists(path):
    """
    Check path to see if folder exists, if it does, no
    need to create it.
    """



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

    This is still in a function because I'm not sure if it can fail
    in any way. Do other systems use something different other than $HOME?
    """
    return os.environ['HOME']


if __name__ == "__main__":
    # Can't index configparser in Python 2, use options, sections and get.
    conf = ConfigParser()
    conf.read('config.ini')

    for entry in config_to_entries(conf):
        print(entry)
