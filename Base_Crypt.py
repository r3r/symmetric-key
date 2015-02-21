__author__ = 'RiteshReddy'
import random, os
class Base_Crypt():
    padd = '~'

    def padd_message(self, message, block_size):
        length = len(message)
        if block_size >= length:
            raise Exception("too many chunks, i.e., message too short for number of chunks")
        if length % block_size != 0:
            message += self.padd * (block_size-(length % block_size))
        return message

    def unpadd_message(self, message):
        i  = len(message)-1
        while i > 0 and message[i] == self.padd:
            i -= 1
        message = message[:i+1]
        return message


    def split_message(self, message, block_size):
        length = len(message)
        num_blocks = length/block_size
        chunks = []
        for i in range(0, length, block_size):
            chunks.append(message[i:i+block_size])
        return chunks, num_blocks

    def get_permutations(self, n, seed):
        random.seed(seed)
        seen = [False] * n
        perms = []
        rng = 2 ** n
        while not all(seen):
            t = random.randrange(rng)
            b = bin(t)[2:]
            b = b.zfill(n)
            perms.append(b)
            for ind, val in enumerate(b):
                if val == '1':
                    seen[ind] = True
        return perms

    def generate_garbage(self, block_size):
        return os.urandom(block_size)

    def cieser_shift(self, text, key, dir='L'):
        lst = [x for x in text]
        for i in range(len(lst)):
            if dir == 'L':
                lst[i] = chr((ord(lst[i]) - key) % 256)
            else:
                lst[i] = chr((ord(lst[i]) + key) % 256)
        return ''.join(lst)





