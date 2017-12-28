# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hazm import *
from FileReader import *
from ExtractKeyword import extract_keyword_from_text
from FindWordRepeats import find_word_repeats


def find_repeats_from_file(address):
    matn = read_from_file(address)
    keywords = extract_keyword_from_text(matn)
    repeats = find_word_repeats(keywords)
    return repeats

