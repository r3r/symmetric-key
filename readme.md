#Symmetric Key Encryption 

##Overview
* Block Oriented Cipher
* Input is broken up into either N blocks(version 2) or blocks of size B (Version 1.*)
* There are two keys: a Seed for a psuedo-random generator and an alphabetic shift cipher key
* The seed is used to generate a series of bitmaps of length N until each position 1...N has a 1 in at least one of the bitmaps
* * Based on the 1s in the sequences of the N bit bitmaps, the corresponding Nth block is chosen when traversing the permutations from the first to last, left to right.
* On each choice of a block, the characters in the block are then alphabetically shifted either to the right or left depending on whether it is an odd block or an even block.

##Version key
* Each version is in its own branch
* Version 1.* : Input is broken up into blocks of size B which is unique for each input message and is also needed for decryption, i.e., this version has 3 keys one that is generated based on the input text
    * Version 1.0: Simple permutation. The shift occurs at the end of all permutations on one stream of text in one direction only
    * Version 1.5: Permutation with shifts occurring in both directions on each choice of the blocks
    * Version 1.75: Permutation with shifts occurring in both directions on each choice of the blocks and insertion of truly random garbage blocks instead of repeating previously seen blocks
* Version 2 : Input is broken up into N blocks. The block sizes vary depending on the length of the text. Only require two keys: the seed and cipher key for decryption.
    * Not possible to insert garbage blocks within text as N is fixed and hence the decryption algorithm expects N blocks of the same size that the encryption algorithm broke the text into.

##How to run
* Symmetric_Key is the API for the encryption and decryption classes.
* Simply run the driver() function in Symmetric_Key.py file for sample usage.

##inspired by John Shaegan's research
