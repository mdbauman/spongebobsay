#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""That one meme is now on your terminal
By Matt Bauman 2017 github.com/mdbauman"""

import sys
import codecs
import os
import random
import shutil
import textwrap

#force utf-8 writer in case terminal is a silly encoding
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

def derpify_text(words):
    ret = []
    for word in words:
        uc = ''.join(random.choice([c.upper(), c.lower()]) for c in word)
        ret.append(uc)
    return ret

def wrap_text(words):
    terminal_size = shutil.get_terminal_size(fallback=(80, 20))
    width = 40 if terminal_size.columns>40 else terminal_size.columns

    return textwrap.wrap(' '.join(words),width)

def make_balloon(lines):
    max_len = max(len(line) for line in lines)
    first_line = ' '+'_'*(max_len+2)
    last_line = ' '+'-'*(max_len+2)

    balloon = first_line+'\n'
    for line in lines:
        if(len(lines)==1):
            balloon = balloon+'< '+line+' >\n'
        elif(line==lines[0]):
            balloon = balloon+'/ '+line.ljust(max_len,' ')+' \\\n'
        elif(line==lines[-1]):
            balloon = balloon+'\\ '+line.ljust(max_len,' ')+' /\n'
        else:
            balloon = balloon+'| '+line.ljust(max_len,' ')+' |\n'
    
    balloon = balloon + last_line+'\n  \\\n   \\\n    \\\n'
    return balloon

def get_bob():
    files = []
    for fname in os.listdir('bobs'):
        files.append(fname)
    return random.choice(files)

def print_bob(fname):
    with codecs.open('bobs/'+fname, 'r', encoding='unicode_escape') as file:
        lines = file.readlines()
        for line in lines:
            print(line, end='')

def main():
    words = derpify_text(sys.argv[1:])
    lines = wrap_text(words)
    balloon = make_balloon(lines)
    print(balloon)
    #print(lines)
    #print_bob(get_bob())

if __name__ == '__main__':
    main()