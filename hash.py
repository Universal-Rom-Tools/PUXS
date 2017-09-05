"""
Function to calculate hash
    return tuple (hash, hashtime)
    - md5checksum
    - sha1checksum
    - crc32checksum
"""

from hashlib import md5
from hashlib import sha1
from time import time
from zlib import crc32


def md5checksum(filepath):
    """
    this function will return the file MD5
    """
    start = time()
    with open(filepath, 'rb') as fh:
        m = md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        end = time()
        return m.hexdigest(), end - start


def sha1checksum(filepath):
    """
    this function will return the file SHA1
    """
    start = time()
    with open(filepath, 'rb') as fh:
        m = sha1()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        end = time()
        return (m.hexdigest(), end - start)


def crc32checksum(filepath):
    """
    this function will return the file CRC32
    """
    start = time()
    buffersize = 65536
    with open(filepath, 'rb') as fh:
        buffr = fh.read(buffersize)
        crcvalue = 0
        while len(buffr) > 0:
            crcvalue = crc32(buffr, crcvalue)
            buffr = fh.read(buffersize)
        end = time()
        return (format(crcvalue & 0xFFFFFFFF, '08x'), end - start)


if __name__ == "__main__":
    crc32, crc32time = crc32checksum(__file__)
    print("crc32 : {} in {}s".format(crc32, crc32time))
    md5, md5time = md5checksum(__file__)
    print("md5 : {} in {}s".format(md5, md5time))
    sha1, sha1time = sha1checksum(__file__)
    print("sha1 : {} in {}s".format(sha1, sha1time))
