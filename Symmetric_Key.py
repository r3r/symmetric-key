__author__ = 'RiteshReddy'
from Encrypt import Encrypt
from Decrypt import Decrypt
import random
import time
class Symmetric_Key():
    blocks = None
    def __init__(self, seed, num_blocks, cipher_key):
        self.seed = seed
        self.cipher_key = cipher_key
        self.num_blocks = num_blocks

    def encrypt(self, message):
        encryptor = Encrypt(self.seed, self.num_blocks, self.cipher_key)
        msg =  encryptor.encrypt(message)
        return msg

    def decrypt(self, cipher):
        decryptor = Decrypt(self.seed, self.num_blocks, self.cipher_key)
        return decryptor.decrypt(cipher)


def driver():
    strings = ["Hello My Name is Ritesh!",
                "NSA NSA NSA SECRET!!!",
                "COOL STUFF!",
                "The quick brown fox jumped over the lazy dog!"]
    for string in strings:
        random.seed(time.time())
        sm = Symmetric_Key(random.randrange(512), random.randrange(1,15), random.randrange(1, 256))
        enc = sm.encrypt(string)
        dec = sm.decrypt(enc)
        print "Seed: ", sm.seed
        print "Cipher Key: ", sm.cipher_key
        print "Num Blocks: ", sm.num_blocks
        print "Original: ", string, "Length: ", len(string)
        print "Encrypted: ", enc, "Length: ", len(enc)
        print "Decrypted: ", dec, "Length: ", len(dec)
        print "Success!" if dec == string else "Failure!!"
        print

driver()
