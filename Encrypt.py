__author__ = 'RiteshReddy'
from Base_Crypt import Base_Crypt
import random
class Encrypt(Base_Crypt):

    def __init__(self, seed, block_size, cipher_key):
        self.seed = seed
        self.cipher_key = cipher_key
        self.block_size = block_size

    def encrypt(self, message):
        message = self.padd_message(message, self.block_size)
        permuted, n = self.__permute(message)
        #substituted = self.cieser_shift(permuted, self.cipher_key, 'R')
        return permuted, n

    def __permute(self, message):
        chunks, n = self.split_message( message, self.block_size)
        perms = self.get_permutations(n, self.seed)
        substituted = []
        p = []
        count = 0
        for perm in perms:
            for ind, val in enumerate(perm):
                if val == '1':
                    if count % 2 == 0:
                        substituted.append(self.cieser_shift(chunks[ind], random.randrange(1, self.cipher_key), 'L'))
                    else:
                        substituted.append(self.cieser_shift(chunks[ind], random.randrange(1, self.cipher_key), 'R'))
                    p.append(ind)
                    #substituted.append(chunks[ind])
                    count += 1
        return ''.join(substituted), n



