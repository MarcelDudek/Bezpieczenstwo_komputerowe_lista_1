import binascii

class Cryptogram:
    message = bytearray()

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

    def print(self):
        print(binascii.hexlify(self.message))



c = Cryptogram()
c.load('test.txt')
c.print()