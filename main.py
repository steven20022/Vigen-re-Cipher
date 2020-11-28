# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pickle


def key():
    key_1 = {"a": "p", "b": "q", "c": "r", "d": "s", "e": "t", "f": "u", "g": "v", "h": "w", "i": "x", "j": "y", "k": "z", "l": "a", "m": "b", "n": "c", "o": "d", "p": "e", "q": "f", "r": "g", "s": "h", "t": "i", "u": "j", "v": "k", "w": "l", "x": "m", "y": "n", "z": "o"}
    key_2 = {"a": "y", "b": "z", "c": "a", "d": "b", "e": "c", "f": "d", "g": "e", "h": "f", "i": "g", "j": "h", "k": "i", "l": "j", "m": "k", "n": "l", "o": "m", "p": "n", "q": "o", "r": "p", "s": "q", "t": "r", "u": "s", "v": "t", "w": "u", "x": "v", "y": "w", "z": "x"}
    key_3 = {"a": "t", "b": "u", "c": "v", "d": "w", "e": "x", "f": "y", "g": "z", "h": "a", "i": "b", "j": "c", "k": "d", "l": "e", "m": "f", "n": "g", "o": "h", "p": "i", "q": "j", "r": "k", "s": "l", "t": "m", "u": "n", "v": "o", "w": "p", "x": "q", "y": "r", "z": "s"}
    key_4 = {"a": "h", "b": "i", "c": "j", "d": "k", "e": "l", "f": "m", "g": "n", "h": "o", "i": "p", "j": "q", "k": "r", "l": "s", "m": "t", "n": "u", "o": "v", "p": "w", "q": "x", "r": "y", "s": "z", "t": "a", "u": "b", "v": "c", "w": "d", "x": "e", "y": "f", "z": "g"}
    key_5 = {"a": "o", "b": "p", "c": "q", "d": "r", "e": "s", "f": "t", "g": "u", "h": "v", "i": "w", "j": "x", "k": "y", "l": "z", "m": "a", "n": "b", "o": "c", "p": "d", "q": "e", "r": "f", "s": "g", "t": "h", "u": "i", "v": "j", "w": "k", "x": "l", "y": "m", "z": "n"}
    key_6 = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z", "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"}

    return [key_1, key_2, key_3, key_4, key_5, key_6]


pickle.dump(key(), open("key.txt", "wb"))


def encrypt(string, file):

    string_ = string.lower()
    cypher = ""
    key = pickle.load(open(file, 'rb'))
    i = 0
    for chr_ in string_:
        ii = i % len(key)
        cypher += key[ii].get(chr_)
        i += 1
    return cypher


def decrypt(string, file):

    string_ = string.lower()
    cypher = ""
    key = pickle.load(open(file, 'rb'))
    reverse_key = [{value: key for (key, value) in key[0].items()}, {value: key for (key, value) in key[1].items()},
                   {value: key for (key, value) in key[2].items()}, {value: key for (key, value) in key[3].items()},
                   {value: key for (key, value) in key[4].items()}, {value: key for (key, value) in key[5].items()}]

    i = 0
    for chr_ in string_:
        ii = i % len(reverse_key)
        cypher += reverse_key[ii].get(chr_)
        i += 1
    return cypher


if __name__ == "__main__":
    word = input("Enter Word for Encrypting")
    e_word = encrypt(word,"key.txt")
    print(e_word)
    word = input("Enter Word for Decryption")
    print(decrypt(word, "key.txt"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
