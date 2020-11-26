""" Grabbed from shutil.which. in order to have it available for Python 2.

Seems to be working out of the box. Remove check for windows since it doesn't
really concern me in the context of dotfiles. Would probably be a good idea 
to yank the test cases written for it in Python 3 and see that they all work
ok for Python 2.
"""
import os


def which(cmd, mode=os.F_OK | os.X_OK, path=None):
    """Given a command, mode, and a PATH string, return the path which
    conforms to the given mode on the PATH, or None if there is no such
    file.
    `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
    of os.environ.get("PATH"), or can be overridden with a custom search
    path.
    """
    # Check that a given file can be accessed with the correct mode.
    # Additionally check that `file` is not a directory, as on Windows
    # directories pass the os.access check.
    def _access_check(file_, mode):
        return (os.path.exists(file_) and os.access(file_, mode)
                and not os.path.isdir(file_))

    # If we're given a path with a directory part, look it up directly rather
    # than referring to PATH directories.This includes checking relative to the
    # current directory, e.g. ./script
    if os.path.dirname(cmd):
        if _access_check(cmd, mode):
            return cmd
        return None

    if path is None:
        path = os.environ.get("PATH", os.defpath)
    if not path:
        return None
    path = path.split(os.pathsep)

    # Note: We ignore windows here by removing the relevant code.
    files = [cmd]

    seen = set()
    for dir_ in path:
        normdir = os.path.normcase(dir_)
        if normdir not in seen:
            seen.add(normdir)
            for thefile in files:
                name = os.path.join(dir_, thefile)
                if _access_check(name, mode):
                    return name
    return None
