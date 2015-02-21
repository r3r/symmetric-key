__author__ = 'RiteshReddy'
from Base_Crypt import Base_Crypt
import random
class Encrypt(Base_Crypt):

    def __init__(self, seed, num_blocks, cipher_key):
        self.seed = seed
        self.cipher_key = cipher_key
        self.num_blocks = num_blocks

    def encrypt(self, message):
        message = self.padd_message(message, self.num_blocks)
        permuted  = self.__permute(message)
        #substituted = self.cieser_shift(permuted, self.cipher_key, 'R')
        return permuted

    def __permute(self, message):
        chunks  = self.split_message( message, self.num_blocks)
        perms = self.get_permutations(self.num_blocks, self.seed)
        substituted = []
        seen = [False] * self.num_blocks
        p = []
        count = 0
        for perm in perms:
            for ind, val in enumerate(perm):
                if val == '1' and seen[ind] == False:
                    p.append(ind)
                    #substituted.append(chunks[ind])
                    if count % 2 == 0:
                        substituted.append(self.cieser_shift(chunks[ind], random.randrange(1, self.cipher_key), 'L'))
                    else:
                        substituted.append(self.cieser_shift(chunks[ind], random.randrange(1, self.cipher_key), 'R'))

                    seen[ind] = True
                    count += 1
        return ''.join(substituted)



