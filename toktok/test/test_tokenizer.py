
# -*- coding: utf-8 -*-

"""
Tests for toktok Tokenizer
"""

import unittest

from toktok.tokenize import Tokenizer

class TestTokenzier(unittest.TestCase):
    def test_toktok_tokenize(self):
        # Tokenize a sentence.
        toktok = Tokenizer()
        text = u'Is 9.5 or 525,600 my favorite number?'
        expected_str = u'Is 9.5 or 525,600 my favorite number ?'
        tokenized_text = toktok.tokenize(text, return_str=True)
        assert tokenized_text == expected_str

    def test_toktok_tokenize_url(self):
        # Test sentence with url.
        toktok = Tokenizer()
        text = u'The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things'
        expected_str = u'The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things'
        tokenized_text = toktok.tokenize(text, return_str=True)
        assert tokenized_text == expected_str

    def test_toktok_tokenize_weird_symbols(self):
        # Test sentence with weird symbols.
        toktok = Tokenizer()
        text = u'\xa1This, is a sentence with weird\xbb symbols\u2026 appearing everywhere\xbf'
        expected_str = u'\xa1 This , is a sentence with weird \xbb symbols \u2026 appearing everywhere \xbf'
        expected_tokens = [u'\xa1', u'This', u',', u'is', u'a', u'sentence', u'with', u'weird', u'\xbb', u'symbols', u'\u2026', u'appearing', u'everywhere', u'\xbf']

        tokenized_text_str = toktok.tokenize(text, return_str=True)
        assert tokenized_text_str == expected_str

        tokenized_text = toktok.tokenize(text)
        assert tokenized_text == expected_str



    >>> toktok = ToktokTokenizer()
    >>> text = u'Is 9.5 or 525,600 my favorite number?'
    >>> print (toktok.tokenize(text, return_str=True))
    Is 9.5 or 525,600 my favorite number ?
    >>> text = u'The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things'
    >>> print (toktok.tokenize(text, return_str=True))
    The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things
    >>> text = u'\xa1This, is a sentence with weird\xbb symbols\u2026 appearing everywhere\xbf'
    >>> expected = u'\xa1 This , is a sentence with weird \xbb symbols \u2026 appearing everywhere \xbf'
    >>> assert toktok.tokenize(text, return_str=True) == expected
    >>> toktok.tokenize(text) == [u'\xa1', u'This', u',', u'is', u'a', u'sentence', u'with', u'weird', u'\xbb', u'symbols', u'\u2026', u'appearing', u'everywhere', u'\xbf']
    True
