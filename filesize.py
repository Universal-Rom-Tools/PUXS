"""
Function to caluculate file size
    If strformat = 0
        return in bytes, Kb, MB, GB, TB
    Else
         return in bytes
"""

from os.path import isfile
from os import stat


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(filepath, strformat=0):
    """
    this function will return the file size
    """
    if isfile(filepath):
        file_info = stat(filepath)
        if strformat == 0:
            return convert_bytes(file_info.st_size)
        else:
            return file_info.st_size


if __name__ == "__main__":
    print("file size (strformat=0) : {}".format(file_size(__file__)))
    print("file size (strformat=1) : {}".format(file_size(__file__, 1)))
