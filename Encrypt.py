__author__ = 'RiteshReddy'
from Base_Crypt import Base_Crypt

class Encrypt(Base_Crypt):

    def __init__(self, seed, block_size, cipher_key):
        self.seed = seed
        self.cipher_key = cipher_key
        self.block_size = block_size

    def encrypt(self, message):
        message = self.padd_message(message, self.block_size)
        permuted, n = self.__permute(message)
        substituted = self.cieser_shift(permuted, self.cipher_key, 'R')
        return substituted, n

    def __permute(self, message):
        chunks, n = self.split_message( message, self.block_size)
        perms = self.get_permutations(n, self.seed)
        substituted = []
        p = []
        for perm in perms:
            for ind, val in enumerate(perm):
                if val == '1':
                    p.append(ind)
                    substituted.append(chunks[ind])
        return ''.join(substituted), n



