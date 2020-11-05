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
    
    def __len__(self):
        return len(self.message)

    def __getitem__(self, i):
        return self.message[i]


class Cracker:
    def __init__(self):
        self.cryptograms = []
        self.key = bytearray()
        self.key_cracked = bytearray()

    def load_from_files(self, paths):
        for path in paths:
            c = Cryptogram()
            c.load(path)
            self.cryptograms.append(c)

    def print_all(self):
        for c in self.cryptograms:
            c.print()

    def crack(self):
        self.key = bytearray()
        self.key_cracked = bytearray()

        # find out the max length of the key
        max_len = 0
        for c in self.cryptograms:
            if len(c) > max_len:
                max_len = len(c)
        self.key = bytearray(max_len)
        self.key_cracked = bytearray(max_len)
        for i in range(len(self.cryptograms)):
            for j in range(i, len(self.cryptograms)):
                for k in range(j, len(self.cryptograms)):
                    self.__crack_three(self.cryptograms[i], self.cryptograms[j], self.cryptograms[k])

    def __crack_three(self, c1: Cryptogram, c2: Cryptogram, c3: Cryptogram):
        l = min([len(c1), len(c2), len(c3)])
        for i in range(l):
            if not self.key_cracked[i]:
                k = self.__get_key(c1[i], c2[i], c3[i])
                if k is not None:
                    self.key[i] = k
                    self.key_cracked[i] = 0xFF

    def __get_key(self, c1: int, c2: int, c3: int):
        space = 0b01000000
        c1c2 = c1 ^ c2
        c1c3 = c1 ^ c3
        c2c3 = c2 ^ c3
        if c1c2 & space and c1c3 & space and c2c3 & space:  # impossible to distinguish
            return None
        elif c1c2 & space and c1c3 & space:  # c1 is space
            return c1 ^ space
        elif c1c2 & space and c2c3 & space:  # c2 is space
            return c2 ^ space
        elif c1c3 & space and c2c3 & space:  # c3 is space
            return c3 ^ space
        else:
            return None

    def print_key(self):
        print(binascii.hexlify(self.key))

    def print_cracked_key_bytes(self):
        print(binascii.hexlify(self.key_cracked))


c = Cracker()
paths = ['cryptograms/1.txt', 'cryptograms/2.txt', 'cryptograms/3.txt', 'cryptograms/4.txt',
'cryptograms/5.txt', 'cryptograms/6.txt', 'cryptograms/7.txt', 'cryptograms/8.txt',
'cryptograms/9.txt', 'cryptograms/10.txt', 'cryptograms/11.txt', 'cryptograms/12.txt', 
'cryptograms/13.txt', 'cryptograms/14.txt', 'cryptograms/15.txt', 'cryptograms/16.txt', 
'cryptograms/17.txt', 'cryptograms/18.txt', 'cryptograms/19.txt', 'cryptograms/20.txt']
c.load_from_files(paths)
# c.print_all()
c.crack()
c.print_key()
c.print_cracked_key_bytes()