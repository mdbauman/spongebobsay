#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""That meme is now on your terminal"""

import sys
import codecs
import os
import random
import shutil

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

#TODO don't need apparently - there's a textwrap module!
def wrap_text(args):
    terminal_size = shutil.get_terminal_size(fallback=(80, 20))
    cols = 40 if terminal_size.columns>40 else terminal_size.columns

    ret = []
    ret.append('')
    for word in args:
        line = ret[-1]
        newline = (line + ' ' + word).strip()
        if(len(newline)<=cols):
            ret[-1]=newline
        else:
            ret.append('')
    return ret

#TODO make balloon

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


wrap_text(sys.argv[1:])
print_bob(get_bob())
