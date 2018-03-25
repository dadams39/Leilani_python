#! /usr/bin/env python3
import sys

def entry():
    my_list = sys.argv
    return my_list[-1]

def main():
    print("Leilani is {} years old".format(12))
    print(entry())

    #loop entry 16 times
    last_word = entry()
    for x in enumerate(last_word):
        print(x)


if __name__ == "__main__":
    main()
