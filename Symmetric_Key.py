__author__ = 'RiteshReddy'
from Encrypt import Encrypt
from Decrypt import Decrypt
import random
import time
class Symmetric_Key():
    blocks = None
    def __init__(self, seed, block_size, cipher_key):
        self.seed = seed
        self.cipher_key = cipher_key
        self.block_size = block_size

    def encrypt(self, message):
        encryptor = Encrypt(self.seed, self.block_size, self.cipher_key)
        msg, self.blocks =  encryptor.encrypt(message)
        return msg, self.blocks

    def decrypt(self, cipher, num_blocks):
        decryptor = Decrypt(self.seed, self.block_size, self.cipher_key, num_blocks)
        return decryptor.decrypt(cipher)


def driver():
    strings = ["Hello My Name is Ritesh!",
                "NSA NSA NSA SECRET!!!",
                "COOL STUFF!",
                "The quick fox jumped over the lazy brown dog!"]
    for string in strings:
        random.seed(time.time())
        sm = Symmetric_Key(random.randrange(512), random.randrange(2, 10), random.randrange(1,26))
        enc, blocks = sm.encrypt(string)
        dec = sm.decrypt(enc, blocks)
        print "Seed: ", sm.seed
        print "Block Size: ", sm.block_size
        print "Cipher Key: ", sm.cipher_key
        print "Num Blocks: ", blocks
        print "Original: ", string
        print "Encrypted: ", enc, "Length: ", len(enc)
        print "Decrypted: ", dec
        print

driver()
