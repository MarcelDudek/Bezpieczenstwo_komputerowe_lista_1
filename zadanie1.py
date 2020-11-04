import binascii

class Cryptogram:
    def __init__(self):
        self.message = bytearray()

    def load(self, path):
        f = open(path)
        while True:
            char = f.read(9)
            if not char:
                break
            byte = 0
            shift = 7
            for bit in char:
                if bit == '1':
                    byte += 1 << shift
                shift -= 1
            self.message.append(byte)
        f.close()

    def print(self):
        print(binascii.hexlify(self.message))


class Cracker:
    def __init__(self):
        self.cryptograms = []

    def load_from_files(self, paths):
        for path in paths:
            c = Cryptogram()
            c.load(path)
            self.cryptograms.append(c)

    def print_all(self):
        for c in self.cryptograms:
            c.print()


c = Cracker()
paths = ['cryptograms/1.txt', 'cryptograms/2.txt', 'cryptograms/3.txt', 'cryptograms/4.txt',
'cryptograms/5.txt', 'cryptograms/6.txt', 'cryptograms/7.txt', 'cryptograms/8.txt',
'cryptograms/9.txt', 'cryptograms/10.txt', 'cryptograms/11.txt', 'cryptograms/12.txt', 
'cryptograms/13.txt', 'cryptograms/14.txt', 'cryptograms/15.txt', 'cryptograms/16.txt', 
'cryptograms/17.txt', 'cryptograms/18.txt', 'cryptograms/19.txt', 'cryptograms/20.txt']
c.load_from_files(paths)
c.print_all()