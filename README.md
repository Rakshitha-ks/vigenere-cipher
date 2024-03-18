# Vigenère Cipher 
_Welcome to Vigenère Cipher and Decipher repository! This project features a classic old cryptography technique using python._


Table of Contents
-------------
1. [Introduction](#Introduction)
2. [Cryptanalysis](#Cryptanalysis)
3. [Output Preview](#Preview)

Introduction
-------------
   Vigenère Cipher is a method of encrypting alphabetic text. 
   It uses a simple form of polyalphabetic substitution. 
   A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets.
   Vigenère ciphertext is a combination of a Caesar shift combined with a keyword. 
   The length of the keyword determines the number of different encryptions that are applied to the plaintext.

Cryptanalysis
-------------
The strength of the Vigenère cipher is that it is not susceptible to frequency analysis due to the fact that the cipher rotates through different shifts, so the same plaintext letter will not always be encrypted to the same ciphertext letter.However, since a Vigenère cipher encodes the same letter in different ways, depending on the keyword,thus breaking the assumptions behind frequency analysis.  As such, they were regarded by many as unbreakable for 300 years.

A Vigenère cipher is difficult to crack using brute-force because each letter in a message could be encoded as any of the _26_ letters. Because the encoding of the message depends on the keyword used, a given message could be encoded in _26^k_ ways, where _k_ is the length of the keyword.

The primary weakness of the Vigenère cipher is the repeating nature of its key. If a cryptanalyst correctly guesses the length of the key, then the ciphertext can be treated as interwoven Caesar ciphers, which, individually, can be easily broken. Repetitions in the ciphertext indicate repetitions in the plaintext, and the space between such repetitions hint at the length of the keyword.

Preview
-------------
***Encryption*** :
![v_encrypt](https://github.com/Rakshitha-ks/vigenere-cipher/assets/130575059/ec595a48-6225-4f7a-b471-82515582c4ad)

***Decryption*** :
![v_decrypt](https://github.com/Rakshitha-ks/vigenere-cipher/assets/130575059/1ddebf1e-7199-46ff-94b6-634b7223f9a8)



