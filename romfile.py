"""Rom File creation"""

from hash import crc32checksum
from hash import md5checksum
from hash import sha1checksum
from filesize import file_size
from pathlib import PurePath


class romfile:
    """
    Rom class who define :
    - parentpath
    - romfilename
    - size
    - crc32
    - md5
    - sha1
    """

    def __init__(self, fullpath):
        self.parentpath = PurePath(fullpath).parents[0]
        self.name = PurePath(fullpath).name
        self.size = file_size(fullpath, 1)
        if self.size < 524288000:
            self.crc32 = crc32checksum(fullpath)[0]
            self.md5 = md5checksum(fullpath)[0]
            self.sha1 = sha1checksum(fullpath)[0]
        else:
            self.crc32 = ''
            self.md5 = md5checksum(fullpath)[0]
            self.sha1 = ''


if __name__ == "__main__":
    rom1 = romfile(__file__)
    print("parentpath :", rom1.parentpath)
    print("name :", rom1.name)
    print("size :", rom1.size)
    print("crc32 :", rom1.crc32)
    print("md5 :", rom1.md5)
    print("sha1 :", rom1.sha1)
