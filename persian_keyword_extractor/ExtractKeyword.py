# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hazm import *
from MeaninglessWords import meaningless_words


def extract_keyword_from_text(text):

    # aval matn e khod ra normal sazi mikonim
    normalizer = Normalizer()
    normalized_text = normalizer.normalize(text)

    # kalamat ra joda mikonim
    text_words = word_tokenize(normalized_text)

    # chack mikonim ke kalamati ke arzeshe ma naee nadarand dar an nabashand
    final_words = []
    for i in text_words:
        if i not in meaningless_words:
            final_words.append(i)

    return final_words