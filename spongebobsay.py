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
import argparse

#force utf-8 writer in case terminal is a silly encoding
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def derpify_text(words):
    ret = []
    for word in words:
        uc = ''.join(random.choice([c.upper(), c.lower()]) for c in word)
        ret.append(uc)
    return ret

def wrap_text(words, width):
    if not width:
        terminal_size = shutil.get_terminal_size(fallback=(80, 20))
        width = 40 if terminal_size.columns>40 else terminal_size.columns

    return textwrap.wrap(' '.join(words),int(width))

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
    
    balloon = balloon + last_line+'\n  \\\n   \\\n'
    return balloon

def random_bob():
    files = []
    for fname in os.listdir(SCRIPT_DIR+'/bobs'):
        files.append(fname)
    return random.choice(files)

def print_bob(fname):
    with codecs.open(SCRIPT_DIR+'/bobs/'+fname, 'r', encoding='unicode_escape') as file:
        lines = file.readlines()
        for line in lines:
            print(line, end='')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nowrap', help="Disable automatic line wrap", action='store_true')
    parser.add_argument('-d', '--derpify', help="Derpify text", action='store_true')
    parser.add_argument('-w', '--width', help="Set max width, ignored if using -n", action='store')
    parser.add_argument('-f', '--file', help="Specify .bob file, ex. 'mocking.bob'", action='store')
    opts, text = parser.parse_known_args()

    #cesi n'est pas une pipe
    if(len(text)==0):
        for line in sys.stdin:
            text.append(line)
    
    if opts.derpify:
        text = derpify_text(text)
    if opts.nowrap:
        lines = ''.join(text).rstrip().split('\n')
    else:
        lines = wrap_text(text, opts.width)
    if opts.file:
        bobfile = SCRIPT_DIR+'/bobs/'+opts.f
    else:
        bobfile = random_bob()

    if(lines==str(lines)):
        lines = [lines,]

    balloon = make_balloon(lines)
    print(balloon)
    print_bob(bobfile)
    print('\033[m') #default color

if __name__ == '__main__':
    main()
